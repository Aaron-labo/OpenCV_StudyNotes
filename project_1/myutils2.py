import cv2


def sort_contours(contours, method="left-to-right"):
    sequence = False
    i = 0

    if method == "right-to-right" or method == "bottom-to-top":
        sequence = True
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(cnt) for cnt in contours]  # 用一个最小的矩形，把找到的形状包起来,具有四个参数(x,y,h,w)
    (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b: b[1][i], reverse=sequence))
    return contours, boundingBoxes
