# Quick Start Guide

## Prerequisites

- Node.js and npm installed (https://nodejs.org/)
- Python 3.8+ installed (https://www.python.org/)

## Option 1: Automatic Setup (Windows)

1. Double-click `start.bat` in the project root
2. This will automatically:
   - Create Python virtual environment
   - Install all dependencies for backend
   - Start Flask server on port 5000
   - Install all dependencies for frontend
   - Start React dev server on port 3000
3. Wait for both servers to be ready
4. Open browser to `http://localhost:3000`

## Option 2: Manual Setup (All Platforms)

### Step 1: Install Backend Dependencies

Open a terminal/command prompt in the project root:

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Flask server
python app.py
```

Backend will start on http://localhost:5000

### Step 2: Install Frontend Dependencies

Open a **new terminal/command prompt** in the project root:

```bash
cd frontend

# Install dependencies
npm install

# Start React development server
npm start
```

Frontend will open on http://localhost:3000

## Testing the Application

1. **Test Backend Health**:
   - Open http://localhost:5000/health in browser
   - You should see: `{"status": "Backend is running"}`

2. **Test Upload Functionality**:
   - Open http://localhost:3000 in browser
   - Observe the animated green leaves falling in the background
   - Click "Choose Image" and select an image
   - Click "Upload & Process"
   - View the processed result

## Stopping the Servers

- **Terminal Method**: Press `Ctrl+C` in each terminal window
- **Task Manager**: Find and kill node.exe and python.exe processes

## Troubleshooting

### Port 3000 or 5000 Already in Use

**Windows:**
```bash
netstat -ano | findstr :3000
# Note the PID, then:
taskkill /PID <PID> /F

netstat -ano | findstr :5000
# Note the PID, then:
taskkill /PID <PID> /F
```

### npm install fails

Try clearing npm cache:
```bash
npm cache clean --force
rm -r node_modules package-lock.json
npm install
```

### Python package installation fails

Upgrade pip and try again:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### CORS Error when uploading

Make sure:
1. Flask backend is running on http://localhost:5000
2. Both `Access-Control-*` headers are present in Flask response
3. Browser console shows the actual error message

### Images not showing

1. Check browser console (F12) for JavaScript errors
2. Verify image format is supported (PNG, JPG, JPEG, GIF, BMP)
3. Check file size is under 16MB
4. Look at Flask server logs for processing errors

## Next Steps

1. **Customize Colors**: Edit the `#00b300` (green) color in `frontend/src/styles/App.css`
2. **Add ML Model**: Replace the image processing logic in `backend/app.py`
3. **Deploy**: Use services like Heroku, Render, or AWS for production deployment

## Useful Commands

```bash
# Frontend commands
npm start          # Start development server
npm build          # Build for production
npm test           # Run tests

# Backend commands
python app.py      # Run Flask server
python -m flask shell  # Interactive Flask shell
```

## File Locations

- Frontend entry: `frontend/src/index.js`
- Backend entry: `backend/app.py`
- Styles: `frontend/src/styles/App.css`
- Components: `frontend/src/components/`
- Uploaded images: `backend/uploads/`

Good luck! 🍃
