from PIL import Image, ImageDraw, ImageFont,ImageEnhance
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签


text = "42 段浩"
positionflag = 2 #水印位置（0：左上角，1：左下角，2：右上角，3：右下角，4：居中）
alphavalue = 1#水印透明度（范围在0——1之间的1位小数）
#设置所使用的字体
font = ImageFont.truetype(r'simkai.ttf', 200)

# 文字水印
im = Image.open('image1.jpg').convert('RGBA') # 打开原始图片，并转换为RGB
newImg = Image.new('RGBA', im.size, (255, 255, 255, 0)) # 存储添加水印后的图片
imagedraw = ImageDraw.Draw(newImg) # 创建绘制对象
imgwidth, imgheight = im.size # 记录图片大小
txtwidth = 800 # 字体宽度
txtheight = 200 # 字体高度

# 设置水印文字位置
if positionflag == 0: # 左上角
    position=(0,0)
elif  positionflag == 1: # 左下角
        position=(0,imgheight - txtheight)
elif  positionflag == 2: # 右上角
    position=(imgwidth - txtwidth,0)
elif  positionflag == 3: # 右下角
    position=(imgwidth - txtwidth, imgheight - txtheight)
elif  positionflag == 4: # 居中
    position=(imgwidth/2,imgheight/2)
# 绘制文字
imagedraw.text(position, text, font=font, fill="white")
# 设置透明度
alpha = newImg.split()[3]
alpha = ImageEnhance.Brightness(alpha).enhance(alphavalue)
newImg.putalpha(alpha)
Image.alpha_composite(im, newImg).save('frog_text.jpg','png')   # 保存图片

# 显示结果
img1 = Image.open('image1.jpg') # 打开原始图片
img2 = Image.open('frog_text.jpg') # 打开加了水印的图片
plt.subplot(121)
plt.title('原始图像')
plt.imshow(img1)
plt.subplot(122)
plt.title('添加水印后的图像')
plt.imshow(img2)
plt.show()