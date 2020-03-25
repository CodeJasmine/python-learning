"""
输入年份 如果是闰年输出为True 否则输出False
"""

year = int(input('请输入年份：'))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = (year % 4 == 0 and year % 100 != 0) or \
    year % 400 == 0
print('是否为闰年'+is_leap)
