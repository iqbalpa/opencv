import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    # draw rectangle around faces
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))
    # detect eyes
    eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    # draw rectangle around eyes
    for x, y, w, h in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0))
    # show frame
    cv2.imshow("frame", frame)
    # press q to quit
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
