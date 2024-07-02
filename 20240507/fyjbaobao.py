# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:02:53 2023

@author: 杨艳林
"""


from aip import AipFace
from picamera import PiCamera
import urllib.request
import RPi.GPIO as GPIO
import base64
import time
from time import sleep

servo_pin = 18 #18为BCM编码               # 舵机信号线接树莓派GPIO12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servo_pin, GPIO.OUT, initial=False)

#百度人脸识别API账号信息
APP_ID = '42995942'
API_KEY = 'GyKLkCCgdkei1DkzlCyytdWL'
SECRET_KEY = 'DNFii3njpF4ddzfagkv4YqvTqCIdnWkp'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)#创建一个客户端用以访问百度云
#图像编码方式
IMAGE_TYPE='BASE64'
camera = PiCamera()#定义一个摄像头对象
#用户组
GROUP = '01'

#照相函数
def getimage():
    camera.resolution = (1024,768)#摄像界面为1024*768
    camera.start_preview()#开始摄像
    time.sleep(2)
    camera.capture('faceimage.jpg')#拍照并保存
    time.sleep(2)
#对图片的格式进行转换
def transimage():
    f = open('faceimage.jpg','rb')
    img = base64.b64encode(f.read())
    return img    
#上传到百度api进行人脸检测
def go_api(image):
    result = client.search(str(image, 'utf-8'), IMAGE_TYPE, GROUP);#在百度云人脸库中寻找有没有匹配的人脸
    if result['error_msg'] == 'SUCCESS':#如果成功了 
        name = result['result']['user_list'][0]['user_id']#获取名字
        score = result['result']['user_list'][0]['score']#获取相似度
        if score > 80:#如果相似度大于80
            if name == 'yyl':
                print("欢迎%s !"% name)
                time.sleep(3)
            if name == 'xzh':
                print("欢迎%s !" % name)
                time.sleep(3)
        else:
            print("对不起，我不认识你！")
            name = 'Unknow'            
            return 0
        curren_time = time.asctime(time.localtime(time.time()))#获取当前时间
    
        #将人员出入的记录保存到Log.txt中
        f = open('Log.txt','a')
        f.write("Person: " + name + "     " + "Time:" + str(curren_time)+'\n')
        f.close()
        return 1
    if result['error_msg'] == 'pic not has face':
        print('检测不到人脸')
        time.sleep(2)
        return 0
    else:
        print(result['error_code']+' '+result['error_code'])
        return 0

# 旋转角度转换到PWM占空比
def angleToDutyCycle(angle):
    return 2.5 + angle / 180.0 * 10

p = GPIO.PWM(servo_pin, 50)    # 初始频率为50HZ
p.start(angleToDutyCycle(0))  # 舵机初始化角度为0
sleep(0.5)
p.ChangeDutyCycle(0)           # 清空当前占空比，使舵机停止抖动

#主函数
if __name__ == '__main__':
    while True:
        print('请对准摄像头！')
        if True:
            getimage()#拍照
            img = transimage()#转换照片格式
            res = go_api(img)#将转换了格式的图片上传到百度云
            if(res == 1):#是人脸库中的人
                print("开门，在三秒后关门！")
                angle = 180
                p.ChangeDutyCycle(angleToDutyCycle(angle))
                sleep(0.2)
                p.ChangeDutyCycle(0) # 清空当前占空比，使舵机停止抖动
                time.sleep(3)
                p.ChangeDutyCycle(angleToDutyCycle(0)) # 舵机初始化角度为0
           #     p.ChangeDutyCycle(0) # 清空当前占空比，使舵机停止抖动
                print("关门,稍等三秒进入下一个！")
                time.sleep(3)
                
            else:
                print('稍等三秒进入下一个')
                time.sleep(3)
