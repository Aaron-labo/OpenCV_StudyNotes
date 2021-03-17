import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing():
    pass

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

image = cv2.imread('E:\\Python\\OpenCV_StudyNotes\\picture\\diffraction3.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (3, 3), 1)

cv2.namedWindow('image')
cv2.createTrackbar('threshold', 'image', 0, 255, nothing)

imgAju = np.ones(image.shape, np.uint8)
row, col = image.shape
M = 255//73
for i in range(row):
    for j in range(col):
        if image[i][j] > 80:
            imgAju[i][j] = 255
        elif image[i][j] < 7:
            imgAju[i][j] = 0
        else:
            imgAju[i][j] = (image[i][j]-7)*M

while True:
    thresh = cv2.getTrackbarPos('threshold', 'image')
    imgBinary1 = cv2.threshold(image, thresh, 256, cv2.THRESH_BINARY)[1]
    imgBinary2 = cv2.threshold(imgAju, thresh, 256, cv2.THRESH_BINARY)[1]

    # imgBinary1 = Bianry(image1)
    # imgBinary2 = Bianry(image)

    # histr1 = cv2.calcHist([image], [0], None, [256], [0, 256])
    # print(histr1.shape)
    # plt.plot(histr1)
    # plt.xlim([0, 256])


    # cv2.imshow('image origenal', image1)
    # cv2.imshow('image', image)
    # plt.show()
    # cv2.imshow('blur1', blur1)
    # cv2.imshow('blur2', blur2)
    # cv2.imshow('blur3', blur3)
    cv2.imshow('imgBinary1', imgBinary1)
    cv2.imshow('imgBinary2', imgBinary2)
    # cv2.imshow('binary', binary)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()