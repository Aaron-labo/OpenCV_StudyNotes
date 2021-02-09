import cv2
import numpy as np


# 展示函数
def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 数字排序
def sort_contours(contours, method="left-to-right"):
    sequence = False
    i = 0
    if method == "right-to-left" or method == "bottom-to-top":
        sequence = True
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    contourBox = [cv2.boundingRect(cnt) for cnt in contours]
    contours, contourBox = zip(*sorted(zip(contours, contourBox), key=lambda x: x[1][i], reverse=sequence))
    return contours, contourBox

# 等比缩放
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(r * w), height)
    else:
        r = width / float(w)
        dim = (width, int(r * h))
    imageResize = cv2.resize(image, dim, interpolation=inter)
    return imageResize


# 导入模板及模板的预处理(灰度和二值化)
image1 = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\number.png")
imageGray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
imageBianry1 = cv2.threshold(imageGray1, 127, 255, cv2.THRESH_BINARY_INV)[1]

# 找出数字轮廓，并形成最小矩形轮廓
refCnts = cv2.findContours(imageBianry1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
refCnts = sort_contours(refCnts, method="left-to-right")[0]

# 将图片按照最小矩形轮廓，切割数字
digit = {}
for (i, c) in enumerate(refCnts):
    x, y, w, h = cv2.boundingRect(c)
    roi = imageBianry1[y: y + h, x: x + w]
    digit[i] = cv2.resize(roi, (57, 88))


# 初始化卷积核
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 4))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
Kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 引入信用卡图片，并做初步处理(灰度，二值化，礼帽)
image2 = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\credit_card3.png")
image2 = resize(image2, width=300)
imageGray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
imageTophat = cv2.morphologyEx(imageGray2, cv2.MORPH_TOPHAT, rectKernel)

# 使用Sobel进行边缘检测，只需要检测x方向的；
imageSobel = cv2.Sobel(imageTophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
# 线性调节每个像素的数值，是其不大于255
# gradex = cv2.convertScaleAbs(imageSobel)
gradex = np.absolute(imageSobel)
maxVal = np.max(gradex)
minVal = np.min(gradex)
gradex = ((gradex - minVal) / (maxVal - minVal)) * 255
gradex = gradex.astype("uint8")

# 闭运算，将数字横向连接在一起
imageClose = cv2.morphologyEx(gradex, cv2.MORPH_CLOSE, rectKernel)
# 二值化处理，TGHRESH_OTSU表示有opencv来自动决定阈值(所以前面的阈值参数为0)
imageThresh = cv2.threshold(imageClose, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# 在此闭运算，是空隙更少
imageThresh = cv2.morphologyEx(imageThresh, cv2.MORPH_CLOSE, sqKernel)

#计算轮廓,并通过轮廓的长宽比例来删选
refCnts = cv2.findContours(imageThresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
locs = []
for (i, c) in enumerate(refCnts):
    (x, y, w, h) = cv2.boundingRect(c)
    r = w / float(h)
    if 2.5 < r < 4:
        if (40 < w < 55) and (10 < h < 20):
            locs.append((x, y, w, h))
print("len(locs):", len(locs))
#对四个数字区块进行排序
locs = sorted(locs, key=lambda b: b[0])

output = []
image_loc = image2.copy()
for (i, (gx, gy, gw, gh)) in enumerate(locs):
    #切割一组数据
    groupOutput = []
    group = imageGray2[gy - 5: gy + gh + 5, gx - 5: gx + gw + 5]
    group = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #cv_show("group", group)

    #计算每个数字轮廓，并切割
    numContours = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    numRect = sort_contours(numContours, method="left-to-right")[0]
    for c in numRect:
        (x, y, w, h) = cv2.boundingRect(c)
        roi = group[y: y + h, x: x + w]
        roi = cv2.resize(roi, (57, 88))
        #cv_show("roi", roi)
        #将信用卡上的数字与模板依次相对比，计算得分
        scores = []
        for (j, template) in digit.items():
            result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF)
            (_, score, _, _) = cv2.minMaxLoc(result)
            scores.append(score)
        groupOutput.append(str(np.argmax(scores)))

    #画出轮廓
    cv2.rectangle(image_loc, (gx - 5, gy - 5), (gx + gw + 5, gy + gh + 5), (0, 0, 255), 2)
    cv2.putText(image_loc, "".join(groupOutput), (gx, gy - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (13, 158, 153), 2)

    #得出结果
    output.extend(groupOutput)
    output.append(" ")

print("Credit Card #:{}".format("".join(output)))
cv_show("image", image_loc)
