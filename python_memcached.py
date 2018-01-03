#! /usr/bin/python
# _*_ coding:utf-8 _*_

import memcache

mc = memcache.Client(["192.168.0.104:11211"], debug=True)
#mc.set("name", "robinn")
#result = mc.get("name")
#print(result)


print(mc.get("addr"))