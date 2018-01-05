#!/usr/bin/python
# _*_ coding:utf-8 _*_

from RedisHelper import RedisHelp

#发布
if __name__ == "__main__":
    rs = RedisHelp()
    flag = rs.pub("hello")
    print("publisher: hello | successful!"+ str(flag))