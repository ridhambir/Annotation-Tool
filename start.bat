@echo off
REM Start Backend (Flask)
echo Starting Flask Backend on port 5000...
start cmd /k "cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python app.py"

REM Wait a moment for backend to start
timeout /t 3

REM Start Frontend (React)
echo Starting React Frontend on port 3000...
start cmd /k "cd frontend && npm install && npm start"

echo.
echo Both servers are starting:
echo - Frontend: http://localhost:3000
echo - Backend: http://localhost:5000
echo.
pause
