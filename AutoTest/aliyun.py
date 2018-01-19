#!/usr/bin/pythyon
# _*_ coding:utf-8 _*_
# author: Robinn

from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

#构建应用
phantomjsURL = "C:/Users/admin/Desktop/demos/Tools/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe"
driver = webdriver.PhantomJS(executable_path=phantomjsURL)
while True:
    driver.get('https://mailsso.mxhichina.com/login.htm?app_code=smartmail&lang=zh_CN&network_env=1&redirect_url=https%3A%2F%2Fqiye.aliyun.com%2Falimail%2Fauth%2FcallbackForCore%3Freurl%3D%252Falimail%252F&sign=02e70dd7a0011d0cd92b9e8d8b3e8cd1')
    driver.find_element_by_xpath('//*[@id="username"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('postmaster@herbsdyyy.org.cn')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('MS123dox')
    driver.find_element_by_xpath('//*[@id="login_submit_btn"]').click()
    sreach_window = driver.current_window_handle

    try:
        dr = WebDriverWait(driver,10)
        if driver.find_element_by_xpath('//*[@id="root_nav_ding"]'):
            driver.find_element_by_xpath('//*[@id="header_wrap"]/div[3]/div[3]').click()
            print(u'点击进入邮箱')
    except:
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="login_checkcode_ico"]').click()
        time.sleep(5)
        driver.save_screenshot('screen_shoot.jpg')


        #PIL裁剪图片
        img = Image.open("screen_shoot.jpg")
        yzm_box = (198,147,300,178)
        yzm_img = img.crop(yzm_box)
        yzm_img.save("yzm.jpg")



        #验证码识别
        from aip import AipOcr
        APP_ID = '10704346'
        API_KEY = 'M73AwH6k1rpxdGEjFXCD74rH'
        SECRET_KEY = 'G4DlQ4GIW9vbcBQCLybuLN6EE5evgNt1'
        def get_img_content(img_filepath):
            with open(img_filepath,"rb") as f:
                return f.read()

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        img = get_img_content("yzm.jpg")
        res = client.basicGeneral(img)

        str = ""
        for line in res:
            if type(res[line]) == list:
                words = res[line]
                for x in words:
                    str = str+x["words"]+","
                    print x["words"]

        yzm = str[:-1]
        #成功识别验证码后登陆
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('MS123dox')
        driver.find_element_by_xpath('//*[@id="login_checkcode"]').send_keys(yzm)
        driver.find_element_by_xpath('//*[@id="login_submit_btn"]').click()
        time.sleep(10)
        driver.save_screenshot('screen_shoot1.jpg')

        try:
            if driver.find_element_by_xpath('//*[@id="root_nav_ding"]'):
                driver.maximize_window()
                print(u"已经打开邮箱中转页面。。。请稍等。。。")
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="header_wrap"]/div[3]/div[3]').click()
                time.sleep(10)
                break
        except:
            continue

driver.find_element_by_xpath('//*[@id="sqm_71"]/div/div').click()
time.sleep(10)
driver.save_screenshot('screen_shoot2.jpg')
os.system("mspaint screen_shoot2.jpg")