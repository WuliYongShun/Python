#!/usr/bin/python
# _*_coding:utf-8 _*_

def myfn2(str="world"):
    print(str)

def myfn1(str):
    print(str)

def myfn(arg1,*args):
    print(arg1)
    print("======")
    for m in args:
        print(m)

myfn1("hello")
myfn(10,12,23,56,89,466)
myfn2("sadfasdf")

def myfn3(name,age=20):
    print("uname: "+name)
    print("uage: " +str(age))

myfn3("robs",56)

sum = lambda a1,a2:a1+a2
n = sum(20.20,56)
print(n)
print(int(n))


def total(a,b):
    return a+b

print(total(1,56))



