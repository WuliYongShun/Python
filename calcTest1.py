#!/usr/bin/python
# _*_coding:utf-8 _*_

from calc import sum
from calc import calce

print(sum(12,30))
print(calce(25,2))
num = 89

def add():
    global num
    num = num + 1

print(num)
add()
print("###"+str(num)+"###")