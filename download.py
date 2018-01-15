#!/usr/bin/python
# _*_ coding:utf-8 _*_

import requests
url = 'http://96.ierge.cn//7/109/218490.mp3'
r = requests.get(url)
with open("music/demo3.mp3", "wb") as code:
     code.write(r.content)