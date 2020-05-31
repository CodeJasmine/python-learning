"""
校 园 新 闻 爬 取 
pip3 install beautifulsoup4
"""
# 连接数据库出现RuntimeError: cryptography is required for sha256_password or caching_sha2 _password
# 解决办法：安装cryptography即可:pip install cryptography
import requests
from bs4 import BeautifulSoup
import pymysql


def crawl():
    info_list = []
    for num in range(1, 3):
        url = 'http://news.niit.edu.cn/4000/list'+str(num)+'.htm'
        html = requests.get(url).content
        html_doc = str(html, 'utf-8')
        soup = BeautifulSoup(html_doc, 'html.parser')
        title_list = soup.find_all('span', {'class': 'news_title'})
        for title in title_list:
            link_node = title.find('a')
            temp_dict = {}
            temp_dict['title'] = link_node['title'].strip()
            date_node = title.parent.find('span', {'class', 'news_meta'})
            temp_dict['created'] = date_node.text
            temp_dict['updated'] = date_node.text
            temp_dict['is_deleted'] = 0
            temp_dict['is_top'] = 0
            url = 'http://news.niit.edu.cn' + link_node['href']
            html = requests.get(url).content
            html_doc = str(html, 'utf-8')
            soup = BeautifulSoup(html_doc, 'html.parser')
            content_div = soup.find(
                'div', {'class': 'wp_articlecontent'})
            temp_dict['content'] = content_div.get_text()
            img_list = content_div.find_all('img')
            if len(img_list) >= 1:
                img_url = img_list[0]['src']
                temp_dict['cover'] = 'http://news.niit.edu.cn/'+img_url
            else:
                # 新闻没有图片，使用默认
                temp_dict['cover'] = 'https://pic.qqtn.com/up/2018-6/15282737257309278.jpg'
            info_list.append(temp_dict)
    return info_list


def data_insert(info_list):
    db = pymysql.connect("localhost", "root", "123456", "db_python")
    cursor = db.cursor()
    val = []
    for dic in info_list:
        item = (dic['cover'], dic['created'], dic['updated'], dic['is_deleted'],
                dic['is_top'], dic['content'], dic['title'])
        val.append(item)
    sql = "INSERT INTO info_manage (id,cover,is_top,content,title,created,updated,is_deleted) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        # 执行sql语句，批量插入
        cursor.executemany(sql, val)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    list = crawl()
    print(len(list))
    data_insert(list)
