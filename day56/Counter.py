"""
分析数据的时候统计计数
"""

from collections import Counter
# 习惯使用list的，往往会这样统计
sku_purchase = [3, 5, 8, 4, 8, 8, 5, 9, 7, 5, 2, 3, 5, 4]

d = {}
for i in sku_purchase:
    if d.get(i) is None:
        d[i] = 1
    else:
        d[i] += 1

d_most = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# 最受欢迎的商品（键为商品编号），排序结果：
print(d_most)
# 如果使用Counter，能写出更加简化的代码
# 一行代码搞定，便输出统计结果，并且输出按照购买次数的由大到小排序好的列表
print(Counter(sku_purchase).most_common())
# 除此之外，使用Counter还能快速统计一句话中单词出现次数，一个单词中字符出现次数
print(Counter('I love python so much').most_common())
