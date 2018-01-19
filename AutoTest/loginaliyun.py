#!/usr/bin/pythyon
# _*_ coding:utf-8 _*_
# author: Robinn

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#构建应用
phantomjsURL = "C:/Users/admin/Desktop/demos/Tools/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe"
driver = webdriver.PhantomJS(executable_path=phantomjsURL)


#打开邮箱服务
driver.get('https://mailsso.mxhichina.com/login.htm?app_code=smartmail&lang=zh_CN&network_env=1&redirect_url=https%3A%2F%2Fqiye.aliyun.com%2Falimail%2Fauth%2FcallbackForCore%3Freurl%3D%252Falimail%252F&sign=02e70dd7a0011d0cd92b9e8d8b3e8cd1')
driver.find_element_by_xpath('//*[@id="username"]').clear()
driver.find_element_by_xpath('//*[@id="password"]').clear()


driver.find_element_by_xpath('//*[@id="login_submit_btn"]').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('')
driver.find_element_by_xpath('//*[@id="login_submit_btn"]').click()
driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
driver.find_element_by_xpath('//*[@id="login_submit_btn"]')
driver.find_element_by_xpath('//*[@id="password"]').click()
driver.save_screenshot('screen_shoot.jpg')


#验证码识别
from aip import AipOcr
APP_ID = '107346'
API_KEY = 'M73AwHEjFXCD74rH'
SECRET_KEY = 'G4DlQ4GCLybuLN6EE5evgNt1'
def get_img_content(img_filepath):
    with open(img_filepath,"rb") as f:
        return f.read()

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
img = get_img_content("screen_shoot.jpg")
res = client.basicGeneral(img)

str = ""
for line in res:
    if type(res[line]) == list:
        words = res[line]
        for x in words:
            str = str+x["words"]+","
            print x["words"]
print(str)

yzm = res


#退出应用
sys.exit(0)
driver.quit()