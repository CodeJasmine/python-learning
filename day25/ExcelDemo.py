"""
把班级卡片数据excel表读入，循环遍历所有数据，每行对应一个字典对象，将sheet转成一个list里套字典的，顺便将整个内容生成个词云图。
"""

import xlrd
import os
import random
import wordcloud

wordbook = xlrd.open_workbook('./res/excel/班级资料.xlsx')
sheet = wordbook.sheets()[0]
list = sheet.col_values(3)+sheet.col_values(13)
# 构建并配置词云对象
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#6c909e',
    colormap='Pastel1',
    font_path='./res/font/SimHei.ttf'
)
string = " ".join(list)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出
w.to_file('./res/img/output5.png')
