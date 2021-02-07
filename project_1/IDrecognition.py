# 导入工具包
from imutils import contours
import numpy as np
import argparse
import cv2
import myutils2


# #设置参数
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                 help="path to input image")
# ap.add_argument("-t", "--template", required=True,
#                 help="path to template OCR-A image")
# args = vars(ap.parse_args())

# #指定信用卡类型
# FIRST_NUMBER = {
#     "3": "American Express",
#     "4": "Visa",
#     "5": "MasterCard",
#     "6": "Discover Card"
# }

# 绘制展示
def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 读取一个模板图像
img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\number.png")
cv_show("image", img)
# 灰度图
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化处理
# threshold函数应该返回两个值，第二个值为输入图像，所以用[1]
# threshold操作，超过thresh的部分取最大值，否则取零，然后在对图像进行反转
imgBinary = cv2.threshold(imgGray, 10, 255, cv2.THRESH_BINARY_INV)[1]
cv_show("binary image", imgBinary)

# 计算轮廓，findcontours()函数只接受二值图像作参数
# 计算轮廓是会在原图上进行修改，所以使用copy复制一个新的图像
# cv2.RETR_EXTERNAL表示值绘制外轮廓
# cv2.CHAIN_APPROX_SIMPLE水平保存
imgCnts, hierarchy = cv2.findContours(imgBinary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
cv2.drawContours(img, imgCnts, -1, (0, 0, 255), 3)
cv_show("contours image", img)
print(np.array(imgCnts).shape)
# 比较轮廓的横坐标，对轮廓排列顺序，与其数值相匹配
imgCnts = myutils2.sort_contours(imgCnts, method="left-to-right")[0]
# 新建一个空字典
digits = {}


