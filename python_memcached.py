#! /usr/bin/python
# _*_ coding:utf-8 _*_

import memcache

if __name__ == "__main__":

    mc = memcache.Client(["192.168.0.104:11211"], debug=True)
    mc.flush_all()
    # mc.set("name", "robinn")
    # result = mc.get("name")
    # print(result)

    mc.add("date", "2018")
    result = mc.get("date")
    mc.replace("date", "2020")
    result = mc.get("date")

    mc.set("name", "robinn")
    result = mc.get("name")
    mc.set_multi({"name": "xili", "sex": "male", "addr": "sichuan chengdu"})
    result1 = mc.get("name")
    print("result: ", result, result1)
    print("name: "+mc.get("name"))
    print("sex: "+mc.get("sex"))
    print("addr: "+mc.get("addr"))

    result2 = mc.get_multi(["name", "sex", "addr"])
    print(result2)

    mc.delete("date")
    print(mc.get("date"))
    print(mc.get("addr"))

    mc.delete_multi(["name", "sex", "addr"])

    print(mc.get_multi(["name", "sex", "addr"]))

    mc.set("city", "chengdu")
    print(mc.get("city"))

    mc.append("city"," china")
    print(mc.get("city"))

    mc.prepend("city", "sichuan ")
    print(mc.get("city"))

    mc.set("num", 5)
    print(mc.get("num"))

    mc.incr("num",10)
    print(mc.get("num"))

    mc.decr("num", 2)
    print(mc.get("num"))