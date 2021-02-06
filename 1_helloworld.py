import cv2

img = cv2.imread("D:\Personal\Pictures\wallpaper\lion.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("image", img)
cv2.imshow("image Gray", gray)

cv2.waitKey(0)