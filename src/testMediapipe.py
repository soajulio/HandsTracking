import sys

try:
    import mediapipe as mp
    print("MediaPipe est bien installé !")
    print(f"Version : {mp.__version__}")
except ImportError:
    print("MediaPipe n'est pas installé. Installe-le avec :")
    sys.exit(1)