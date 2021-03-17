# 导入工具包
import numpy as np
import cv2
import myutils2

# 绘制展示
def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 读取一个模板图像
img = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\number.png")
# 灰度图
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化处理
# threshold函数应该返回两个值，第二个值为输入图像，所以用[1]
# threshold操作，超过thresh的部分取最大值，否则取零，然后在对图像进行反转
imgBinary = cv2.threshold(imgGray, 10, 255, cv2.THRESH_BINARY_INV)[1]

# 计算轮廓，findcontours()函数只接受二值图像作参数
# 计算轮廓是会在原图上进行修改，所以使用copy复制一个新的图像
# cv2.RETR_EXTERNAL表示值绘制外轮廓
# cv2.CHAIN_APPROX_SIMPLE水平保存
refCnts, hierarchy = cv2.findContours(imgBinary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
cv2.drawContours(img, refCnts, -1, (0, 0, 255), 3)
# 比较轮廓的横坐标，对轮廓排列顺序，与其数值相匹配
refCnts = myutils2.sort_contours(refCnts, method="left-to-right")[0]

# 新建一个空字典
digits = {}
# 循环遍历每一个轮廓
# i为下标，c为i对应的图像
for (i, c) in enumerate(refCnts):
    (x, y, w, h) = cv2.boundingRect(c)
    #用外接矩形返回的值,切割图像，制成每个数字的模板
    roi = imgBinary[y:y+h, x:x+w]
    #因原模板太小，用resize调整大小
    roi = cv2.resize(roi, (57, 88))
    #每个数字对应一个模板,存入字典
    digits[i] = roi



# 处理输入图像
# 初始化卷积核
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 3))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 读取输入图像，预处理
image = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\credit_card1.png")
image = myutils2.resize(image, width=300)
cv2.imshow('image', image)
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 礼帽操作，突出明亮的区域，滤除部分干扰信息
imageTophat = cv2.morphologyEx(imageGray, cv2.MORPH_TOPHAT, rectKernel)
#ksize=-1,则使用系统默认的3*3的核
imageSobel = cv2.Sobel(imageTophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)

gradx = np.absolute(imageSobel)
(minVal, maxVal) = (np.min(gradx), np.max(gradx))
gradx = (255 * ((gradx - minVal) / (maxVal - minVal)))
gradx = gradx.astype("uint8")
print("gradx.shape", np.array(gradx).shape)
#通过闭操作，将数字连载一起
imageClose = cv2.morphologyEx(gradx, cv2.MORPH_CLOSE, rectKernel)
#THRESH_OTSU会自动寻找合适的阈值，合适的峰值，让OPopencv自动判断阈值，所以第二个参数是0
imageThresh = cv2.threshold(imageClose, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#在进行依次闭操作
imageClose = cv2.morphologyEx(imageThresh, cv2.MORPH_CLOSE, sqKernel)

#计算轮廓
threshCnts, hier = cv2.findContours(imageClose.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cur_img = image.copy()
cv2.drawContours(cur_img, threshCnts, -1, (0, 0, 255), 3)
# cv2.imshow('contours', cur_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

locs = []
for (i, c) in enumerate(threshCnts):
    # 计算矩形
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)
    #选择适当的区域，根据实际任务来，这里基本都是四个数字一组
    if 2.5 < ar < 4.0:
        if(40 < w < 55) and (10 < h < 20):
            #符合的留下来
            locs.append((x, y, w, h))
print('locs', len(locs))
# 将符合的轮廓从左到右排序
locs = sorted(locs, key=lambda x: x[0])
output = []

#遍历每一个轮廓的数字
for(i, (gX, gY, gW, gH)) in enumerate(locs):
    groupOutput = []
    group = imageGray[gY - 5:gY + gH + 5, gX - 5:gX + gW + 5]
    groupThresh = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv_show("groupthresh", groupThresh)
    #计算每一组的轮廓
    digitCnts, hierarchy = cv2.findContours(groupThresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #对每一组轮廓进行排序
    digitCnts = myutils2.sort_contours(digitCnts, method="left-to right")[0]

    for c in digitCnts:
        # 找到当前数值的轮廓，resize成合适的大小
        (x, y, w, h) = cv2.boundingRect(c)
        roi = groupThresh[y: y + h, x: x + w]
        roi = cv2.resize(roi, (57, 88))
        cv_show("roi", roi)

        #计算匹配得分
        scores = []
        #在模板中计算每一个得分
        for(digit, digitROI) in digits.items():
            result = cv2.matchTemplate(roi, digitROI, cv2.TM_CCORR)
            (_, score, _, _) = cv2.minMaxLoc(result)
            scores.append(score)
        groupOutput.append(str(np.argmax(scores)))

    #画出轮廓
    image_loc = image.copy()
    cv2.rectangle(image, (gX -5, gY -5), (gX + gW + 5, gY + gH + 5),
                  (0, 0, 255), 2)
    cv2.putText(image, "".join(groupOutput), (gX, gY - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (13, 158, 153), 2)

    #得出结果
    output.extend(groupOutput)

#打印结果
print("Credit Card Type:{}".format(output[0]))
print("Credit Card #:{}".format("".join(output)))
