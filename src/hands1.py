import cv2 as cv
import mediapipe as mp
cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
#utilitaire qui permet d’afficher les landmarks
mpDraw = mp.solutions.drawing_utils
while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # affiche les points uniquement
            #pDraw.draw_landmarks(img, handLms)
            # affiche les points et les arêtes entre
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS )
    cv.imshow("Image",img)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()