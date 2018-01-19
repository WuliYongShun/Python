#!/usr/bin/pythyon
# _*_ coding:utf-8 _*_
# author: Robinn

import os
import sys
import time

from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

reload(sys)
sys.setdefaultencoding("utf-8")

#构建应用
phantomjsURL = "C:/Users/admin/Desktop/demos/Tools/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe"
driver = webdriver.PhantomJS(executable_path=phantomjsURL)


#内分泌增高站开始提交
#sj
driver.get('http://4g.ztet120.com/ynxw/')  #4g.ztet120.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_4g.ztet120.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="form"]/div/div[4]/input[1]').click()
sreach_window = driver.current_window_handle


driver.get('http://4g.029xianjkek.com/ynxw/') #4g.029xianjkek.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_4g.029xianjkek.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="form"]/div/div[4]/input[1]').click()
sreach_window = driver.current_window_handle


driver.get('http://4g.xianlh120.com/ynxw/') #4g.xianlh120.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_4g.xianlh120.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="form"]/div/div[4]/input[1]').click()
sreach_window = driver.current_window_handle


driver.get('http://4g.029xalhjk.com/ynxw/') #4g.029xalhjk.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_4g.029xalhjk.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="form"]/div/div[3]/div[10]/input[1]').click()
sreach_window = driver.current_window_handle


#pc
driver.get('http://pc.029jingke.com/news/347.html') #pc.029jingke.com
driver.find_element_by_xpath('//*[@id="topname"]').send_keys('tester_pc.029jingke.com')
driver.find_element_by_xpath('//*[@id="tophometel"]').send_keys('13888888888')
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[5]/form/div/div[12]/input').click()
sreach_window = driver.current_window_handle



#发育行为站开始提交
#sj
driver.get('http://3g.029xianjkek.com/yyxw/') #3g.029xianjkek.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_3g.029xianjkek.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="form"]/div[3]/input[1]').click()
sreach_window = driver.current_window_handle


driver.get('http://3g.xianlh120.com/yyxw/') #3g.xianlh120.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_3g.xianlh120.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="form"]/div[3]/input[1]').click()
sreach_window = driver.current_window_handle


driver.quit()
driver = webdriver.PhantomJS(executable_path=phantomjsURL)

driver.get('http://3g.029xianerke.com/yyxw/') #3g.029xianerke.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_3g.029xianerke.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="form"]/div[3]/input[1]').click()
sreach_window = driver.current_window_handle


driver.get('http://3g.029xalhjk.com/yyxw/') #3g.029xalhjk.com
driver.find_element_by_xpath('/html/body/div[9]/form/div[1]/div[3]/ul/li[1]/div/input').send_keys('tester_3g.029xalhjk.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('/html/body/div[9]/form/div[2]/ul/li[2]/input').click()
sreach_window = driver.current_window_handle



driver.get('http://3g.029jingke.com/yyxw/') #3g.029jingke.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_3g.029jingke.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="form"]/div[3]/input[1]').click()
sreach_window = driver.current_window_handle


driver.get('http://3g.02981329999.com/yyxw/') #3g.02981329999.com
driver.find_element_by_xpath('//*[@id="name"]').send_keys('tester_3g.02981329999.com')
driver.find_element_by_xpath('//*[@id="hometel"]').send_keys('13888888888')
driver.find_element_by_xpath('//*[@id="gh"]/div[1]/input').click()
sreach_window = driver.current_window_handle


#pc
driver.get('http://www.xianlh120.com/ystd/580.html') #www.xianlh120.com
driver.find_element_by_xpath('//*[@id="topname"]').send_keys('tester_www.xianlh120.com')
driver.find_element_by_xpath('//*[@id="tophometel"]').send_keys('13888888888')
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[5]/form/div/div[3]/input').click()
sreach_window = driver.current_window_handle



driver.get('http://www.029jingke.com/ystd/580.html') #www.029jingke.com
driver.find_element_by_xpath('//*[@id="topname"]').send_keys('tester_www.029jingke.com')
driver.find_element_by_xpath('//*[@id="tophometel"]').send_keys('13888888888')
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[5]/form/div/div[3]/input').click()



driver.get('http://www.02981329999.com/ystd/580.html') #www.02981329999.com
driver.find_element_by_xpath('//*[@id="topname"]').send_keys('tester_www.02981329999.com')
driver.find_element_by_xpath('//*[@id="tophometel"]').send_keys('13888888888')
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[5]/form/div/div[3]/input').click()
sreach_window = driver.current_window_handle


print(u"发送测试完成。正常运行。无异常。")
driver.quit()
driver = webdriver.PhantomJS(executable_path=phantomjsURL)

#打开邮箱服务
while True:
    driver.get('https://mailsso.mxhichina.com/login.htm?app_code=smartmail&lang=zh_CN&network_env=1&redirect_url=https%3A%2F%2Fqiye.aliyun.com%2Falimail%2Fauth%2FcallbackForCore%3Freurl%3D%252Falimail%252F&sign=02e70dd7a0011d0cd92b9e8d8b3e8cd1')
    driver.find_element_by_xpath('//*[@id="username"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
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
        APP_ID = '1074346'
        API_KEY = 'M73AwH6jFXCD74rH'
        SECRET_KEY = 'G4DlQ4GILN6EE5evgNt1'
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
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
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


#退出应用
sys.exit(0)
driver.quit()
