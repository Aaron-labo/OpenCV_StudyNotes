import cv2

img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\credit_card1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
ret3, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret4, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
ret5, thresh5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("image", img)
cv2.imshow("Binary", thresh1)
cv2.imshow("Gray Binary", thresh2)
cv2.imshow("Gray Trunc", thresh3)
cv2.imshow("Gray Tozero", thresh4)
cv2.imshow("Gray Tozero_inv", thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()