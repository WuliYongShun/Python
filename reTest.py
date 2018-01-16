#!/usr/bin/python
# _*_ coding:utf-8 _*_

import re

if __name__ == "__main__":

    str = "where is w3c are you ready"
    obj = re.match("where",str)
    print(obj.span())


    objgroup = re.search(r"(.*) is (.*?) are (.*) ready", str, re.M|re.I)
    if objgroup:
        print(objgroup.group())
        print(objgroup.group(0))
        print(objgroup.group(1))
        print(objgroup.group(2))
        print(objgroup.group(3))

    tel = "0385-2560456-451 #这是一个国内电话"
    num = re.sub(r"#.*$","",tel)
    print(num)

    num1 = re.sub(r"\D","",tel)
    print(num1)