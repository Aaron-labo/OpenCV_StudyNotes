import cv2

#图像预处理（灰度及二值化）
img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\res2.jpg")
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
cv2.drawContours(img2, contours, -1, (0, 0, 255), 1)
cnt = contours[0]
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 0, 255), 2)

#输出图像
cv2.imshow('image', img)
cv2.imshow('contours', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()