import cv2
import numpy as np
import time
import math
from adafruit_servokit import ServoKit
#初始化PCA9685模块
kit = ServoKit(channels=16)

angle_down = 90
angle_up = 50
#设置舵机初始位置
kit.servo[0].angle = angle_down # 水平方向舵机
kit.servo[1].angle = angle_up # 垂直方向舵机

#定义舵机移动函数
def move_servo(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(0.1) # 等待舵机稳定

def left():
    global angle_down
    # 向左移动>=10个像素
    angle_down += 1
    move_servo(0, angle_down)
def right():
    global angle_down
    angle_down -= 1
    # 向右移动>=10个像素
    move_servo(0, angle_down)
def up():
    global angle_up
    angle_up -= 1
    # 向上移动>=10个像素
    move_servo(1, angle_up)
def down():
    global angle_up
    angle_up += 1
    # 向下移动>=10个像素
    move_servo(1, angle_up)

def PID(x, y, xc, yc):
    """
    :param (x, y, xc, yc)分别代表激光的xy轴和中点xy的位置
    :return None
    """
    kp = 0.5
    dx = xc - x
    if dx > 0:
        for i in range(int(abs(dx) * kp)):
            left(x)
    else:
        for i in range(int(abs(dx) * kp)):
            right(x)

def findLaser(crop):
    """
    找到图片中点绿色激光点与红色激光点并定位中心
    :param crop: 需要处理点图片
    :return: 绿色激光点中心（x1, y1）;红色激光点中心（x2, y2)
    """
    cX1, cY1, cX2, cY2 = None, None, None, None
    greenLaser = 'green'
    redLaser = 'red'
    # 色系下限上限表
    color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
                  'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
                  }

    # 高斯滤波
    blurred = cv2.GaussianBlur(crop, (11, 11), 0)
    # cv2.imshow('blurred', blurred)
    # 创建运算核
    kernel = np.ones((1, 1), np.uint8)
    # 开运算
    opening = cv2.morphologyEx(blurred, cv2.MORPH_OPEN, kernel)
    # 二值化处理
    thresh = cv2.threshold(opening, 230, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('thresh', thresh)

    hsv = cv2.cvtColor(thresh, cv2.COLOR_BGR2HSV)  # 转化成HSV图像
    # 颜色二值化筛选处理
    inRange_hsv_green = cv2.inRange(hsv, color_dist[greenLaser]['Lower'], color_dist[greenLaser]['Upper'])
    inRange_hsv_red = cv2.inRange(hsv, color_dist[redLaser]['Lower'], color_dist[redLaser]['Upper'])

    # 找绿色激光点
    try:
        cnts1 = cv2.findContours(inRange_hsv_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        c1 = max(cnts1, key=cv2.contourArea)
        M = cv2.moments(c1)
        cX1 = int(M["m10"] / M["m00"])
        cY1 = int(M["m01"] / M["m00"])
        cv2.circle(crop, (cX1, cY1), 3, (0, 255, 0), -1)
        rect = cv2.minAreaRect(c1)
        box = cv2.boxPoints(rect)
        # cv2.drawContours(crop, [np.int0(box)], -1, (0, 255, 0), 2)
    except:
        print('没有找到绿色的激光')

    # # 找红色激光点
    # try:
    #     cnts2 = cv2.findContours(inRange_hsv_red.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    #     c2 = max(cnts2, key=cv2.contourArea)
    #     M = cv2.moments(c2)
    #     cX2 = int(M["m10"] / M["m00"])
    #     cY2 = int(M["m01"] / M["m00"])
    #     cv2.circle(crop, (cX2, cY2), 3, (0, 0, 255), -1)
    #     rect = cv2.minAreaRect(c2)
    #     box = cv2.boxPoints(rect)
    # #         cv2.drawContours(crop, [np.int0(box)], -1, (0, 0, 255), 2)
    # except:
    #     print('没有找到红色的激光')
    return cX1, cY1, cX2, cY2


def draw_fit_line(dire, type):
    """
    :param dire: 传入需要拟合的含有白色直线的图像
    :return: 传出直线一般式参数a，b，c
    """
    dic = {'up': (hStart, wStart + leftRight_distance), 'down': (hEnd - upDown_distance, wStart + leftRight_distance),
           'left': (hStart + upDown_distance, wStart), 'right': (hStart + upDown_distance, wEnd - leftRight_distance)}

    # 存放直线的像素点坐标
    axis = []
    for i in range(len(dire)):
        for j in range(len(dire[i])):
            if dire[i][j] == 255:  # 判断为白色像素
                # 对应在原图中的高宽坐标
                h = i + dic[type][0]
                w = j + dic[type][1]
                axis.append([w, h])

    data_np = np.array(axis)  # 坐标矩阵化
    output = cv2.fitLine(data_np, cv2.DIST_L2, 0, 0.01, 0.01)  # 直线拟合
    #     print(output)
    k = output[1] / output[0]
    b = output[3] - k * output[2]
    return k, b


def crop(h, w, cnt):
    '''
    将图形裁剪出上下左右四个部分的中间位置
    :param cnt: 需要裁剪的图片
    :return:
    '''
    global upDown_distance, leftRight_distance
    # 上下部分裁剪的宽度
    upDown_distance = h
    # 左右部分裁剪的宽度
    leftRight_distance = w
    up = cnt[0:upDown_distance, leftRight_distance:wEnd - wStart - leftRight_distance]
    down = cnt[hEnd - hStart - upDown_distance:hEnd - hStart, leftRight_distance:wEnd - wStart - leftRight_distance]
    left = cnt[upDown_distance:hEnd - hStart - upDown_distance, 0:leftRight_distance]
    right = cnt[upDown_distance:hEnd - hStart - upDown_distance, wEnd - wStart - leftRight_distance:wEnd - wStart]

    # 显示四个边长裁剪过后的图片
    #     cv2.imshow('up', up)
    #     cv2.imshow('down', down)
    #     cv2.imshow('left', left)
    #     cv2.imshow('right', right)
    return up, down, left, right


def getCoordinate(k1, b1, k2, b2):
    x = (b2 - b1) / (k1 - k2)
    y = k1 * x + b1
    return int(x), int(y)


def drawCenter(a, b, c, d):
    # 显示边长交点
    cv2.circle(img, (a[0], a[1]), 3, (0, 0, 255), -1)
    cv2.circle(img, (b[0], b[1]), 3, (0, 0, 255), -1)
    cv2.circle(img, (c[0], c[1]), 3, (0, 0, 255), -1)
    cv2.circle(img, (d[0], d[1]), 3, (0, 0, 255), -1)
    # 画边界线
    cv2.line(img, (a[0], a[1]), (b[0], b[1]), (0, 255, 0), 1)
    cv2.line(img, (b[0], b[1]), (c[0], c[1]), (0, 255, 0), 1)
    cv2.line(img, (a[0], a[1]), (d[0], d[1]), (0, 255, 0), 1)
    cv2.line(img, (c[0], c[1]), (d[0], d[1]), (0, 255, 0), 1)

    xCenter = (a[0] + b[0] + c[0] + d[0]) // 4
    yCenter = (a[1] + b[1] + c[1] + d[1]) // 4
    cv2.circle(img, (xCenter, yCenter), 4, (0, 0, 255), -1)

    return xCenter, yCenter


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)  # 设置窗口的大小

    for i in range(4):
        for j in range(6):
            ret, img = cap.read()

    # img = cv2.imread('/Users/duanhao/Desktop/8.jpg')

    # 需要裁剪的区域###################################
    hStart, hEnd, wStart, wEnd = 100, 720, 280, 870
    ################################################
    cropImg = img[hStart:hEnd, wStart:wEnd]

    # 图像inRange二值化处理
    hsv = cv2.cvtColor(cropImg, cv2.COLOR_BGR2HSV)
    l_g = np.array([0, 0, 0])  # 阈值下限
    u_g = np.array([255, 255, 110])  # 阈值上限   90-120
    mask = cv2.inRange(hsv, l_g, u_g)

    # cv2.imshow('cropImg', cropImg)
    # cv2.imshow('Img', img)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 传入二值化后的图片返回裁剪出来的四个边长举行
    # 上下部分裁剪的宽度
    upDown_distance = 80
    # 左右部分裁剪的宽度
    leftRight_distance = 80
    try:
        # 传入参数1：上下部分裁剪宽度; 参数2：左右部分裁剪宽度

        up, down, left, right = crop(upDown_distance, leftRight_distance, mask)
        # 在img原图中拟合四条直线 -> 得到拟合直线的k，b
        up_k, up_b = draw_fit_line(up, 'up')
        down_k, down_b = draw_fit_line(down, 'down')
        left_k, left_b = draw_fit_line(left, 'left')
        right_k, right_b = draw_fit_line(right, 'right')

        # 求出A，B， C， D四个边长交点坐标 -> 顺时针方向定义ABCD点
        A = getCoordinate(up_k, up_b, left_k, left_b)
        B = getCoordinate(up_k, up_b, right_k, right_b)
        C = getCoordinate(down_k, down_b, right_k, right_b)
        D = getCoordinate(down_k, down_b, left_k, left_b)

        # 画出边界线以及中心点
        xCenter, yCenter = drawCenter(A, B, C, D)
        print('四个顶点坐标', A, B, C, D)
        print('中心点坐标：', xCenter, yCenter)

        cv2.imshow('cropImg', cropImg)
        # cv2.imshow('Img', img)
        # cv2.imshow('mask', mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print('没有裁剪好图片，识别不到黑色方框！')
        print(f'原来图形尺寸为{img.shape[0:1]}')
        xCenter, yCenter = 545, 420

    xc1, yc1 = -1, -1
    while math.sqrt(abs(xCenter - xc1) ** 2 + abs(yCenter - yc1) ** 2) > 10:
        ret, img = cap.read()
        cropImg = img[hStart:hEnd, wStart:wEnd]
        angle_down += 1
        move_servo(0, angle_down)
        time.sleep(2)
        # 找激光点 -> 重复执行
        xc1, yc1, xc2, yc2 = findLaser(cropImg)
        # 对应到原点中的激光坐标
        # xc2, yc2 = xc2 + wStart, yc2 + hStart
        # print('红色激光点坐标:', xc2, yc2)
        xc1, yc1 = xc1 + wStart, yc1 + hStart
        # PID(xc1, yc1, xCenter, yCenter)
        print('绿色激光点坐标:', xc1, yc1)
    print("归位成功！")