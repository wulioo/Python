# -*- codeing = utf-8 -*-
# @Time : 2020/9/10 10:33 上午
import requests
import pymysql
from bs4 import BeautifulSoup as Bs


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

# --设置通用url
url = 'https://movie.douban.com/top250?start='


def get_url(url_page):
    reps = requests.get(url_page, headers=headers).text

    return reps


def bs4_soup():
    # --设置一个循环,循环十页获取的电影
    movie_page = []
    for index in range(1, 10):
        # --每一页*25
        url_page = url + str(index * 25)
        # -- 调用get_url函数
        reps = get_url(url_page)
        # --创建bs对象，并且对网页进行解析
        soup = Bs(reps, 'lxml')
        # --查询reps div模块下的class=item内容
        soup = soup.find_all(class_="item")
        movie_all = []
        for s in soup:
            movie_list = []
            # --查询item下的a标签href属性内容
            soup_a = s.a['href']
            movie_list.append(soup_a)
            # --查询所有a标签，然后输出所有标签中的“字符串”内容；
            title_list = []
            for string in s.find_all(class_='title'):
                string = string.text
                # -- / The Shawshank Redemption 将/替换成空格
                string = string.replace('/', ' ')
                # --去掉字符串首尾空格
                string = string.strip()
                title_list.append(string)
            movie_list.append(title_list)

            # --获取item下img标签属性src的内容
            soup_img = s.img['src']
            movie_list.append(soup_img)

            # --获取item标签下span,class为ohter其他内容
            soup_other = s.find(class_='other').text
            # --去掉/符号和空格符号
            soup_other = soup_other.replace('/', '').strip()
            movie_list.append(soup_other)

            # --获取item标签P标签的电影的内容
            content = s.find('p').text
            # --去掉电影内容前后空格符号和br换行符
            content = content.replace('\n', '').replace('\r', '').replace(' ', '').strip()
            movie_list.append(content)

            # --获取item标签下的电影评分和评价人数
            eva = s.find_all('span')[-2:]  # 查找span标签 在讲最后两个元素取出循环 拿出内容
            eva_list = []
            for e in eva:
                eva_list.append(e.text)
            movie_list.append(eva_list)
            movie_all.append(movie_list)
        movie_page.append(movie_all)
    return movie_page

# -----保存数据到mysql中
def save_to_mysql(movie_page):
    for movie_pag in movie_page:
        for movie in movie_pag:
            # --建立数据库连接对象
            conn = pymysql.connect(host='localhost', port=3306, user='root', password='aa1234bb', db='py_doub')
            # --使用cursor()方法创建一个游标对象 cursor
            my_cursor = conn.cursor()
            # --sql语句
            insert_sql = """
                insert into doubae1(movice_name,movice_a,movice_title,movice_conntent,movice_eva,movice_img)values (%s,%s,%s,%s,%s,%s)
            """
            # --
            my_cursor.execute(insert_sql, (movie[0], movie[2], movie[1][0], movie[3], movie[4], movie[5][1]))
            # --执行sql语句
            conn.commit()
            # --关闭连接
            my_cursor.close()
            conn.close()


if __name__ == '__main__':
    movie_page = bs4_soup()
    # --save保存数据
    save_to_mysql(movie_page)


