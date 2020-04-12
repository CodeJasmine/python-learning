"""
使用Pillow来处理图像:pip3 install Pillow
"""

# 图像相关
from io import BytesIO
from PIL import Image
import requests as requests
from PIL import Image, ImageFilter
# 系统相关
import os

# 打开图片，打印其格式，大小，图片类型
img = Image.open('./day19/love.jpg')
print(img.format, img.size, img.mode)

# 复制图片,并打印其格式，大小，图片类型
img2 = Image.open('./day19/love.jpg').save('./day19/love-1.jpg')

# 用thumbnail()方法将图片生成1/4大小的缩略图
w, h = img.size
img.thumbnail((w//4, h//4))
img.save('./day19/缩略.jpg', 'jpeg')

# 使用filter()滤镜,此处使用模糊效果
img = Image.open('./day19/love.jpg')
img3 = img.filter(ImageFilter.BLUR)
img3.save('./day19/模糊.jpg', 'jpeg')

# 图片翻转
img = Image.open('./day19/love.jpg')
img4 = img.transpose(Image.FLIP_LEFT_RIGHT)
img4.save('./day19/左右翻转.jpg', 'jpeg')
img5 = img.transpose(Image.FLIP_TOP_BOTTOM)
img5.save('./day19/上下翻转.jpg', 'jpeg')
img6 = img.transpose(Image.ROTATE_90)
img6.save('./day19/旋转90°.jpg', 'jpeg')
img7 = img.transpose(Image.ROTATE_180)
img7.save('./day19/旋转180°.jpg', 'jpeg')

# 学习遍历目录和文件
list = os.listdir('./day19')
for file in list:
    if os.path.splitext(file)[-1] == '.jpg':
        print(os.path.splitext(file)[0])

# 处理网络图片
resp = requests.get(
    'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1713396441,1487163637&fm=26&gp=0.jpg')
Image = Image.open(BytesIO(resp.content))
# 在此之前可以做相关处理
Image.save('./day19/test.png')
