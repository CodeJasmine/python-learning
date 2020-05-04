"""
元组既是不可变（immutable）对象，自然就没有增加、删除元素的方法。
"""

from numpy import random

# 基本操作
a = ()
b = (1, 'xiaoming', 29.5, '17312662388')
c = ('001', '2019-11-11', ['三文鱼', '电烤箱'])

# 从 [1,5) 区间内随机选择 10 个数
d = random.randint(1, 5, 10)
# 转 tuple：(1, 4, 2, 1, 3, 3, 2, 3, 4, 2)
at = tuple(d)
print(at)
# 统计 3 出现次数，恰好也为 3 次
at.count(3)
print(at)

# 可变与不可变
e = (1, 3, [5, 7], 9, 11, 13)
e[2].insert(1, 6)
print(e)
