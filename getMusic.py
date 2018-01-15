#!/usr/bin/python
# _*_ coding:utf-8 _*_
# 音乐爬虫

if __name__ == "__main__":
    # num = 245610
    # print(int(num/30000))
    # print(int(num/2000))
    import requests
    from bs4 import BeautifulSoup
    file = open("music.html","r")
    html_doc = file.read()
    # print(html_doc)

    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify())
    content1 = soup.find(id="content1")

    li = content1.find_all("li")

    #目标音乐站
    url = "http://96.ierge.cn/"
    musicid = []
    musicname = []
    musicurl = []
    for x in li:
        mtitle = x.a.get("title")
        musicname.append(mtitle)
        ids = x.input.get("title")
        musicid.append(ids)
        n1 = int(int(ids)/30000)
        n2 = int(int(ids)/2000)
        xurl = url + "/" + str(n1) + "/" + str(n2) + "/" + ids+".mp3"
        musicurl.append(xurl)
        # print x.input.get("title")
        print(xurl)
        print(mtitle)


        # url = 'http://96.ierge.cn/7/109/218490.mp3'
        r = requests.get(xurl)
        with open("music/"+mtitle+".mp3", "wb") as code:
            code.write(r.content)
        print(" 下载完成。。。。")