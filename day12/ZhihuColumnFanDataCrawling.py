"""
爬取知乎专栏粉丝数据
"""

import requests
import csv
import json


def crawl():
    url = "https://www.zhihu.com/api/v4/columns/smetalk/followers"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    csvfile = open('./day12/知乎专栏粉丝数据.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    keys = {'id', 'name', 'url', 'gender', 'avatar_url', 'follower_count'}
    writer.writerow(keys)

    # 查询参数
    for j in range(50000):
        params = {
            "limit": 20,
            "offset": j,
            "include": "data[*].follower_count,gender,is_followers"
        }

        response = requests.get(url, headers=headers, params=params)
        print("请求URL：", response.url)
        print("返回的数据：", response.text)

        i = 1
        for dic in response.json().get("data"):
            writer.writerow([dic['id'], dic['name'], dic['url'],
                             dic['gender'], dic['avatar_url'], dic['follower_count']])
            i += 1
    csvfile.close


if __name__ == '__main__':
    crawl()
