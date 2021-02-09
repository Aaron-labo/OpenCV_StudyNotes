import numpy as np
import cv2
import pytesseract
from PIL import Image

#输出函数
def cv_show(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#尺度变换
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None:
        r = height / float(h)
        dim = (int(r * w), height)
    else:
        r = width / float(w)
        dim = (width, int(r * h))
    return cv2.resize(image, dim, interpolation=inter)

#透视变换
def four_point_transform(image, pts):
    #获取输入左边点
    rect = np.float32(pts)
    (tl, bl, br, tr) = rect

    #print("topright:{}\ntopleft:{}\nbottomleft:{}\nbottomright:{}".format(tr, tl, bl, br))
    widthTop = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
    widthBottom = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
    maxWidth = int(max(widthTop, widthBottom))

    heightLeft = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    heightRight = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    maxHeight = int(max(heightLeft, heightRight))
    #变换后对应的坐标位置
    dst = np.array([
        [0, 0],
        [0, maxHeight - 1],
        [maxWidth - 1, maxHeight - 1],
        [maxWidth - 1, 0]
    ], dtype="float32")

    #计算变换矩阵,并输出
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped


#导入待处理的发票图片
image = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\page.jpg")
#图像大小做变换前，先计算出变换比例
ratio = image.shape[0] / 500.0
imageCopy = image.copy()
#变换大小
image = resize(image, height=500)
cv2.imshow("original image", image)

#预处理(灰度，高斯模糊，边缘检测)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(gray, (5, 5), 0)
imageCanny = cv2.Canny(imageBlur, 75, 200)

#轮廓检测
contours = cv2.findContours(imageCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

#遍历每一个轮廓
points = []
for c in cnts:
    #计算轮廓周长,True表示闭合轮廓
    peri = cv2.arcLength(c, True)
    #轮廓近似，用长度的2%作为精度
    approx = cv2.approxPolyDP(c, 0.02*peri, True)

    if len(approx) == 4:
        points = approx
        break
#print(points)
#展示结果
cv2.drawContours(image, [points], -1, (0, 255, 0), 2)
#cv2.imshow("contours", image)

#透视变换
warped = four_point_transform(imageCopy, points.reshape(4, 2) * ratio)


#二值化处理
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
warped = cv2.threshold(warped, 135, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("E:\\Python\\OpenCV_StudyNotes\\picture\\page_bianry.jpg", warped)

#读取文本
imageText = Image.open("E:\\Python\\OpenCV_StudyNotes\\picture\\page_bianry.jpg")
text = pytesseract.image_to_string(imageText)
print(text)


warped = resize(warped, height=1000)
cv_show("image", warped)
