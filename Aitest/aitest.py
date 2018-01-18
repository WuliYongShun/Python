#!/usr/bin/pythyon
# _*_ coding:utf-8 _*_


from aip import AipOcr
import json

# 定义常量
APP_ID = '10704346'
API_KEY = 'M73AwH6k1rpxdGEjFXCD74rH'
SECRET_KEY = 'G4DlQ4GIW9vbcBQCLybuLN6EE5evgNt1'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "1.jpg"
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(json.dumps(result).decode("unicode-escape"))