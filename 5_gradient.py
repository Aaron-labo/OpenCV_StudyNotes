import cv2

img = cv2.imread("D:\Personal\Pictures\wallpaper\yellowcar.jpg")
img = cv2.resize(img, None, fx = 0.8, fy = 0.8)
img = cv2.GaussianBlur(img, (3, 3), 1)

#二值化处理
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imgBinary = cv2.threshold(imgGray, 100, 255, cv2.THRESH_BINARY)

#Sobel算子
Sobelx = cv2.Sobel(imgBinary, cv2.CV_64F, 1, 0, ksize=3)
Sobelx = cv2.convertScaleAbs(Sobelx)
Sobely = cv2.Sobel(imgBinary, cv2.CV_64F, 0, 1, ksize=3)
Sobely = cv2.convertScaleAbs(Sobely)
imgSobel = cv2.addWeighted(Sobelx, 1, Sobely, 1, 0)

#Scharr算子
Scharrx = cv2.Scharr(imgBinary, cv2.CV_64F, 1, 0)
Scharrx = cv2.convertScaleAbs(Scharrx)
Scharry = cv2.Scharr(imgBinary, cv2.CV_64F, 0, 1)
Scharry = cv2.convertScaleAbs(Scharry)
imgScharr = cv2.addWeighted(Scharrx, 1, Scharry, 1, 0)

#Laplacian算子
imgLaplacian = cv2.Laplacian(imgBinary, cv2.CV_64F)
imgLaplacian = cv2.convertScaleAbs(imgLaplacian)

cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", imgBinary)
cv2.imshow("Sobel Image", imgSobel)
cv2.imshow("Scharr Image", imgScharr)
cv2.imshow("Laplacian Image", imgLaplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()