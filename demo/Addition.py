"""
加法测试，输入答案后会提示答案是否错误，如果错误，提示报错并返回正确答案
"""

import random

a = random.randint(0, 9)
b = random.randint(0, 9)
c = a+b
print(a, ' + ', b, ' = ?')
value = int(input('请输入答案：'))
if value == c:
    print('答案正确')
else:
    print('答案错误，正确答案为：', c)
