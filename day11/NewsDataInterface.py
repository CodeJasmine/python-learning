"""
新闻数据接口
"""

import json
import requests

resp = requests.get(
    'http://api.tianapi.com/allnews/index?key=af156f34f0214b95825cbf7418c2f0ee&num=50&col=7')
newslist = json.loads(resp.text)['newslist']
result = []
data = "./day11/data.json"
for news in newslist:
    temp_dict = {}
    temp_dict['title'] = news['title']
    temp_dict['pic_url'] = news['picUrl']
    result.append(temp_dict)
with open(data, 'w') as f:
    json.dump(result, f)
