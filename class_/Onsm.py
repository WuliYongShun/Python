#!/usr/bin/python
# _*_ coding:utf-8 _*_

class Ons:
    cnt = 0

    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        Ons.cnt += 1

    def showinfo(self):
        print("name："+self.name+" || sex:"+self.sex)
        Ons.cnt += 1

    def showcnt(self):
        print("cnt: "+str(self.cnt))

    def showselfInfo(self):
        print(self.__class__)
        print(self.__dict__)