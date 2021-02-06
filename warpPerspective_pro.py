import os
import numpy as np
import cv2
import tkinter.filedialog
import time
import tkinter.messagebox
import re
import matplotlib.pyplot as plt

dir = time.strftime('%Y-%m-%d')
filenames = 'right'

#上传文件
def get_files():
    global filenames
    filenames = tkinter.filedialog.askopenfilenames(title="选择照片", filetypes=[('图片','jpg'),('图片','png')])
    CN_Pattern = re.compile(u'[\u4E00-\u9FBF]+')
    JP_Pattern = re.compile(u'[\u3040-\u31fe]+')
    if filenames:
        if not os.path.exists(dir):
            os.makedirs(dir)
        CN_Match = CN_Pattern.search(str(filenames))
        JP_Match = JP_Pattern.search(str(filenames))
        if CN_Match:
            filenames = None
            tkinter.messagebox.showinfo('提示','文件路径或文件名不能含有中文，请修改！')
            return
        elif JP_Match:
            filenames = None
            tkinter.messagebox.showinfo('提示','文件路径或文件名不能含有日文，请修改！')
            return

    if not os.path.exists(dir):
        os.makedirs(dir)

def translate(image, x, y):
    #定义平移矩阵
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    #返回转换后的图像
    return shifted

#定义平移函数
def pic_translate():
    if not filenames:
        tkinter.messagebox.showinfo('提示', '请先选择图片才能进行图片平移!')
    if not os.path.exists(dir):
        os.makedirs(dir)
    if filenames:
        for filename in filenames:
            if filenames:
                img = cv2.imread(filename)
                newFile = filename.split('/')[-1]
                name = newFile.split('.')[0]
                filetype = newFile.split('.')[-1]
                #将原图分别做上、下、左、右平移操作
                Downshifted25 = translate(img, 0, 25)
                cv2.imwrite(dir + '/' + name + '_Downshifted25.' + filetype, Downshifted25)
                Upshifted25 = translate(img, 0, -25)
                cv2.imwrite(dir + '/' + name + '_Upshifted25.' + filetype, Upshifted25)
                Rightshifted25 = translate(img, 25, 0)
                cv2.imwrite(dir + '/' + name + '_Rightshifted25.' + filetype, Rightshifted25)
                Leftshifted25 = translate(img, -25, 0)
                cv2.imwrite(dir + '/' + name + '_Leftshifted25.' + filetype, Leftshifted25)

                Downshifted50 = translate(img, 0, 50)
                cv2.imwrite(dir + '/' + name + '_Downshifted50.' + filetype, Downshifted50)
                Upshifted50 = translate(img, 0, -50)
                cv2.imwrite(dir + '/' + name + '_Upshifted50.' + filetype, Upshifted50)
                Rightshifted50 = translate(img, 50, 0)
                cv2.imwrite(dir + '/' + name + '_Rightshifted50.' + filetype, Rightshifted50)
                Leftshifted50 = translate(img, -50, 0)
                cv2.imwrite(dir + '/' + name + '_Leftshifted50.' + filetype, Leftshifted50)

                Downshifted100 = translate(img, 0, 100)
                cv2.imwrite(dir + '/' + name + '_Downshifted100.' + filetype, Downshifted100)
                Upshifted100 = translate(img, 0, -100)
                cv2.imwrite(dir + '/' + name + '_Upshifted100.' + filetype, Upshifted100)
                Rightshifted100 = translate(img, 100, 0)
                cv2.imwrite(dir + '/' + name + '_Rightshifted100.' + filetype, Rightshifted100)
                Leftshifted100 = translate(img, -100, 0)
                cv2.imwrite(dir + '/' + name + '_Leftshifted100.' + filetype, Leftshifted100)

        tkinter.messagebox.showinfo('提示', '平移后的图片已经保存到了' + dir + '中！')

#定义旋转rotate函数
def rotation(image, angle, center = None, scale = 1.0):
    #获取图像尺寸
    (h, w) = image.shape[:2]
    #若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w/2, h/2)
    #执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    retated = cv2.warpAffine(image, M, (w, h))
    #返回旋转后的图像
    return retated

def pic_rotation():
    if not filenames:
        tkinter.messagebox.showinfo('提示', '请先选择图片才能进行图片旋转！')
    if not os.path.exists(dir):
        os.makedirs(dir)
    if filenames:
        for filename in filenames:
            if filenames:
                img = cv2.imread(filename)
                newFile = filename.split('/')[-1]
                name = newFile.split('.')[0]
                filetype = newFile.split('.')[-1]
                # 将原图分别做旋转操作
                Rotated15Degrees = rotation(img, 15)
                cv2.imwrite(dir + '/' + name + '_Rotated15Degrees.' + filetype, Rotated15Degrees)
                Rotated30Degrees = rotation(img, 30)
                cv2.imwrite(dir + '/' + name + '_Rotated03Degrees.' + filetype, Rotated30Degrees)
                Rotated45Degrees = rotation(img, 45)
                cv2.imwrite(dir + '/' + name + '_Rotated45Degrees.' + filetype, Rotated45Degrees)
                Rotated60Degrees = rotation(img, 60)
                cv2.imwrite(dir + '/' + name + '_Rotated60Degrees.' + filetype, Rotated60Degrees)
                Rotated75Degrees = rotation(img, 75)
                cv2.imwrite(dir + '/' + name + '_Rotated75Degrees.' + filetype, Rotated75Degrees)
                Rotated90Degrees = rotation(img, 90)
                cv2.imwrite(dir + '/' + name + '_Rotated90Degrees.' + filetype, Rotated90Degrees)
                Rotated105Degrees = rotation(img, 105)
                cv2.imwrite(dir + '/' + name + '_Rotated105Degrees.' + filetype, Rotated105Degrees)
                Rotated120Degrees = rotation(img, 120)
                cv2.imwrite(dir + '/' + name + '_Rotated120Degrees.' + filetype, Rotated120Degrees)
                Rotated135Degrees = rotation(img, 135)
                cv2.imwrite(dir + '/' + name + '_Rotated135Degrees.' + filetype, Rotated135Degrees)
                Rotated150Degrees = rotation(img, 150)
                cv2.imwrite(dir + '/' + name + '_Rotated150Degrees.' + filetype, Rotated150Degrees)
                Rotated165Degrees = rotation(img, 165)
                cv2.imwrite(dir + '/' + name + '_Rotated165Degrees.' + filetype, Rotated165Degrees)
                Rotated180Degrees = rotation(img, 180)
                cv2.imwrite(dir + '/' + name + '_Rotated180Degrees.' + filetype, Rotated180Degrees)
                Rotated195Degrees = rotation(img, 195)
                cv2.imwrite(dir + '/' + name + '_Rotated195Degrees.' + filetype, Rotated195Degrees)
                Rotated210Degrees = rotation(img, 210)
                cv2.imwrite(dir + '/' + name + '_Rotated210Degrees.' + filetype, Rotated210Degrees)
                Rotated225Degrees = rotation(img, 225)
                cv2.imwrite(dir + '/' + name + '_Rotated225Degrees.' + filetype, Rotated225Degrees)
                Rotated240Degrees = rotation(img, 240)
                cv2.imwrite(dir + '/' + name + '_Rotated240Degrees.' + filetype, Rotated240Degrees)
                Rotated255Degrees = rotation(img, 255)
                cv2.imwrite(dir + '/' + name + '_Rotated255Degrees.' + filetype, Rotated255Degrees)
                Rotated270Degrees = rotation(img, 270)
                cv2.imwrite(dir + '/' + name + '_Rotated270Degrees.' + filetype, Rotated270Degrees)
                Rotated285Degrees = rotation(img, 285)
                cv2.imwrite(dir + '/' + name + '_Rotated285Degrees.' + filetype, Rotated285Degrees)
                Rotated300Degrees = rotation(img, 300)
                cv2.imwrite(dir + '/' + name + '_Rotated300Degrees.' + filetype, Rotated300Degrees)
                Rotated315Degrees = rotation(img, 315)
                cv2.imwrite(dir + '/' + name + '_Rotated315Degrees.' + filetype, Rotated315Degrees)
                Rotated330Degrees = rotation(img, 330)
                cv2.imwrite(dir + '/' + name + '_Rotated330Degrees.' + filetype, Rotated330Degrees)
                Rotated345Degrees = rotation(img, 345)
                cv2.imwrite(dir + '/' + name + '_Rotated345Degrees.' + filetype, Rotated345Degrees)

        tkinter.messagebox.showinfo('提示', '旋转后的图片已经保存到了' + dir + '中！')

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    #初始化缩放比例，并获取图像尺寸
    dim = None
    (h, w) = image.shape[:2]
    #如果宽度和高度均为0，则返回原图
    if width is None and height is None:
        return image
    #宽度是空
    if width is None:
        #则根据高度计算缩放比例
        r = height/float(h)
        dim = (int(w * r), height)
    #高度是空
    if height is None:
        #则根据宽度计算缩放比例
        r = width/float(h)
        dim = (width, int(w * r))
    #缩放图像
    resized = cv2.resize(image, dim, interpolation = inter)
    #返回缩放后图像
    return resized

#创建插值方法数组
methods = [("cv2.INTER_LINEAR", cv2.INTER_LINEAR)]

def pic_resize():
    if not filenames:
        tkinter.messagebox.showinfo('提示', '请先选择图片才能进行图片缩放!')
    if not os.path.exists(dir):
        os.makedirs(dir)
    if filenames:
        for filename in filenames:
            if filename:
                img = cv2.imread(filename)
                newFile = filename.split('/')[-1]
                name = newFile.split('.')[0]
                filetype = newFile.split('.')[-1]
                #将原图做缩放操作
                for(resizeType, method) in methods:
                    Resize2Times = resize(img, width = img.shape[1] * 2, inter = method)
                    cv2.imwrite(dir + '/' + name + '_Resize2Times.' + filetype, Resize2Times)
                    Resize3Times = resize(img, width=img.shape[1] * 3, inter=method)
                    cv2.imwrite(dir + '/' + name + '_Resize3Times.' + filetype, Resize3Times)
                    ResizeAHalf = resize(img, width=img.shape[1] // 2, inter=method)
                    cv2.imwrite(dir + '/' + name + '_ResizeAHalf.' + filetype, ResizeAHalf)
                    ResizeOneThird = resize(img, width=img.shape[1] // 3, inter=method)
                    cv2.imwrite(dir + '/' + name + '_ResizeOneThird.' + filetype, ResizeOneThird)

        tkinter.messagebox.showinfo('提示', '缩放后的图片已经保存到了' + dir + '中！')

def pic_flip():
    if not filenames:
        tkinter.messagebox.showinfo('提示', '请先选择图片才能进行图片翻转!')
    if not os.path.exists(dir):
        os.makedirs(dir)
    if filenames:
        for filename in filenames:
            if filename:
                img = cv2.imread(filename)
                newFile = filename.split('/')[-1]
                name = newFile.split('.')[0]
                filetype = newFile.split('.')[-1]
                #将原图分别做翻转操作
                Horizentallyflipped = cv2.flip(img, 1)
                cv2.imwrite(dir + '/' + name + '_Horizentallyflipped.' + filetype, Horizentallyflipped)
                Verticallyflipped = cv2.flip(img, 0)
                cv2.imwrite(dir + '/' + name + '_Verticallyflipped.' + filetype, Verticallyflipped)
                HorizentallyAndvertically = cv2.flip(img, -1)
                cv2.imwrite(dir + '/' + name + '_HorizentallyAndvertically.' + filetype, HorizentallyAndvertically)

        tkinter.messagebox.showinfo('提示', '翻转后的图片已经保存到了' + dir + '中！')

def mouse(event, x, y, flags, param):
    image = param[0]
    pts1 = param[1]
    pts2 = param[2]
    if event == cv2.EVENT_LBUTTONDOWN:
        pts1.append([x, y])
        xy = "%d, %d" %(x, y)
        cv2.circle(image, (x, y), 4, (0, 255, 255), thickness = -1)
        cv2.putText(image, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 255, 255), thickness = 2)
        cv2.imshow("image", image)
    if event == cv2.EVENT_RBUTTONDOWN:
        pts2.append([x, y])
        xy = "%d, %d" % (x, y)
        cv2.circle(image, (x, y), 4, (255, 0, 255), thickness = -1)
        cv2.putText(image, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255, 0, 255), thickness = 2)
        cv2.imshow("image", image)

def pic_perspective():
    if filenames:
        for filename in filenames:
            if filename:
                print("file:", filename)
                image = cv2.imread(filename)
    #原图中卡片的四个角点
    cv2.namedWindow("image")

    tips_str = "Left to right, top to bottom\nLeft click the original image\nRight click the target"
    y0, dy = 20, 20
    for i, line in enumerate(tips_str.split('\n')):
        y = y0 + i*dy
        cv2.putText(image, line, (2, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)

    cv2.imshow("image", image)
    pts1 = []
    pts2 = []
    cv2.setMouseCallback("image", mouse ,param = (image, pts1, pts2))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("pts1:", pts1)
    pts1 = np.float32(pts1[:4])
    print("pts2:", pts2)
    pts2 = np.float32(pts2[:4])

    assert len(pts1) == 4

    #生成透视变换矩阵
    M = cv2.getPerspectiveTransform(pts1, pts2)
    #进行透视变换
    dst = cv2.warpPerspective(image, M, (image.shape[2], image.shape[0]))
    cv2.imwrite('dst.jpg', dst)
    #matplotlib默认以RGB通道显示，所以需要用[:,:,::-1]反转一下
    plt.subplot(121), plt.imshow(image[:, :, ::-1]), plt.title('imput')
    plt.subplot(122), plt.imshow(dst[:, :, ::-1]), plt.title('output')
    plt.show()

    #tkinter.messagebox.showinfo('提示','透视变换的图片处理完毕！')
    return dst

root = tkinter.Tk()
root.title('批量处理')
button = tkinter.Button(root, text = "上传图片", command = get_files, width = 20, height = 2)
button.grid(row = 0, column = 0, padx = 180, pady = 0)
button1 = tkinter.Button(root, text = "图片平移", command = pic_translate, width = 20, height = 2)
button1.grid(row = 1, column = 0, padx = 1, pady = 1)
button2 = tkinter.Button(root, text = "图片旋转", command = pic_rotation, width = 20, height = 2)
button2.grid(row = 2, column = 0, padx = 1, pady = 1)
button3 = tkinter.Button(root, text = "图片缩放", command = pic_resize, width = 20, height = 2)
button3.grid(row = 3, column = 0, padx = 1, pady = 1)
button4 = tkinter.Button(root, text = "图片翻转", command = pic_flip, width = 20, height = 2)
button4.grid(row = 4, column = 0, padx = 1, pady = 1)
button5 = tkinter.Button(root, text = "透视变换", command = pic_perspective, width = 20, height = 2)
button5.grid(row = 5, column = 0, padx = 1, pady = 1)

root.geometry('500x400+600+300')
root.mainloop()