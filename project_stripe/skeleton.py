import cv2                                        # pass  太慢了
import numpy as np

im = cv2.imread('E:\\Python\\OpenCV_StudyNotes\\picture\\test_1.png', cv2.IMREAD_GRAYSCALE)
thresh, im = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('binary.png', im)  # 控制背景为黑色
dst = im.copy()

num_erode = 0

while (True):
    if np.sum(dst) == 0:
        break
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dst = cv2.erode(dst, kernel)
    num_erode = num_erode + 1

skeleton = np.zeros(dst.shape, np.uint8)

for x in range(num_erode):
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dst = cv2.erode(im, kernel, None, None, x)
    open_dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)
    result = dst - open_dst
    skeleton = skeleton + result
    cv2.waitKey(1000)

cv2.imshow('result', skeleton)

cv2.waitKey(0)
cv2.destroyAllWindows()