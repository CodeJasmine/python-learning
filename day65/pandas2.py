"""
Pandas_
"""

import pandas as pd

# Pandas之分块读入数据
# iterator取值boolean，默认为False，返回一个TextFileReader对象，以便逐块处理文件
chunk = pd.read_csv('test.csv', sep='\s+', iterator=True)
# 先读入一行，get_chunk设置为1表示一次读入一行，目标文件一共2行
print(chunk.get_chunk(1))
# 再读入下一行
# print(chunk.get_chunk(1))
# 此时我们的数据文件如下
# Pandas读取之空值处理
# 假设我们的数据文件如下，data列中有一个#值，我们想把它处理成NaN值
d = {'id': [1, 2], 'name': ['wangf', 'nitt'],
     'age': [21, 20], 'date': ['2020-05-28', '#']}
df = pd.DataFrame(d)
df.to_csv('test_date.csv', sep=' ', index=False)
df = pd.read_csv('test_date.csv', sep='\s+', na_values=['#'])
print('\n', df)
