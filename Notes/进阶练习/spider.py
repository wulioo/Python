# -*- codeing = utf-8 -*-
# @Time : 2020/8/23 10:53 上午
# ---------网页解析，获取数据------------
from bs4 import BeautifulSoup
# ---------------------
import re
# ---------正则表达式,文字匹配------------
import urllib.request, urllib.error
# ---------进行excel操作------------
import xlwt
# ---------进行SQLite数据库操作------------
import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?staer="
    datalist = getDate(baseurl)
    savepath = "douban.xls"


    # 3.保存数据
    saveDate(datalist, savepath)

    #askURL(baseurl)

# ------1.爬取网页---------
# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
findImagSrc = re.compile(r'<img.*src="(.*?)"', re.S)  #re.S 让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findIng = re.compile(r'<span class="ing">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

def getDate(baseurl):
    datalist = []
    # 调用范围（0-10）页，10次
    for i in range(0, 10):
        url = baseurl + str(i*25)
        print(url)
        # 保存获取到的网页源码
        html = askURL(url)
     # 2.逐一分析
        soup = BeautifulSoup(html, "html.parser")
        #查找符合要求的字符串，将div节点属性item存储形成一个列表
        try:
            for item in s.find_all('div', class_="item"):
                # 测试，查看电影item的全部信息
                #print(item)
                data = []
                item = str(item)
                # re库用来通过正则表达式来查找指定的字符串
                link = re.findall(findLink, item)[0]
                data.append(link)
                #print(data)
                imgSrc = re.findall(findImagSrc, item)[0]
                data.append(imgSrc)
                Title = re.findall(findTitle, item)
                if (len(Title) == 2):
                    # 添加中文名
                    ctitle = Title[0]
                    data.append(Title)
                    # 添加外国名
                    otitle = Title[1].replace("/", "")  #去掉无关的符号
                    data.append(otitle)
                else:
                    data.append(Title[0])
                    data.append('')     #外国名字留空

                Rating = re.findall(findRating, item)[0]
                data.append(Rating)
                Judge = re.findall(findJudge, item)[0]
                data.append(Judge)
                Ing = re.findall(findIng, item)
                if len(Ing) != 0:
                    Ing = Ing[0].replace("。","")
                    data.append(Ing)
                else:
                    data.append(" ")
                Bd = re.findall(findBd, item)[0]
                re.sub('<br(\s+)?/>(\s+)?'," ", Bd)  #去掉<br/>
                re.sub('/', " ", Bd)
                # 去掉前后前后空格
                data.append(Bd.strip())
                # 将处理好的一部电影放入datalist
                datalist.append(data)
        except Exception as result:
            print(result)
    print(datalist)
    return datalist







# -----得到指定一个URL网页的内容
def askURL(url):
    # 模拟浏览器头部信息，表示告诉服务器我们是什么类型的机器来进行访问
    # head = {'Use-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    # 封装了一个req对象
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    html = ""
    try:
        # 传递一个封装好的req对象给responce
        responce = urllib.request.urlopen(req)
        # 读取服务器返回的信息并且解码utf-8
        html = responce.read().decode("utf-8")
        #print(html)
    except Exception as result:

        print(result)

    return html
def saveDate(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8")
    # cell_overwrite_ok=True 是否覆盖
    sheet = book.add_sheet('豆瓣Top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0,8):
        sheet.write(0, i, col[i])#列名
    for y in range(0,250):
        print("第{}条".format(y))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1,j,data[j])


    book.save('student.xls')


# ----当程序执行时---------
if __name__ == "__main__":
    # 调用函数main
    main()