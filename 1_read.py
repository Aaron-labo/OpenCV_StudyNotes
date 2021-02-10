import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()
    frame = frame[:, ::-1, :]
    cv2.imshow("cap", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
