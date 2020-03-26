"""
加法测试，随机产生两个一位数的整数，然后使其相加，测试输入答案后是否正确，如果错误，提示报错并返回正确答案
"""

import random

a = random.randint(0, 9)
b = random.randint(0, 9)
print(a, ' + ', b, ' = ?')
value = int(input('请输入答案：'))
if value == (a+b):
    print('答案正确')
else:
    print('答案错误，正确答案为：', (a+b))
