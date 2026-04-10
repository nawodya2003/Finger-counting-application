import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7) 
mpDraw = mp.solutions.drawing_utils

tipIds = [8, 12, 16, 20]

while True:
    success, img = cap.read() 
    if not success:
        break
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    fingers = [] 

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            if len(lmList) != 0:
              
                if lmList[4][1] > lmList[3][1]:
                    fingers.append(1) 
                else:
                    fingers.append(0) 

                for id in range(0, 4):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1) 
                    else:
                        fingers.append(0) 

    if len(fingers) > 0:
        totalFingers = fingers.count(1) 
    else:
        totalFingers = 0

    cv2.putText(img, f'Count: {totalFingers}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)

    cv2.imshow("Smart Finger Counter", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()