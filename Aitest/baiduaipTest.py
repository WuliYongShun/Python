#!/usr/bin/pythyon
# _*_ coding:utf-8 _*_
# author: Robinn

from aip import AipImageClassify
from aip import AipOcr


def get_img_content(img_filepath):
    with open(img_filepath,"rb") as f:
        return f.read()

APP_ID = '10704346'
API_KEY = 'M73AwH6k1rpxdGEjFXCD74rH'
SECRET_KEY = 'G4DlQ4GIW9vbcBQCLybuLN6EE5evgNt1'

# 图像识别
# client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
# img = get_img_content("test.jpg")
# res = client.objectDetect(img)
# print(res)


#文字识别
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
img = get_img_content("2.png")
res = client.basicGeneral(img)

# print rest
str = ""
for line in res:
    if type(res[line]) == list:
        words = res[line]
        for x in words:
            str = str+x["words"]+","
            print x["words"]
print("===================================")
print(str)
print("===================================")


