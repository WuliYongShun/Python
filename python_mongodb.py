#!/usr/bin/python
# _*_ coding:utf-8 _*_

import pymongo

if __name__ == "__main__":
    #创建链接
    mc = pymongo.MongoClient("mongodb://192.168.0.104:27017")

    #获取数据库
    db = mc.users

    #获取集合
    col = db.infos

    #插入文档
    #col.insert({"name": "zhongmama", "age": "23"})


    #遍历集合文档
    for line in col.find():
        for x in line:
            print(str(x)+":"+str(line[x]))
        print("======================")

    #文档个数
    cnt = col.count()
    print(cnt)


    #查询一个文档
    lineme = col.find_one({"size":"20pt"})
    keys = lineme.keys()
    for i in keys:
        print(str(i)+":"+str(lineme[i]))