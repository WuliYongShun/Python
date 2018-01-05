#!/usr/bin/python
# _*_ coding:utf-8 _*_

import redis

#发布和订阅
class RedisHelp(object):
    def __init__(self):
        self.__conn = redis.Redis(host="192.168.0.104", port=6379, db=0, password="robinn")
        self.channel = "notice"

    def pub(self, msg):
        self.__conn.publish(self.channel,msg)
        return True

    def sub(self):
        pub_obj = self.__conn.pubsub()
        pub_obj.subscribe(self.channel)
        pub_obj.parse_response()
        return pub_obj