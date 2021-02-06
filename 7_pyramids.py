import cv2 as cv

img = cv.imread("D:\Personal\Pictures\wallpaper\woman.jpg")
img = cv.resize(img, None, fx = 0.2, fy = 0.2)

imgUp = cv.pyrUp(img)
imgDown = cv.pyrDown(imgUp)
differ = img - imgDown

cv.imshow("Origenal Image", img)
cv.imshow("Up Image", imgUp)
cv.imshow("Down Image", imgDown)
cv.imshow("Differ Image", differ)

cv.waitKey(0)
cv.destroyAllWindows()