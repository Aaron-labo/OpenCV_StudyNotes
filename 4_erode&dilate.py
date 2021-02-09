import cv2
import numpy as np

img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\credit_card1.png")
img = cv2.resize(img, None, fx=0.8, fy=0.8)
#二值化处理
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imgBinary = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
#腐蚀、膨胀运算
kernel = np.ones(3, np.uint8)
imgErosion = cv2.erode(imgBinary, kernel, iterations=1)
imgDilate = cv2.dilate(imgErosion, kernel ,iterations=1)
#开闭环运算
imgOpen = cv2.morphologyEx(imgBinary, cv2.MORPH_OPEN, kernel)
imgClose = cv2.morphologyEx(imgBinary, cv2.MORPH_CLOSE, kernel)
#梯度运算
imgGradient = cv2.morphologyEx(imgBinary, cv2.MORPH_GRADIENT, kernel)
#礼帽、黑毛运算
imgTophat = cv2.morphologyEx(imgBinary, cv2.MORPH_TOPHAT, kernel)
imgBlackhat = cv2.morphologyEx(imgBinary, cv2.MORPH_BLACKHAT, kernel)
#输出图像
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Binary Image", imgBinary)
cv2.imshow("Erosion Image", imgErosion)
cv2.imshow("Dilate Image", imgDilate)
cv2.imshow("Open Image", imgOpen)
cv2.imshow("Close Image", imgClose)
cv2.imshow("Gradient Image", imgGradient)
cv2.imshow("Tophat Image", imgTophat)
cv2.imshow("Blackhat Image", imgBlackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()