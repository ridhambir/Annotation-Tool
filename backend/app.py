from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import base64
import uuid
from inference.model_infer import infer_image

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_image(image_path):
    """
    Process the image with your model logic here.
    For now, it returns the image info without Pillow dependency.
    You can replace this with your actual ML model inference.
    """
    try:
        # Read file and get basic info
        file_size = os.path.getsize(image_path)
        
        # Read and encode image to base64 for frontend display
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        # Determine media type
        _, ext = os.path.splitext(image_path)
        media_type = f'image/{ext.lower().lstrip(".")}'
        img_base64 = base64.b64encode(image_data).decode()
        
        return file_size, img_base64, media_type
    except Exception as e:
        raise Exception(f"Image processing error: {str(e)}")


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check if file is allowed
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed. Allowed types: png, jpg, jpeg, gif, bmp'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        filename = f"{uuid.uuid4().hex}_{filename}"
        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(upload_path)
        
        # Process image (basic read for frontend preview)
        file_size, img_base64, media_type = process_image(upload_path)

        # Run model inference (uses ultralytics RTDETR wrapper)
        try:
            # save annotated outputs so frontend can display them
            inference_results = infer_image(upload_path, device='cpu', conf=0.25, save=True, name=None)
        except Exception as e:
            inference_results = {'error': f'Inference failed: {str(e)}'}

        # Build accessible URLs for any saved annotated images
        annotated_urls = []
        if isinstance(inference_results, dict) and 'saved' in inference_results:
            run_name = inference_results.get('run_name')
            # saved paths are absolute; construct route URLs based on run_name
            for saved_path in inference_results.get('saved', []):
                fname = os.path.basename(saved_path)
                # URL: /runs/<run_name>/<fname>
                host = request.host_url.rstrip('/')
                annotated_urls.append(f"{host}/runs/{run_name}/{fname}")

        return jsonify({
            'message': 'Image uploaded and processed successfully',
            'original_filename': file.filename,
            'uploaded_filename': filename,
            'file_size': file_size,
            'image_url': f'data:{media_type};base64,{img_base64}',
            'inference': inference_results,
            'annotated': annotated_urls
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'Backend is running'}), 200


@app.route('/runs/<run_name>/<path:filename>')
def serve_run_image(run_name, filename):
    # Serve saved annotated images from backend/runs/<run_name>/
    runs_root = os.path.join(os.path.dirname(__file__), 'runs')
    folder = os.path.join(runs_root, run_name)
    if not os.path.exists(folder):
        return jsonify({'error': 'Run not found'}), 404
    return send_from_directory(folder, filename)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
