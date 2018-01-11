#!/user/bin/python
# _*_ coding:utf-8 _*_

import math
import time
import calendar

print(time.time())

localtime = time.localtime(time.time())
print(localtime)

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2018,5)
print(cal)


print(2+3)
print(2-3)
print(2*3)
print(9/3)
print(9%2)
print(2 ** 3)
print(9//2)

print("++++++++++++++++++++++++++++")

print(2==3)
print(2!=3)

print(2>3)
print(2<3)
print(2>=3)
print(2<=3)
print(2<>3)
















