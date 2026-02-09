# Leaf Animation UI with Image Upload

A full-stack web application featuring an animated green leaf background and an image upload section connected to a Flask backend for image processing.

## Features

- **Animated Leaf Background**: 15 animated green leaves falling with random patterns on a black background using Framer Motion
- **Image Upload Section**: Green-bordered upload form with preview functionality
- **Flask Backend**: Handles image processing and storage
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Processing**: Uploads and processes images through the backend API

## Project Structure

```
Project/
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── LeafAnimation.js
│   │   │   └── ImageUpload.js
│   │   ├── styles/
│   │   │   └── App.css
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
└── backend/
    ├── uploads/
    ├── app.py
    └── requirements.txt
```

## Installation

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will open at `http://localhost:3000`

### Backend Setup

1. Navigate to the backend directory in a **separate terminal**:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

## Usage

1. **Start both servers**: 
   - Frontend on `http://localhost:3000`
   - Backend on `http://localhost:5000`

2. **Upload an Image**:
   - Click on "Choose Image" button
   - Select an image from your computer (PNG, JPG, JPEG, GIF, BMP)
   - Click the image preview to change it
   - Click "Upload & Process" button

3. **View Results**:
   - The processed image will be displayed in the "Processing Result" section
   - Image information (dimensions, filename) is shown

## API Endpoints

### POST `/upload`
Uploads and processes an image.

**Request**:
- Form data with `file` field containing the image

**Response**:
```json
{
  "message": "Image processed successfully",
  "original_filename": "photo.jpg",
  "processed_filename": "processed_xyz.jpg",
  "image_url": "data:image/jpeg;base64,...",
  "image_size": "800x600"
}
```

### GET `/health`
Health check endpoint.

**Response**:
```json
{
  "status": "Backend is running"
}
```

## Customization

### Leaf Animation
Edit `frontend/src/components/LeafAnimation.js` to:
- Change number of leaves: Modify `Array.from({ length: 15 })`
- Adjust fall speed: Change `duration` values
- Modify leaf emoji: Replace '🍃' with another character
- Change colors: Modify the `color` property in `.leaf` CSS

### Upload Section Styling
Edit `frontend/src/styles/App.css` to:
- Change the green color from `#00b300` to your preference
- Adjust border radius and padding
- Modify animation durations in `@keyframes glow`

### Backend Processing
Edit `backend/app.py` in the `process_image()` function to:
- Add your own image processing logic
- Integrate ML models for image analysis
- Apply filters or transformations
- Extract features or metadata

## File Size Limits

- Maximum file size: 16MB
- Images will be resized to fit within 800x800px
- Supported formats: PNG, JPG, JPEG, GIF, BMP

## Technologies Used

### Frontend
- React 18
- Framer Motion (animations)
- Axios (API calls)
- CSS3

### Backend
- Flask 2.3
- Flask-CORS (cross-origin requests)
- Pillow (image processing)
- Werkzeug (file upload handling)

## Troubleshooting

### "Cannot POST /upload" Error
- Make sure the Flask backend is running on port 5000
- Check that CORS is properly configured in `app.py`
- Verify the API endpoint URL in `ImageUpload.js`

### Images Not Uploading
- Check browser console for errors (F12)
- Ensure file size is under 16MB
- Verify file format is supported
- Check backend terminal for error messages

### Leaves Not Visible
- Make sure you're on the correct frontend URL (http://localhost:3000)
- Check browser console for JavaScript errors
- Verify Framer Motion is installed: `npm list framer-motion`

### Port Already in Use
```bash
# For port 3000 (React)
netstat -ano | findstr :3000

# For port 5000 (Flask)
netstat -ano | findstr :5000
```

Kill the process using the port or change the port in the configuration.

## Future Enhancements

- Add image filters (grayscale, blur, etc.)
- Integrate with ML models (object detection, image classification)
- Add image download functionality
- Implement image gallery for uploaded images
- Add drag-and-drop upload
- Create user authentication system
- Add image metadata display (EXIF data, dimensions, etc.)

## License

MIT

## Support

For issues or questions, please check the troubleshooting section or review the code comments.
