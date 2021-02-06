import cv2 as cv

img = cv.imread("D:\Personal\Pictures\wallpaper\lion.jpeg")

cv.imshow("Original Image", img)

cv.waitKey(0)
cv.destroyAllWindows()