#!/usr/bin/python
# _*_ coding:utf-8 _*_
import Onsm
class child(Onsm.Ons):
    age = 20
    def __init__(self):
        child.age = child.age+50
    def showXi(self):
        print(child.age)
    def showinfo(self):
        print("调用了子类的showinfo()")


oneobj = Onsm.Ons("robs","female")
oneobj.showinfo()
oneobj.showcnt()
oneobj.showselfInfo()
Onsm.Ons.cnt = Onsm.Ons.cnt+10
print(Onsm.Ons.cnt)

oneobj.name = "doxxxx"
print(oneobj.name)
print(oneobj.__dict__)
print(oneobj.__doc__)
print(oneobj.__class__)


print("#####################")
print(Onsm.Ons.__module__)
print(Onsm.Ons.__dict__)
print(Onsm.Ons.__name__)
print(Onsm.Ons.__doc__)
print(Onsm.Ons.__bases__)
print("#####################")

childobj = child()
childobj.showXi()
print(child.age)
print(child.cnt)
childobj.showcnt()
childobj.showselfInfo()
childobj.showinfo()