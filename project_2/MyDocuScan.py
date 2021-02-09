import cv2
import numpy as np
import  pytesseract
from PIL import Image

#展示函数
def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#尺度放缩
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=inter)

#透视变换
def four_point_transform(image, pts):
    rect = np.float32(pts)
    (tr, tl, bl, br) = rect

    widthTop = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
    widthBottom = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
    widthMax = int(max(widthTop, widthBottom))

    heightRight = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    heightLeft = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    heightMax = int(max(heightRight, heightLeft))

    dst = np.array([
        [widthMax - 1, 0],
        [0, 0],
        [0, heightMax - 1],
        [widthMax - 1, heightMax - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    image = cv2.warpPerspective(image, M, (widthMax, heightMax))
    return image

#导入图片，并做预处理(尺度变换、灰度、高斯模糊、边缘检测)
image = cv2.imread("E:\\Python\\OpenCV_StudyNotes\\picture\\bill.jpg")
imageCopy = image.copy()
ratio = image.shape[0] / 500.0
image = resize(image, height=500)
cv2.imshow("original image", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(gray, (5, 5), 0)
imageCanny = cv2.Canny(imageBlur, 135, 200)

#外轮廓检测
contours = cv2.findContours(imageCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
points = []
for c in contours:
    imageLen = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * imageLen, True)
    if len(approx) == 4:
        points = approx
        break

#透视变换
warp = four_point_transform(imageCopy, points.reshape(4, 2) * ratio)
#对透视变换后的图形做预处理
warp = cv2.cvtColor(warp, cv2.COLOR_RGB2GRAY)
warp = cv2.threshold(warp, 135, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("E:\\Python\\OpenCV_StudyNotes\\picture\\bill_bianry_2.jpg", warp)

#识别文本
imageText = Image.open("E:\\Python\\OpenCV_StudyNotes\\picture\\bill_bianry_2.jpg")
text = pytesseract.image_to_string(imageText)
print(text)


warp = resize(warp, height=500)
cv_show("image", warp)