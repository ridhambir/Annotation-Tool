import os
import uuid
import logging

logging.basicConfig(level=logging.INFO)

# Attempt to import ultralytics; fail gracefully if not present
try:
    from ultralytics import RTDETR
    _HAS_ULTRALYTICS = True
    _IMPORT_ERROR = None
except Exception as e:
    RTDETR = None
    _HAS_ULTRALYTICS = False
    _IMPORT_ERROR = str(e)

# Path to model weights (adjust if needed)
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'best.pt')


def load_model(model_path=MODEL_PATH):
    """Load RTDETR model. Returns the model instance."""
    if not _HAS_ULTRALYTICS:
        raise RuntimeError(f"ultralytics is not installed: {_IMPORT_ERROR}")
    try:
        model = RTDETR(model_path)
        return model
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")


# Load once at import if possible
MODEL = None
if _HAS_ULTRALYTICS:
    try:
        MODEL = load_model()
    except Exception:
        MODEL = None


def infer_image(image_path, device='cpu', conf=0.25, save=False, name='result', project_dir=None):
    """
    Run inference on an image or folder. Returns a JSON-serializable dict with boxes, scores and class names.
    If ultralytics or the model is not available, returns an error dict instead of raising.
    """
    if not _HAS_ULTRALYTICS:
        return {'error': f"ultralytics not installed: {_IMPORT_ERROR}"}
    if MODEL is None:
        return {'error': 'Model not loaded (see server logs)'}

    try:
        # Ensure unique run name when saving to avoid overwriting or caching
        run_name = name if name else f"run_{uuid.uuid4().hex}"
        logging.info(f"Running inference on: {image_path} (run_name={run_name}, device={device}, conf={conf})")

        # Decide where to save annotated outputs
        if project_dir is None:
            project_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'runs')
        os.makedirs(project_dir, exist_ok=True)

        # Ultralytics RTDETR model callable
        # pass project and name so saved outputs are predictable: project/<name>/
        results = MODEL(image_path, save=save, device=device, conf=conf, name=run_name, project=project_dir, verbose=False)

        # results may be a list-like; take first
        res0 = results[0]

        out = {
            'source': image_path,
            'run_name': run_name,
            'project': project_dir,
            'saved': [],
            'boxes': [],
            'scores': [],
            'classes': [],
            'names': [],
        }

        # Try to extract boxes/scores/classes safely
        boxes = []
        scores = []
        classes = []

        if hasattr(res0, 'boxes') and res0.boxes is not None:
            try:
                xyxy = getattr(res0.boxes, 'xyxy', None)
                confs = getattr(res0.boxes, 'conf', None)
                clss = getattr(res0.boxes, 'cls', None)

                if xyxy is not None:
                    try:
                        boxes = xyxy.tolist()
                    except Exception:
                        boxes = [list(map(float, b)) for b in xyxy]
                if confs is not None:
                    scores = confs.tolist()
                if clss is not None:
                    classes = [int(c) for c in clss.tolist()]
            except Exception:
                # fallback: try tensor attributes
                try:
                    for b in res0.boxes:
                        boxes.append(getattr(b, 'xyxy', None))
                except Exception:
                    pass

        # Map class indices to names if available
        names = []
        model_names = getattr(MODEL, 'names', None)
        for c in classes:
            if model_names and int(c) in model_names:
                names.append(model_names[int(c)])
            else:
                names.append(str(c))

        out['boxes'] = boxes
        out['scores'] = scores
        out['classes'] = classes
        out['names'] = names

        # If outputs were saved, collect saved file paths (only common image extensions)
        if save:
            save_folder = os.path.join(project_dir, run_name)
            saved_files = []
            try:
                for fname in os.listdir(save_folder):
                    if fname.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                        saved_files.append(os.path.join(save_folder, fname))
            except Exception:
                saved_files = []
            out['saved'] = saved_files

        logging.info(f"Inference result: {len(boxes)} boxes for {image_path}; saved={len(out.get('saved',[]))}")

        return out

    except Exception as e:
        logging.exception("Inference failed")
        return {'error': str(e)}
