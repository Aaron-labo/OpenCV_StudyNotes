# import cv2
# import numpy as np
#
# drawing = False
# mode = True
# ix, iy = -1, -1
#
# def nothing(x):
#     pass
#
# def draw(event, x, y, flags, param):
#     global drawing, mode, ix, iy
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
#             else:
#                 cv2.circle(img, (x, y), 5, (b, g, r), -1)
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv2.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
#         else:
#             cv2.circle(img, (x, y), 5, (b, g, r), -1)
#
#
#
# img = np.zeros((300, 512, 3), np.uint8)
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
# cv2.createTrackbar('0 : OFF \n1:ON', 'image', 0, 1, nothing)
#
# while(True):
#     cv2.imshow('image', img)
#
#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')
#     s = cv2.getTrackbarPos('0 : OFF \n1:ON', 'image')
#
#     if s == 1:
#         cv2.setMouseCallback('image', draw)
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
# cv2.destroyAllWindows()



import cv2
import numpy as np

def nothing(x):
    pass

drawing = False
mode = True
ix, iy = -1, -1

def draw(event, x, y, flags, param):
    global drawing, mode, ix, iy

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')

    color = (b, g, r)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)
            else:
                cv2.circle(img, (x, y), 5, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), color, -1)
        else:
            cv2.circle(img, (x, y), 5, color, -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('OFF or ON', 'image', 0, 1, nothing)

while(True):
    cv2.imshow('image', img)
    s = cv2.getTrackbarPos('OFF or ON', 'image')
    if s == 1:
        cv2.setMouseCallback('image', draw)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()