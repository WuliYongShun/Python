#!/usr/bin/python
# _*_ coding:utf-8 _*_

import redis


if __name__ == "__main__":

    #连接
    rs = redis.Redis(host='192.168.0.104', port=6379, db=0, password="robinn")
    rs.set("addr", "sichuan chengdu")
    print( rs.get("addr") )


    #连接池
    conn = redis.ConnectionPool(host="192.168.0.104", port=6379,db=0,password="robinn")
    r = redis.Redis(connection_pool=conn)

    #管道(原子操作)
    pip = r.pipeline(transaction=True)
    r.set("fonts", "weiruanyahei")
    r.set("sizes", "12pt")
    pip.execute()

    fonts = r.get("fonts")
    sizes = r.get("sizes")

    print(fonts)
    print(sizes)