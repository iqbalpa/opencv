import cv2

cap = cv2.VideoCapture(0)


# # gray scaling
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame', frame)
#     cv2.imshow('gray', gray_frame)

#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# rescaling
def rescale_frame(frame, percentage):
    width = int(frame.shape[1] * percentage / 100)
    height = int(frame.shape[0] * percentage / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame50 = rescale_frame(frame, 50)
    cv2.imshow('frame 50%', frame50)
    cv2.imshow('frame 100%', frame)
    frame150 = rescale_frame(frame, 150)
    cv2.imshow('frame 150%', frame150)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()