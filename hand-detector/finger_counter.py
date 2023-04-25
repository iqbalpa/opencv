import cv2
import mediapipe as mp

# capture video via webcam
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

finger_coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_coord = (4, 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    multi_hand_landmarks = results.multi_hand_landmarks

    if multi_hand_landmarks:
        hand_list = []
        for hand_landmarks in multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            for i, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                hand_list.append((cx, cy))
        for point in hand_list:
            cv2.circle(frame, point, 5, (0, 0, 255), cv2.FILLED)

        # count fingers
        count = 0
        for coord in finger_coord:
            if hand_list[coord[0]][1] < hand_list[coord[1]][1]:
                count += 1
        if hand_list[thumb_coord[0]][1] < hand_list[thumb_coord[1]][1]:
            count += 1
        cv2.putText(
            frame, str(count), (50, 50), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 5
        )

    cv2.imshow("Finger Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
