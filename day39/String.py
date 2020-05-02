"""
字符串
"""

import re

# strip 用于去除字符串前后的空格
print(' I love her\t\n '.strip())

# replace 用于字符串的替换
print('I love her'.replace(' ', '_'))

# join 用于合并字符串
print('_'.join(['book', 'store', 'count']))

# title 用于单词的首字符大写
print('i love her'.title())

# find 用于返回匹配字符串的起始位置索引
print('i love her'.find('her'))

# 判断 str1 是否由 str2 旋转而来
#  原理：判断str1 是否为 str2+str2 的子串
#  如 str1 = 'ab' str2 = 'ba' str2+str2 = 'baba',显然str1 in str2 + str2
#  再通过判断两个字符串是否有空的，或者长度是否相等，用于排除


def is_rotation(s1: str, s2: str) -> bool:
    if s1 is None or s2 is None:
        return False

    if len(s1) != len(s2):
        return False

    def is_substring(s1: str, s2: str) -> bool:
        return s1 in s2

    return is_substring(s1, s2 + s2)


r = is_rotation('stringbook', 'bookstring')
print(r)

r = is_rotation('greatman', 'maneatgr')
print(r)

# 密码安全检查，使用正则表达式非常容易实现
# 密码安全要求：
#  要求密码为 6 到 20 位
#  密码只包含英文字母和数字
pat = re.compile(r'[\da-zA-Z]{6,20}')
# \d匹配数字 0-9
pat.fullmatch('abc12')
pat.fullmatch('asdfghjklqwerttyuiop1234567890')
pat.fullmatch('qaz_231')
pat.fullmatch('abc123456')
