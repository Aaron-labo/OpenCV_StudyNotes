import cv2
from skimage import morphology
import numpy as np

img = cv2.imread('E:\\Python\\OpenCV_StudyNotes\\picture\\test_1.png',0)
_,binary = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)

binary[binary==255] = 1
skeleton0 = morphology.skeletonize(binary)
skeleton = skeleton0.astype(np.uint8)*255

imgCopy = skeleton.copy()  # 复制一个新的图像用于绘画轮廓
contours = cv2.findContours(skeleton, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]  # 找到轮廓
cv2.drawContours(imgCopy, contours, -1, (0, 0, 255), 3)  # 绘制轮廓

cv2.imshow('skeleton', imgCopy)
cv2.waitKey(0)
cv2.destroyAllWindows()