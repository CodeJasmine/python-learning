"""
按行读文件
"""
from collections import defaultdict
import re

# 正则，匹配单词
rec = re.compile(r'\s+')
# 统计单词出现频率
dd = defaultdict(int)
# 读取文件 r+表示读写模式
with open('./res/txt/当我老了.txt', 'r+') as f:
    # 每次读取一行
    for line in f:
        clean_line = line.strip()
        if clean_line:
            # 正则分词
            words = rec.split(clean_line)
            # 遍历，统计
            for word in words:
                dd[word] += 1
# 按照频次降序排列
dd = sorted(dd.items(), key=lambda x: x[1], reverse=True)
print('---输出结果---')
print(dd)
