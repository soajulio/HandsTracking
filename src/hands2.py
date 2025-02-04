import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands() #uses default parameters
mpDraw = mp.solutions.drawing_utils #utilitaire qui permet d’afficher les la
while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS )
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                #on doit transfromer les coords de décimales en pixels...
                h, w, _ = img.shape # on récupère dimX et dimY
                cx, cy = int(lm.x * w ), int(lm.y * h)
                print(id, cx, cy)
                if id == 4:
                    cv.circle(img, (cx,cy), 15, (255,0,255), cv.FILLED)
    cv.imshow("Image",img)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()