@echo off
setlocal

REM Set Python version and download URL
set "PYTHON_VERSION=3.11.5"
set "PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe"
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%"

REM Debugging messages to ensure variables are set correctly
echo PYTHON_VERSION: %PYTHON_VERSION%
echo PYTHON_INSTALLER: %PYTHON_INSTALLER%
echo PYTHON_URL: %PYTHON_URL%

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Downloading Python...

    REM Download Python installer
    powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'"

    REM Install Python silently with pip
    start /wait "" "%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1

    REM Cleanup installer file
    del "%PYTHON_INSTALLER%"

    REM Refresh the environment variables to make Python and pip available immediately
    set "PATH=%PATH%;%ProgramFiles%\Python311\Scripts\;%ProgramFiles%\Python311\"

    echo Python installed successfully.
) else (
    echo Python is already installed.
)

REM Upgrade pip to the latest version
python -m ensurepip --upgrade
python -m pip install --upgrade pip

REM Install the termcolor and yt-dlp modules
pip install termcolor yt-dlp keyboard

echo termcolor, keyboard and yt-dlp modules installed successfully.

endlocal
pause
