# 🍃 Leaf Animation UI - Complete Documentation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Quick Start](#quick-start)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Installation Guide](#installation-guide)
6. [Running the Application](#running-the-application)
7. [API Documentation](#api-documentation)
8. [Customization Guide](#customization-guide)
9. [Deployment](#deployment)
10. [Troubleshooting](#troubleshooting)

---

## 🎨 Project Overview

A beautiful, modern web application featuring:
- **Animated green leaves** continuously falling on a **black background**
- **Image upload interface** with green styling and glowing effects
- **Flask backend** for image processing and storage
- **Real-time image processing** with file validation
- **Fully responsive design** for desktop and mobile

**Live Demo Flow:**
1. Open the app → See animated leaves falling
2. Click "Choose Image" in the form
3. Select an image file
4. Click "Upload & Process"
5. View the processed result

---

## 🚀 Quick Start

### Windows Users (Easiest)
```bash
# Double-click start.bat in the project root
start.bat
```

### All Platforms (Manual)
```bash
# Terminal 1: Start Backend
cd backend
python -m venv venv
venv\Scripts\activate  # or: source venv/bin/activate (Mac/Linux)
pip install -r requirements.txt
python app.py

# Terminal 2: Start Frontend
cd frontend
npm install
npm start
```

**URLs:**
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

---

## ✨ Key Features

### 🍃 Animated Leaf Background
- 15 animated green leaves with realistic falling motion
- Random speeds and patterns for each leaf
- Smooth rotations and fade effects
- Built with Framer Motion library
- Continuously loops without stopping

### 📤 Image Upload Section
- Black background with glowing green border
- File preview before submission
- Green submit button with hover effects
- Real-time error messages
- Displays processed image immediately after upload

### 🛡️ Image Processing
- Automatic file validation (type & size)
- Supported formats: PNG, JPG, JPEG, GIF, BMP
- Auto-resize to max 800x800px
- JPEG compression (85% quality)
- Unique filename generation

### 🎭 Professional Styling
- Dark theme with green accents
- Glow effects on buttons and borders
- Smooth animations and transitions
- Mobile-responsive layout
- Accessible form controls

---

## 📁 Project Structure

```
Project/
├── 📄 README.md                    # Main documentation
├── 📄 QUICKSTART.md                # Quick start guide
├── 📄 SETUP_SUMMARY.md             # Setup summary
├── 📄 INDEX.md                     # This file
├── ⚙️ .gitignore                   # Git configuration
├── 🦇 start.bat                    # Windows startup script
├── 🐳 docker-compose.yml           # Docker configuration
│
├── 📦 frontend/                    # React Application (Port 3000)
│   ├── 📄 package.json             # Node dependencies
│   ├── 📄 Dockerfile               # Docker image config
│   ├── 📄 .env.example             # Environment variables template
│   ├── 📁 public/
│   │   └── index.html              # HTML entry point
│   └── 📁 src/
│       ├── App.js                  # Main app component
│       ├── index.js                # React entry point
│       ├── config.js               # API configuration
│       ├── 📁 components/
│       │   ├── LeafAnimation.js    # ✨ Animated leaves
│       │   └── ImageUpload.js      # 📤 Upload form
│       └── 📁 styles/
│           └── App.css             # 🎨 All styling
│
└── 🐍 backend/                     # Flask Application (Port 5000)
    ├── 📄 app.py                   # Flask server & processing
    ├── 📄 requirements.txt         # Python dependencies
    ├── 📄 Dockerfile               # Docker image config
    ├── 📄 .env.example             # Environment variables template
    └── 📁 uploads/                 # Processed images storage
```

---

## 📥 Installation Guide

### Prerequisites
- **Node.js** v14+ (https://nodejs.org/)
- **Python** 3.8+ (https://www.python.org/)
- **npm** (comes with Node.js)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Installed packages:**
- Flask 2.3 - Web framework
- Flask-CORS 4.0 - Cross-origin support
- Pillow 10.0 - Image processing
- Werkzeug 2.3 - WSGI utilities
- Gunicorn 21.2 - Production server
- Python-dotenv 1.0 - Environment variables

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

**Main dependencies:**
- React 18 - UI library
- Framer Motion 10.16 - Animation library
- Axios 1.6 - HTTP client
- React Scripts 5.0 - Build tool

---

## ▶️ Running the Application

### Method 1: Windows (Easiest)
```bash
# From project root, double-click:
start.bat
```

### Method 2: Manual (Terminal 1 - Backend)
```bash
cd backend
venv\Scripts\activate  # Windows
python app.py
# → Backend running on http://localhost:5000
```

### Method 2: Manual (Terminal 2 - Frontend)
```bash
cd frontend
npm start
# → Frontend opens at http://localhost:3000
```

### Method 3: Docker
```bash
# From project root
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## 🔌 API Documentation

### Endpoint: Upload Image

**POST** `/upload`

**Description:** Upload an image, process it, and return the result

**Request:**
```
Content-Type: multipart/form-data

{
  "file": <image_file>
}
```

**Supported File Types:**
- PNG (.png)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- Bitmap (.bmp)

**Size Limit:** 16 MB

**Response (Success - 200):**
```json
{
  "message": "Image processed successfully",
  "original_filename": "vacation.jpg",
  "processed_filename": "processed_a1b2c3d4.jpg",
  "image_url": "data:image/jpeg;base64,/9j/4AAQSkZJRg...",
  "image_size": "800x600"
}
```

**Response (Error - 400/500):**
```json
{
  "error": "File type not allowed. Allowed types: png, jpg, jpeg, gif, bmp"
}
```

---

### Endpoint: Health Check

**GET** `/health`

**Description:** Check if backend is running

**Response (200):**
```json
{
  "status": "Backend is running"
}
```

---

## 🎨 Customization Guide

### 1. Customize Leaf Animation

Edit: `frontend/src/components/LeafAnimation.js`

```javascript
// Change number of leaves
Array.from({ length: 15 })  // Change 15 to your number

// Change leaf character
<motion.div>🍃</motion.div>  // Change to 🌿, ❄️, etc.

// Change animation duration
duration: 8 + Math.random() * 4  // Adjust the range

// Change leaf color
color: #00b300  // Edit in App.css
```

### 2. Customize Colors

Edit: `frontend/src/styles/App.css`

Replace `#00b300` (current green) with your color:
```css
/* Examples */
#00b300  /* Green */
#FF6B6B  /* Red */
#4ECDC4  /* Teal */
#FFE66D  /* Yellow */
#95E1D3  /* Mint */
```

### 3. Customize Upload Form

Edit: `frontend/src/components/ImageUpload.js`

```javascript
// Change form title
<h1>Image Upload</h1>

// Change button text
<button>{uploading ? 'Uploading...' : 'Upload & Process'}</button>

// Add more file types (in ImageUpload.js and app.py)
```

### 4. Add ML Model Processing

Edit: `backend/app.py` (line 36-50)

```python
def process_image(image_path):
    """Replace with your model inference"""
    img = Image.open(image_path)
    
    # Your ML model processing here
    from your_model import predict
    result = predict(img)
    
    # Process based on result...
    
    return output_filename, img
```

### 5. Configuration Files

Edit: `frontend/.env`
```
REACT_APP_API_URL=http://localhost:5000
```

Edit: `backend/.env`
```
FLASK_ENV=development
MAX_FILE_SIZE_MB=16
```

---

## 🚀 Deployment

### Deploy Frontend (Vercel)

1. Push code to GitHub
2. Create account at https://vercel.com
3. Import repository
4. Set environment variable: `REACT_APP_API_URL=<your-backend-url>`
5. Deploy

### Deploy Backend (Render or Heroku)

1. Push backend code to GitHub
2. Create account at https://render.com or https://heroku.com
3. Create new service
4. Set environment: `FLASK_ENV=production`
5. Deploy

### Deploy with Docker

```bash
# Build images
docker-compose build

# Push to Docker Hub
docker tag project-frontend:latest yourusername/frontend:latest
docker tag project-backend:latest yourusername/backend:latest
docker push yourusername/frontend:latest
docker push yourusername/backend:latest

# Deploy (AWS, Digital Ocean, etc.)
docker pull yourusername/frontend:latest
docker pull yourusername/backend:latest
docker-compose up -d
```

---

## 🔧 Troubleshooting

### Issue: "Port 3000 already in use"
```bash
# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:3000 | xargs kill -9
```

### Issue: "Port 5000 already in use"
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

### Issue: npm install fails
```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and lock file
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

### Issue: Python packages won't install
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Try again
pip install -r requirements.txt
```

### Issue: CORS error when uploading
- Verify Flask backend is running on http://localhost:5000
- Check `ImageUpload.js` has correct API URL
- Verify Flask-CORS is installed

### Issue: Images not uploading
1. Check browser console (F12) for errors
2. Verify file format is PNG/JPG/GIF/BMP
3. Verify file size is under 16MB
4. Check Flask logs for error details
5. Ensure `uploads/` folder exists and is writable

### Issue: Leaves not animated
1. Verify Framer Motion is installed: `npm list framer-motion`
2. Check browser console for JavaScript errors
3. Try clearing browser cache (Ctrl+Shift+Delete)

---

## 📊 Performance Tips

- **Frontend**: Image size limited to 800x800px before upload
- **Backend**: JPEG compression at 85% quality
- **Network**: Base64 encoding for immediate display
- **Storage**: Uploaded images stored in `backend/uploads/`

---

## 🔐 Security Considerations

- File type validation (whitelist only image types)
- File size limits (16MB max)
- Filename sanitization with `secure_filename()`
- Unique filenames with UUID generation
- CORS configured for development (restrict in production)

---

## 📚 Additional Resources

- **React Documentation**: https://react.dev
- **Framer Motion**: https://www.framer.com/motion/
- **Flask Documentation**: https://flask.palletsprojects.com/
- **Pillow Documentation**: https://pillow.readthedocs.io/
- **Axios Documentation**: https://axios-http.com/

---

## 💡 Tips & Tricks

1. **Hot Reload**: Frontend automatically reloads on save
2. **Debug Mode**: Flask has debug mode enabled in development
3. **Mobile Testing**: Use browser DevTools (F12) device emulation
4. **API Testing**: Visit `http://localhost:5000/health` to test backend
5. **Image Optimization**: Images auto-resize on backend

---

## 📝 License

MIT - Free to use and modify

---

## 🎉 Next Steps

1. ✅ Run the application
2. ✅ Test image upload
3. ✅ Customize colors and leaves
4. ✅ Integrate your ML model
5. ✅ Deploy to production

**Happy coding! 🍃**

For more help, see:
- QUICKSTART.md - Quick start guide
- README.md - Full documentation
- SETUP_SUMMARY.md - Setup details
