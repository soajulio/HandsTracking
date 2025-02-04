# HandsTracking
 
# Project 1: Volume tracking with finger gestures (PYCaw + MediaPipe)

## Description
This project uses **PYCaw** to control the system volume based on the distance between the fingers of a hand detected via **MediaPipe**. The more fingers are spread apart, the more volume increases. The app allows intuitive volume control using the computer’s camera and hand gestures.

## Features
- Real-time tracking of finger movements via the camera.
- Control the volume of the system according to the spacing of the fingers.
- Display the current volume in percentage.

## Prerequisites
- **Python 3.x**
- **Libraries:**
  - `opencv-python` (for camera and image processing management)
  - `mediapipe` (for hand and gesture detection)
  - `pycaw`(to control the volume of the Windows system)

## Installation
1. Clone the project on your computer.
2. Make sure you have the necessary python libraries
3. Runs the file "Projet1.py": python Projet1.py

## Explanation of the code
1. Hand detection: Use MediaPipe to detect finger positions in the camera image.
2. Finger spacing calculation: The finger spacing is calculated, and this information is used to adjust the system volume via PYCaw.
3. Volume display: The current volume is displayed as a percentage and is adjusted dynamically when the finger spacing changes.

# Project 2

## Description
This project uses **MediaPipe** to detect raised fingers in real time via the camera and display an image corresponding to the number of raised fingers. Each image represents a specific number of fingers raised (0 to 5 fingers).

## Features
- Hand detection via the camera in real time.
- Counting fingers up.
- Display an image associated with the number of fingers raised, with a fixed position in the camera window.
- Support for a visual interface with OpenCV.

## Prerequisites
- **Python 3.x**
- **Libraries:**
    - `opencv-python` (for camera and image processing management)
    - `mediapipe` (for hand and gesture detection)

## Installation
1. Clone the project on your computer.
2. Make sure you have the necessary python libraries
3. Runs the "Projet2.py" file: python Projet2.py

## Explanation of the code
1. Hand detection: The code uses MediaPipe to detect the hand and hand markers in real time via the camera.
2. Counting raised fingers: Each finger is compared to determine whether or not it is raised based on its position.
3. Image display: Based on the number of fingers raised, an associated image (for example, ZeroFinger.png, OneFingers.png, etc) is displayed on screen in the video window. This image is resized and placed in a corner of the screen.
4. Mirror effect: The camera is displayed with a mirror effect for more intuitive interaction.