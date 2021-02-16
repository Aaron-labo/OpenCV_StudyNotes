import cv2
import numpy as np

img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\credit_card1.png")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows()