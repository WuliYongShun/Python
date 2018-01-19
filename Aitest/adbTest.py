#!/usr/bin/pythyon
# _*_ coding:utf-8 _*_
# author: Robinn

import os
import sys
import PIL
import random
import requests
import subprocess

from io import BytesIO
from PIL import Image
from aip import AipImageClassify
from aip import AipOcr

while True:
    reload(sys)
    sys.setdefaultencoding('utf8')

    config = {
        "tounaowangzhe":{
            "title":(92,437,625,540),
            "answer":(148,530,602,1050),
            "point":[
                (357,595,471,627),
                (357,721,471,740),
                (357,847,471,853),
                (357,973,471,966)
            ]
        }
    }

    #模拟点击
    def click(point):
        cmd = 'adb shell input swipe %s %s %s %s %s' % (
            point[0],
            point[1],
            point[0]+random.randint(0,3),
            point[1]+random.randint(0,3),
            200
        )
        os.system(cmd)

    a = raw_input(u"请按下回车回答问题:")

    #屏幕抓取
    proobj = subprocess.Popen("adb shell screencap -p",shell=True,stdout=subprocess.PIPE)
    screenobj = proobj.stdout.read()
    screenobj = screenobj.replace(b"\r\r\n", b"\n")
    with open("screen.jpg","wb") as f:
        f.write(screenobj)

    # img_fb = BytesIO()
    # img_fb.write(screenobj)


    #PIL裁剪图片
    img = Image.open("screen.jpg")

    title_box = (92,437,625,540)
    title_img = img.crop(title_box)

    answer_box = (148,530,602,1050)
    answer_img = img.crop(answer_box)

    title_img.save("__title.jpg")
    answer_img.save("__answer.jpg")


    #读取文件
    def get_img_content(img_filepath):
        with open(img_filepath,"rb") as f:
            return f.read()


    #获取问题及答案
    def getTitleinfo(img):
        APP_ID = '104170346'
        API_KEY = 'M73AwHkxdjFXCD74rH'
        SECRET_KEY = 'G4DlQQCLybuLN6EE5evgNt1'

        #文字识别
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        res = client.basicGeneral(img)

        str = ""
        for line in res:
            if type(res[line]) == list:
                words = res[line]
                for x in words:
                    str = str+x["words"]+","
        return str[:-1]


    title_str = getTitleinfo(get_img_content("__title.jpg"))
    answer_str = getTitleinfo(get_img_content("__answer.jpg"))
    answer_str = answer_str.split(',')
    result = []
    for x in answer_str:
        result.append(x)



    # 远程获取答案
    url = "http://www.baidu.com/s"
    data = {
        "wd": title_str
    }
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"};
    response = requests.get(url=url, params=data, headers=headers)
    response.encoding = "utf-8"
    html = response.text

    reload(sys)
    sys.setdefaultencoding('utf8')
    for i in range(len(result)):
        result[i] = (html.count(result[i]),result[i],i)

    result.sort(reverse=True)
    print(data["wd"])
    print("=============================================")
    for x in result:
        print(str(x[0])+" | "+x[1]+" | "+str(x[2]))
    print("=============================================")


    #开始点击答题
    click(config["tounaowangzhe"]["point"][int(result[0][2])])












# title_img_io = BytesIO()
# title_img_io.write(title_img)
# with open("title.jpg","wb") as f:
#     f.write(title_img)
#
# answer_img_io = BytesIO()
# answer_img_io.write(answer_img)
# with open("answer.jpg","wb") as f:
#     f.write(answer_img)


# img = Image.open(img_fb)
# title_box = (100,100,200,200)
# title_img = img.crop(title_box)
# answer_box = (100,300,300,500)
# answer_img = img.crop(answer_box)
#
# print(title_img)

#
# with open("title.jpg","wb") as f:
#     f.write(title_img)
#
#
# with open("answer.jpg","wb") as f:
#     f.write(answer_img)


