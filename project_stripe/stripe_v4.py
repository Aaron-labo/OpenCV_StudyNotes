import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing():
    pass

# 滤波图像相减函数
def Bianry(img):
    blur1 = cv2.blur(img, (3, 3))
    blur2 = cv2.blur(blur1, (3, 3))
    blur3 = cv2.blur(blur2, (3, 3))

    imgBinary = np.zeros(blur1.shape)
    w, h = img.shape
    for i in range(w):
        for j in range(h):
            if (int(blur3[i][j]) - int(blur1[i][j])) < 0:
                imgBinary[i][j] = 0
            elif (int(blur3[i][j]) - int(blur1[i][j])) > 0:
                imgBinary[i][j] = 255
    return imgBinary

# 插入图像并预处理
img = cv2.imread('E:\\Python\\OpenCV_StudyNotes\\picture\\testout.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 高斯模糊
image = cv2.GaussianBlur(img, (3, 3), 1)

# 灰度图拉伸
M = int(255/73)
imgAju = (image-7)*M
# for i in range(row):
#     for j in range(col):
#         if image[i][j] > 80:
#             imgAju[i][j] = 255
#         elif image[i][j] < 7:
#             imgAju[i][j] = 0
#         else:
#             imgAju[i][j] = (image[i][j]-7)*M

# 二值化
imgBinary2 = cv2.threshold(imgAju, 43, 256, cv2.THRESH_BINARY)[1]

kernel = np.ones(9, np.uint8)
imgOpen = cv2.morphologyEx(imgBinary2, cv2.MORPH_OPEN, kernel)
imgOpen = cv2.morphologyEx(imgOpen, cv2.MORPH_OPEN, kernel)
#imgErosion = cv2.erode(imgBinary2, kernel, iterations=1)

imgCopy = image.copy()  # 复制一个新的图像用于绘画轮廓
imgCopy = cv2.cvtColor(imgCopy, cv2.COLOR_GRAY2BGR)
imgCopy1 = imgCopy.copy()
contours = cv2.findContours(imgOpen, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]  # 找到轮廓

# 我们只需要中间的原型轮廓，通过每个轮廓的面积筛选除去半圆的小轮廓
locs = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 5000:
        locs.append(cnt)
cv2.drawContours(imgCopy1, locs, -1, (0, 0, 255), 3)  # 绘制轮廓
cv2.imshow('copy', imgCopy1)

# 圆形拟合
row, col = image.shape
core = (col/2, row/2)
sum_center = [0,0]  # 用于存放半径和，便于以后取半径的平均值
list_radius = []  # 用于存放所有轮廓的半径
ave_radius = []
num_circle = 0

for cnt in locs:
    (x, y), radius = cv2.minEnclosingCircle(cnt)  # 得到拟合圆的半径和圆心
    center = (int(x), int(y))  # 将半径和圆心转化成整数
    if abs(int(x) - core[0]) > 100 or radius > 320:
        continue
    num_circle += 1
    sum_center[0] += int(x)
    sum_center[1] += int(y)
    radius = int(radius)
    list_radius.append(radius)
    cv2.circle(imgCopy, center, radius, (0, 255, 0), 2)
    # print(radius)
    # cv2.imshow('test', imgCopy)
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()


for i in range(0,len(list_radius),2) :
    if i == len(list_radius)-1 and len(list_radius)%2 ==1:
        ave_radius.append((list_radius[i]))
    else:
        ave_radius.append(int((list_radius[i]+list_radius[i+1])/2))

ave_center = (int(sum_center[0]/num_circle),int(sum_center[1]/num_circle))  # 计算圆心的平均值

for i in range(len(ave_radius)):

    cv2.circle(imgCopy, ave_center, ave_radius[i], (0, 0, 255), 2)


#图像输出
cv2.imshow('imgBinary2', imgBinary2)
cv2.imshow('imgOpen', imgOpen)
cv2.imshow('contours', imgCopy)
#cv2.imwrite("E:\\Python\\OpenCV_StudyNotes\\picture\\test_1.png", imgBinary2)
cv2.waitKey(0)
cv2.destroyAllWindows()