"""
Pandas_3
"""

import pandas as pd
import numpy as np

# series是pandas两大数据结构中(DataFrame，Series)的一种
# 每个series对象都有两个数组组成
# index：它是从Numpy数组继承的Index对象，保存标签信息
# values：保存值的NumPy数组

# 1、创建一个series
# series的标准构造函数：Series(data=None,undex=None,dtype=None,name=None)
ps = pd.Series(data=[-3, 1, 2], index=['a', 'f', 'b'], dtype=np.float32)
print(ps)
print('**********')
# 2、series增加元素(Pandas允许包含重复的标签)
ps = ps.append(pd.Series(data=[-8.0], index=['f']))
print(ps)
print('**********')
# 3、series访问元素，有两种方法
# 通过索引访问
print(ps[2])
# 通过标签访问
print(ps['f'])
# 4、series之删除元素，append操作和drop操作都是发生在原数据的副本上，不是原数据上
ps = ps.drop('f')
print(ps)
print('**********')
# 5、series之修改元素
ps['b'] = 10.0
print(ps)
