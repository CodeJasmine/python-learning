"""
数值型和容器型
"""

from random import randint, sample

# 十六进制 0x
print(0xf6)
# 使用 e 创建科学计数法表示的浮点数
print(1.11e5)

# 去掉列表中的一个最小值和一个最大值后，计算剩余元素的平均值


def score_mean(lst):
    lst.sort()
    lst2 = lst[1:-1]
    return round((sum(lst2)/len(lst2)), 1)


lst = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
score_mean(lst)

# 打印 99 乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (j, i, j*i), end='\t')
    print()

# 使用 sample 抽样，如下例子从 100 个样本中随机抽样 10 个

lst = [randint(0, 50) for _ in range(100)]
lst_sample = sample(lst, 10)
print(lst_sample)
