import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\diffraction2.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gary = cv2.blur(gray, (3, 3))
ret1, thresh1 = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones(3, np.uint8)
imgClose = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
imgOpen = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)

# ret2, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# ret3, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
# ret4, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
# ret5, thresh5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

# title = ['image', 'binary', 'gray binary', 'trunc', 'tozero', 'tozero_inv']
# image = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in range(len(image)):
#     plt.subplot(3, 2, i+1)
#     plt.imshow(image[i])
#     plt.title(title[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

cv2.imshow("image", img)
cv2.imshow("Binary", thresh1)
cv2.imshow('imgClose', imgClose)
cv2.imshow('imgOpen', imgOpen)
# cv2.imshow("Gray Binary", thresh2)
# cv2.imshow("Gray Trunc", thresh3)
# cv2.imshow("Gray Tozero", thresh4)
# cv2.imshow("Gray Tozero_inv", thresh5)
#
cv2.waitKey(0)
cv2.destroyAllWindows()