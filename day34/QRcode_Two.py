"""
用myqr库制作二维码
"""

from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont

# 图片背景二维码，如使用gif背景，则可以生成动态背景效果


def img_code():
    myqr.run(words='http://111.1.21.146/amobile.music.tc.qq.com/C4000018uCdG0pSm65.m4a?guid=204467990&vkey=FDA0D4BD4FF84A4F0EDA3B474291E60545D725127FF36D99CBF2F1E1E20173924A2FB5ACB1D9B077E6B3F12198A5F34DEC51EB3F0AF6AA94&uin=0&fromtag=66',
             # 设置容错率最高
             version=1,
             # 控制纠错水平，范围是L、M、Q、H,从左到右依次升高
             level='H',
             # 背景图
             picture='./res/avatar/25.jpg',
             # 彩色二维码
             colorized=True,
             # 用以调节图片的对比度，1.0表示原始图片，更小的值表示更低对比度，更大反之，默认为1.0
             contrast=1.0,
             # 用来调节图片的亮度，其余用法和取值同上
             brightness=1.0,
             # 保存图片的名字,格式可以是jpg，png，bmp，gif
             save_name='QRcode1.png',
             # 保存位置
             save_dir=os.getcwd() + '/res/img/'
             )


def draw():
    img = Image.open('./res/img/QRcode1.png')
    w, h = img.size
    txt = '这首歌送给你'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./res/font/SimHei.ttf', 26)
    draw.text((w/2-100, 10), txt, (0, 0, 0), font=font)
    img.save('./res/img/QRcode2.png')


if __name__ == '__main__':
    img_code()
    draw()
