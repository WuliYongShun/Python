#!/usr/bin/python
# _*_ coding:utf-8 _*_

tpl = ()
tpl = (10,)
print(tpl)

tpl = (10,20,30,54,50,90,45)
print(tpl)
del tpl

tpl = [11,22,33,44,56,89]
print(tpl)

x,y = 45,56
print(x)
print(y)

print(tpl+[01,02,03])
print(tpl * 2)
print( 22 in tpl)
print(len(tpl))
print("================")
for x in tpl:
    print(x)