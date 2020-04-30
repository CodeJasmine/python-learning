"""
使用Pandas做数据分析（1）
pip3 install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com pandas
"""
import pandas as pd

# 导入数据表
path1 = "./res/知乎专栏粉丝数据.csv"
# 数据集存入一个名为chipo的数据框
chipo = pd.read_csv(path1, sep='\t')
# 查看前十行
print(chipo.head(10))
# 数据集中有多少列
print(chipo.shape[1])
# 打印出全部的列名
print(chipo.columns)
# 数据集的索引
print(chipo.index)

# print(chipo['follower_count'].nunique())
