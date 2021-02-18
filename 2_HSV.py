import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture("F:\\Personal\\Videos\IDM\\sample_03.mp4")

cv2.namedWindow('control', cv2.WINDOW_NORMAL)
cv2.createTrackbar('H low', 'control', 60, 255, nothing)
cv2.createTrackbar('H high', 'control', 180, 255, nothing)
cv2.createTrackbar('S low', 'control', 50, 255, nothing)
cv2.createTrackbar('S high', 'control', 255, 255, nothing)
cv2.createTrackbar('V low', 'control', 46, 255, nothing)
cv2.createTrackbar('V high', 'control', 255, 255, nothing)

while cap.isOpened():
    frame = cap.read()[1]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_low = cv2.getTrackbarPos('H low', 'control')
    h_high = cv2.getTrackbarPos('H high', 'control')
    s_low = cv2.getTrackbarPos('S low', 'control')
    s_high = cv2.getTrackbarPos('S high', 'control')
    v_low = cv2.getTrackbarPos('V low', 'control')
    v_high = cv2.getTrackbarPos('V high', 'control')

    lower_blue = np.array([h_low, s_low, v_low])
    upper_blue = np.array([h_high, s_high, v_high])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('image1', frame)
    cv2.imshow('image2', mask)
    if cv2.waitKey(24) & 0xFF == 27:
        break

cv2.destroyAllWindows()
