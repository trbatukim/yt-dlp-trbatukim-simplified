@echo off

set SCRIPT_DIR=%~dp0scripts

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to the system PATH.
    pause
    exit /b 1
)

cd /d "%SCRIPT_DIR%"
python "yt-dlp-trbatukim-Edition-Portable-win64-en.py"

echo.
echo Script execution finished. Press any key to exit...
pause >nul
