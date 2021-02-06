import cv2 as cv

img = cv.imread("D:\Personal\Pictures\wallpaper\lion.jpeg")
img = cv.resize(img, None, fx = 0.8, fy = 0.8)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, imgBinary = cv.threshold(imgGray, 127, 255, cv.THRESH_BINARY)
contours, hierarcy = cv.findContours(imgBinary, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

#绘制轮廓
draw_img = img.copy()
cv.drawContours(draw_img, contours, -1, (0, 0, 255), 1)
#drawContours会修改原图

#轮廓近似
cnt = contours[5]
approx = cv.approxPolyDP(cnt, 0.1, True)
draw_img2 = img.copy()
cv.drawContours(draw_img, [approx], -1, (0, 0, 255), 2)
cv.imshow("Approx Image", draw_img2)

cv.imshow("Original Image", img)
cv.imshow("Binary Image", imgBinary)
cv.imshow("Draw Image", draw_img)

cv.waitKey(0)
cv.destroyAllWindows()