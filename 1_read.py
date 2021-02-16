import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("F:\\Personal\\Videos\\IDM\\控方证人.ts")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) &0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


