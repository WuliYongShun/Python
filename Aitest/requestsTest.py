#!/usr/bin/pythyon
# _*_ coding:utf-8 _*_
# author: Robinn

import requests
import sys
result = [u"松本行弘", u"詹姆斯·高斯林", u"林纳斯·托瓦兹", u"方立勋"]
#result = [u"1895年10月26日", u"1891年11月20日", u"1893年12月26日", u"1892年12月26日"]

url = "http://www.baidu.com/s"
data = {
    "wd": u"java之父是谁?"
}

# data = {
#     "wd": u"毛主席生日?"
# }
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