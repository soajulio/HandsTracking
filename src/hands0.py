import cv2 as cv
import mediapipe as mp
cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    print(results.multi_hand_landmarks)
    cv.imshow("Image",img)
    if cv.waitKey(1) == ord('q') :
        break
cap.release()
cv.destroyAllWindows()