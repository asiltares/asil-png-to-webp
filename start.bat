@echo off
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo Python not found. Please install Python: https://www.python.org/downloads/
    pause
    exit /b 1
)

python -c "import PIL" >nul 2>nul
if errorlevel 1 (
    echo Installing Pillow...
    pip install Pillow
)

python png_to_webp.py
pause
