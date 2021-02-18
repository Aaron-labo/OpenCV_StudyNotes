import cv2
import numpy as np
import matplotlib.pyplot as plt

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

title = ['img1', 'img2', 'mask_inv', 'roi', 'img_bg', 'img2_bg']
image = [img1, img2, mask_inv, roi, img1_bg, img2_bg]

for i in range(len(image)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(image[i])
    plt.title(title[i])

plt.show()