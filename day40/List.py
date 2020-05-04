"""
列表（list）作为 Python 中最常用的数据类型之一，是一个可增加、删除元素的可变（mutable）容器。
"""

from copy import deepcopy

# 基本操作
lst = [1, 'xiaoming', 29.5, '17312662388']
lst2 = ['001', '2019-11-11', ['三文鱼', '电烤箱']]

len(lst)
len(lst2)

for _ in lst:
    print(f'{_}的类型为{type(_)}')

sku = lst2[2]
sku.append('烤鸭')
print(sku)
sku.insert(1, '牛腱子')
print(sku)
item = sku.pop()
print(sku)
sku.remove(sku[0])
print(sku)

print(lst2)
lst3 = ['001', '2019-11-11', ['三文鱼', '电烤箱']]
sku_deep = lst3[2].copy()
sku_deep[0] = '腱子'
print(lst2[2])

# 浅拷贝
a = [1, 2, [3, 4, 5]]
ac = a.copy()
ac[0] = 10
ac[2][1] = 40
print(a[0] == ac[0])
print(a[2][1] == ac[2][1])

# 深拷贝
a = [1, 2, [3, 4, 5]]
ac = deepcopy(a)
ac[0] = 10
ac[2][1] = 40
print(a[0] == ac[0])
print(a[2][1] == ac[2][1])

# 切片
a = list(range(1, 20, 3))
print(a)
print(a[:3])
print(a[-1])
print(a[:-1])
print(a[1:5])
print(a[1:5:2])
print(a[::3])
print(a[::-3])
# 逆向切片


def reverse(lst):
    return lst[::-1]


ra = reverse(a)
print(ra)
