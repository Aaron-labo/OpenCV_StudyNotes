#1、使用高斯滤波器，以平滑图像，滤除噪声
#2、计算图像中每个像素点的梯度强度和方向
#3、应用非极大值抑制，以消除边缘检测带来的杂散响应
#4、应用双阈值检测来确定真实的和潜在的边缘
#5、通过抑制孤立的若边缘最终完成边缘检测

import cv2

img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\lena.jpg")
img = cv2.resize(img, None, fx = 0.8, fy = 0.8)

v1 = cv2.Canny(img, 100, 200)
v2 = cv2.Canny(img, 50, 100)

cv2.imshow("Original Image", img)
cv2.imshow("Canny1 Image", v1)
cv2.imshow("Canny2 Image", v2)

cv2.waitKey(0)
cv2.destroyAllWindows()