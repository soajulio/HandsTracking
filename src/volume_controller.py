import cv2 as cv
import mediapipe as mp
import math
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands() #uses default parameters
mpDraw = mp.solutions.drawing_utils

#Variables pour le segment entre le pouce et l'index, ainsi que le milieu de ce segment
index_x, index_y = None, None
thumb_x, thumb_y = None, None
centerSeg_x, centerSeg_y = None, None

# Initialisation de PyCaw pour contrôler le volume système
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Récupération des limites de volume
volMin, volMax = volume.GetVolumeRange()[:2]  # min et max en dB

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
                    thumb_x, thumb_y = cx, cy
                    cv.circle(img, (cx,cy), 15, (255,0,255), cv.FILLED)
                if id == 8:
                    index_x, index_y = cx, cy
                    cv.circle(img, (cx,cy), 15, (255,0,255), cv.FILLED)
            
            if thumb_x is not None and index_x is not None:
                distance = math.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)
                print(f"Distance entre le pouce et l'index : {distance:.2f} pixels")

                # Normalisation de la distance pour l'adapter au volume
                vol = np.interp(distance, [20, 350], [volMin, volMax])  # 20 px = min, 200 px = max
                vol_percent = np.interp(distance, [20, 350], [0, 100])  # Conversion en %

                # Appliquer le volume
                volume.SetMasterVolumeLevel(vol, None)

                # Affichage du volume en pourcentage
                cv.putText(img, f'Volume: {int(vol_percent)}%', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

                # Dessiner une barre de volume
                bar_height = int(np.interp(vol_percent, [0, 100], [400, 150]))  # Position verticale
                cv.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)  # Cadre de la barre
                cv.rectangle(img, (50, bar_height), (85, 400), (255, 0, 0), cv.FILLED)  # Remplissage de la barre

                # Dessiner une ligne entre le pouce et l'index
                cv.line(img, (thumb_x, thumb_y), (index_x, index_y), (0, 255, 0), 3)

                centerSeg_x = (thumb_x + index_x) // 2
                centerSeg_y = (thumb_y + index_y) // 2
    
                cv.circle(img, (centerSeg_x, centerSeg_y), 10, (0,0,255), cv.FILLED)
                
    cv.imshow("Image",img)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()