import cv2 as cv
import mediapipe as mp

# Charger les images associées aux doigts levés
images = [
    cv.imread("C:\IUT\BUTInfo3\Semestre2\App_Graphique\TP_Mediapipe\HandsTracking\imgs\ZeroFinger.png"),  # 0 doigt levé
    cv.imread("C:\IUT\BUTInfo3\Semestre2\App_Graphique\TP_Mediapipe\HandsTracking\imgs\OneFingers.png"),  # 1 doigt levé
    cv.imread("C:\IUT\BUTInfo3\Semestre2\App_Graphique\TP_Mediapipe\HandsTracking\imgs\TwoFingers.png"),  # 2 doigts levés
    cv.imread("C:\IUT\BUTInfo3\Semestre2\App_Graphique\TP_Mediapipe\HandsTracking\imgs\ThreeFingers.png"),  # 3 doigts levés
    cv.imread("C:\IUT\BUTInfo3\Semestre2\App_Graphique\TP_Mediapipe\HandsTracking\imgs\FourFingers.png"),  # 4 doigts levés
    cv.imread("C:\IUT\BUTInfo3\Semestre2\App_Graphique\TP_Mediapipe\HandsTracking\imgs\FiveFingers.png")   # 5 doigts levés
]

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)  # Effet miroir pour un affichage intuitif
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    total_fingers = 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # Stocker les coordonnées des landmarks
            landmarks = {}
            h, w, _ = img.shape

            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks[id] = (cx, cy)

            if len(landmarks) >= 21:
                fingers = []

                # Pouce (comparaison en X)
                if landmarks[4][0] > landmarks[2][0]:  # Main droite
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Autres doigts (comparaison en Y)
                for tip, pip in [(8, 6), (12, 10), (16, 14), (20, 18)]:
                    if landmarks[tip][1] < landmarks[pip][1]:  # Doigt levé
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # Nombre total de doigts levés
                total_fingers = sum(fingers)

    if 0 <= total_fingers <= 5:
        overlay = images[total_fingers]  # Sélectionner l'image correspondante
        if overlay is not None and results.multi_hand_landmarks:
            overlay = cv.resize(overlay, (200, 200))  # Redimensionner
            img[50:250, 50:250] = overlay  # Afficher en haut à gauche
        if overlay is None:
            print("Erreur : Problème lors du chargement de l'image")

    # Affichage du nombre de doigts levés
    cv.putText(img, f'Fingers: {total_fingers}', (300, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv.imshow("Finger Count", img)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()