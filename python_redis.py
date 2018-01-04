#!/usr/bin/python
# _*_ coding:utf-8 _*_

import redis

if __name__ == "__main__":
    rs = redis.Redis(host='192.168.0.104', port=6379, db=0, password="robinn")
    rs.set("addr", "sichuan chengdu")
    print( rs.get("addr") )

    
