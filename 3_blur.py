import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\lena.jpg")
img = cv2.resize(img, None, fx=2, fy=2)
imgBlur = cv2.blur(img, (3, 3))
imgGaussBlur = cv2.GaussianBlur(img, (3, 3), 1)
imgMedBlur = cv2.medianBlur(img, 3)
imgBilateral = cv2.bilateralFilter(img, 9, 75, 75)

# image = [img, imgMedBlur, imgGaussBlur, imgBlur, imgBilateral]
# title = ['original', 'blur', 'guassian', 'median', 'bilateral']
# length = len(image)
# for i in range(length):
#     plt.subplot(length//2+1, 2, i+1)
#     plt.imshow(image[i], cmap=None)
#     plt.title(title[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

cv2.imshow("Original Image", img)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Gaussian Blur Image", imgGaussBlur)
cv2.imshow("Median Blur Image", imgMedBlur)
cv2.imshow("Bilateral Blur Image", imgBilateral)


cv2.waitKey(0)
cv2.destroyAllWindows()