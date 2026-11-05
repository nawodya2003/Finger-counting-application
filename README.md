# Smart Finger Counter

A Python webcam application that detects up to two hands and shows how many fingers are raised in real time (0 to 10). It uses **OpenCV** for camera/video display and **MediaPipe** for hand landmark detection.

## Requirements

- Python 3.9 or newer (Python 3.11 is tested)
- A working webcam

## Installation

Open PowerShell in this project folder and install the dependencies:

```powershell
python -m pip install opencv-python mediapipe
```

## Run the application

```powershell
python finger_counter.py
```

A window named **Smart Finger Counter** opens and displays your camera feed with the detected finger count.

### Run with batch files

- Double-click `StartAll.bat` to start the application.
- Double-click `StopAll.bat` to force-close the running Smart Finger Counter window.

## Controls

- Hold one or two hands in front of the camera.
- Raise or fold fingers to change the displayed count.
- Press `q` while the camera window is selected to close the application.

## Troubleshooting

### `ModuleNotFoundError`

Install the missing packages with:

```powershell
python -m pip install opencv-python mediapipe
```

### Camera window does not open

- Make sure another program is not using the webcam.
- Check that Windows camera permissions allow desktop apps to use the camera.
- Confirm that your webcam is connected and detected by Windows.

### The count is inaccurate

- Use good, even lighting.
- Keep the hand fully visible and facing the camera.
- This version detects up to two hands and is most reliable with palms facing forward.

## Project files

- `finger_counter.py` - the main application.
- `test.py` - prints the installed MediaPipe package location; it is a setup check, not an automated test.
