"""
字典创建方法
"""

# 5种创建方法，注意dict是关键词，所有变量名取的是dic
# 1、手动创建
empty = {}
dic = {'a': 1, 'b': 2, 'c': 3}
print(dic)
# 2、使用dict()构造函数
dic2 = dict(a=1, b=2, c=3)
print(dic2)
# 3、键值对+关键字参数
dic3 = dict({'a': 1, 'b': 2}, c=3, d=4)
print(dic3)
# 4、可迭代对象：列表，元素又为一个元组，后面再加一系列关键字参数
dic4 = dict([('a', 1), ('b', 2)], c=3)
print(dic4)
# 5、fromkeys()方法
dic5 = {}.fromkeys(['k1', 'k2', 'k3'], [1, 2, 3])
print(dic5)
