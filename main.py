import cv2
import numpy as np

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


# # rescaling
# def rescale_frame(frame, percentage):
#     width = int(frame.shape[1] * percentage / 100)
#     height = int(frame.shape[0] * percentage / 100)
#     dim = (width, height)
#     return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame50 = rescale_frame(frame, 50)
#     cv2.imshow('frame 50%', frame50)
#     cv2.imshow('frame 100%', frame)
#     frame150 = rescale_frame(frame, 150)
#     cv2.imshow('frame 150%', frame150)

#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# # changing resolution
# def make_1080p():
#     cap.set(3, 1920)
#     cap.set(4, 1080)
# def make_720p():
#     cap.set(3, 1280)
#     cap.set(4, 720)
# def make_480p():
#     cap.set(3, 640)
#     cap.set(4, 480)
# def change_resolution(width, height):
#     cap.set(3, width)
#     cap.set(4, height)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     make_1080p()
#     cv2.imshow('frame', frame)

#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# smoothing and blurring
while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color1 = np.array([0, 0, 0])
    color2 = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, color1, color2)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15,15), np.float32) / 225
    smoothed = cv2.filter2D(result, -1, kernel)

    gaussian_blur = cv2.GaussianBlur(result, (15, 15), 0)
    median_blur = cv2.medianBlur(result, 15)
    bilateral_blur = cv2.bilateralFilter(result, 15, 75, 75)

    cv2.imshow('frame', frame)

    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow('smoothed', smoothed)

    cv2.imshow('gaussian_blur', gaussian_blur)
    cv2.imshow('median_blur', median_blur)
    cv2.imshow('bilateral_blur', bilateral_blur)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()