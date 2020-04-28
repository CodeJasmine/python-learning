"""
中文文本的情感分析
pip3 install snownlp
"""

from snownlp import SnowNLP

text = '你要感谢那些伤害过你的人，正是因为这些人你才能够变得强大。'
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标准
tags = [x for x in s.tags]
print(tags)
# 断句
print(s.sentences)
# 拼音
print(s.pinyin)

# 情绪判断，返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪
text1 = '这个演技令人作呕'
text2 = '这个演技棒到爆炸'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)
print(text1, s1.sentiments)
print(text2, s2.sentiments)

# 关键词抽取
text3 = '不愿染是与非 怎料事与愿违 心中的花枯萎 时光它去不回 但愿洗去浮华 掸去一身尘灰 再与你一壶清酒 话一世沉醉'
s3 = SnowNLP(text3)
print(s3.keywords(limit=5))
# 概念总结文章
print(s3.summary(limit=4))
