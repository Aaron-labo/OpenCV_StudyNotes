import cv2
import numpy as np

img = cv2.imread("D:\Personal\Pictures\wallpaper\lion.jpeg")
img = cv2.resize(img, None, fx = 0.8, fy = 0.8)
imgBlur = cv2.blur(img, (3, 3))
imgGaussBlur = cv2.GaussianBlur(img, (3, 3), 1)
imgMedBlur = cv2.medianBlur(img, 3)

res = np.hstack([img, imgMedBlur, imgGaussBlur, imgBlur])
cv2.imshow("All Image", res)

# cv2.imshow("Original Image", img)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Gaussian Blur Image", imgGaussBlur)
# cv2.imshow("Median Blur Image", imgMedBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()