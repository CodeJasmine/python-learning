"""
基础词云
pip3 install numpy matplotlib pillow wordcloud imageio jieba snownlp itchat -i https://pypi.tuna.tsinghua.edu.cn/simple
"""

import wordcloud
import random

# 创建词云对象
w = wordcloud.WordCloud()
# 通过字符串生成词云
w.generate("If you never come, my smile is very bright\
            Playing with what you like heartlessly\
            Don't worry about time, don't worry about who's sad or happy\
            If you've never been here, my character is sunny\
            I will not lose my temper willfully or stay up all night\
            Don't pretend to be sad, don't pretend to be pitiful\
            I can wait for a leaf on Sunday morning\
            Looking at the moon of the 15th, we can draw the peaks of mountains and rivers\
            My heart is full of fairy tales\
            I read all night in my dream\
            But then the leaves fall early in the morning")
# 生成本地图片
w.to_file('./res/img/output1.png')

# 创建词云对象，设置词云图片宽、高、字体、背景颜色等参数
# 中文字体需要提前下载中文字体文件
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='#eee',
                        font_path='./res/font/SimHei.ttf')
w.generate('如果你不曾来过，我的笑容很灿烂\
            没心没肺的玩着自己喜欢的事\
            不用管时间，也不用管谁的悲欢\
            如果你不曾来过，我的性格很阳光\
            不会任性的发脾气，也不会彻夜不眠\
            不用伪装悲伤，也不用故作可怜\
            我可以在星期天的清晨等一片叶子\
            遥望十五的月亮勾画山河的峰峦\
            我的心中塞满了童话的故事\
            梦乡里我读了一夜的书\
            可是后来清晨的叶子总早一步落下')
w.to_file('./res/img/output2.png')
