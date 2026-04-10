import cv2
import mediapipe as mp

# 1. කැමරාව ඔන් කිරීම 🎥
cap = cv2.VideoCapture(0)

# 2. අත හඳුනාගන්න MediaPipe සූදානම් කිරීම ✋
mpHands = mp.solutions.hands
# මෙතන max_num_hands=1 දුන්නම එක අතක් විතරක් අල්ලගන්නවා, ඒ නිසා හරියටම 5 ට සීමා වෙනවා.
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7) 
mpDraw = mp.solutions.drawing_utils

# 3. අනිත් ඇඟිලි 4 හි මුදුනේ තියෙන ලක්ෂ්‍ය වල අංක (දබර, මැද, වෙද, සුලැඟිල්ල)
tipIds = [8, 12, 16, 20]

while True:
    success, img = cap.read() # කැමරාවෙන් රූපයක් ගන්නවා
    if not success:
        break

    # රූපය හරවමු (කණ්ණාඩියක් වගේ ලස්සනට පේන්න) 🪞
    img = cv2.flip(img, 1)

    # MediaPipe වලට තේරෙන්නේ RGB පාට, ඒ නිසා පාට වෙනස් කරනවා
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    fingers = [] # දිගෑරලා තියෙන ඇඟිලි ගාන එකතු කරන්න හිස් ලැයිස්තුවක්

    # අතක් අඳුරගත්තොත් විතරක් මේ ටික වෙනවා ✅
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # අතේ තිත් ටිකයි ඉරි ටිකයි රූපයේ අඳින්න ✍️
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            lmList = [] # අතේ හැම ලක්ෂ්‍යයකම X,Y ඛණ්ඩාංක (තැන) ගබඩා කරන්න
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            if len(lmList) != 0:
                # 1. මාපටැඟිල්ල (Thumb) වෙනම චෙක් කරනවා 👍
                # මාපටැඟිල්ලේ මුදුන ඊට පහළින් තියෙන හන්දියට වඩා එළියෙන් තියෙනවද බලනවා
                if lmList[4][1] > lmList[3][1]:
                    fingers.append(1) # ඇඟිල්ල දිගෑරලා
                else:
                    fingers.append(0) # ඇඟිල්ල නවල

                # 2. අනිත් ඇඟිලි 4 චෙක් කරනවා ✌️
                for id in range(0, 4):
                    # ඇඟිල්ලේ මුදුන (Tip) ඊට පහළින් තියෙන හන්දියට වඩා උඩින්ද තියෙන්නේ කියලා බලනවා
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1) # ඇඟිල්ල දිගෑරලා
                    else:
                        fingers.append(0) # ඇඟිල්ල නවල

    # ඇඟිලි ගාන ගණනය කිරීම 🧮
    if len(fingers) > 0:
        totalFingers = fingers.count(1) # '1' ඒව කීයද කියල බලනවා
    else:
        totalFingers = 0 # අතක් පේන්න නැත්නම් කෙලින්ම ගාන බිංදුවයි ⭕

    # තිරයේ ගාන ලස්සනට පෙන්නන්න 🖥️
    cv2.putText(img, f'Count: {totalFingers}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)

    # අපිට පේන්න වින්ඩෝ එකක් ඕපන් කිරීම 🖼️
    cv2.imshow("Smart Finger Counter", img)

    # 'q' අකුර එබුවාම වැඩසටහන නවතින්න 🛑
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# වැඩසටහන ඉවර වුණාම කැමරාව නිදහස් කරන්න
cap.release()
cv2.destroyAllWindows()