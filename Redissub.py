#!/usr/bin/python
# _*_ coding:utf-8 _*_

from RedisHelper import RedisHelp

#订阅
if __name__ == "__main__":
    r = RedisHelp()
    redis_sub = r.sub()

    while True:
        msg = redis_sub.parse_response()
        print(msg)