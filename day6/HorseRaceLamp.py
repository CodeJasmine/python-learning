"""
在屏幕上显示跑马灯文字
"""


import os
import time
from termcolor import *


def main():
    content = '人的一生注定会遇到两个人 一个惊艳了时光 一个温柔了岁月。'
    color = ['red', 'yellow', 'green', 'blue']
    i = 0
    while True:
        # 清理屏幕上的输出
        # os.system('cls')  # os.system('clear)
        index = i % len(color)
        print(colored(content, color[index]))
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]
        i = i+1


if __name__ == '__main__':
    main()
