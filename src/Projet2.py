import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)  # Miroir pour un affichage intuitif
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # Récupération des coordonnées des doigts
            landmarks = {}
            h, w, _ = img.shape

            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks[id] = (cx, cy)

            if len(landmarks) >= 21:
                fingers = []

                # Pouce : Comparaison en X
                if landmarks[4][0] > landmarks[2][0]:  # Main droite
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Autres doigts : Comparaison en Y
                for tip, pip in [(8, 6), (12, 10), (16, 14), (20, 18)]:
                    if landmarks[tip][1] < landmarks[pip][1]:  # Doigt levé
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # Nombre de doigts levés
                total_fingers = sum(fingers)
                cv.putText(img, f'Fingers: {total_fingers}', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv.imshow("Finger Count", img)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()