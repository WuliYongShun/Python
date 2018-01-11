#!/usr/bin/python
# _*_ coding:utf-8 _*_

dict = {"uname":"robs","usex":"male","uaddr":"sichuang chengdu","key":"asdfasdfl4sfda4s5"}
print(dict)

print(dict["usex"])
# del dict["usex"]
print(dict)

print(dict["key"])


print("++++++++++++++++++++++++++++++")
s = dict.copy()
for x in dict:
    print(dict[x])
print("++++++++++++++++++++++++++++++")

print(s)