@echo off
taskkill /f /fi "imagename eq python.exe" /fi "windowtitle eq Smart Finger Counter" >nul 2>&1
if errorlevel 1 (
    echo Smart Finger Counter is not currently running.
) else (
    echo Smart Finger Counter stopped.
)

