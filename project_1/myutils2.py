import cv2


def sort_contours(contours, method="left-to-right"):
    sequence = False
    i = 0

    if method == "right-to-right" or method == "bottom-to-top":
        sequence = True
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(cnt) for cnt in contours]  # 用一个最小的矩形，把找到的形状包起来,具有四个参数(x,y,h,w)
    contours, boundingBoxes = zip(*sorted(zip(contours, boundingBoxes), key=lambda b: b[1][i], reverse=sequence))
    return contours, boundingBoxes

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
    resize = cv2.resize(image, dim, interpolation=inter)
    return resize