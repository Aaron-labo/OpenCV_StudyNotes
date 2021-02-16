import cv2
import numpy as np

img1 = cv2.resize(cv2.imread("picture\\panda.jpeg"), (500, 600))
img2 = cv2.resize(cv2.imread("picture\\cat.jpeg"), (100, 150))

img2Gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
mask = cv2.threshold(img2Gray, 130, 255, cv2.THRESH_BINARY)[1]

mask_inv = cv2.bitwise_not(mask)

rows, cols, channels = img2.shape
roi = img1[350:rows+350, 10:cols+10]

img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_bg = cv2.bitwise_and(img2, img2, mask=mask_inv)
dst = cv2.add(img1_bg, img2_bg)
img1[350:rows+350, 10:cols+10] = dst

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('binary', mask_inv)
cv2.imshow('roi', roi)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_bg', img2_bg)

cv2.waitKey(0)
cv2.destroyAllWindows()