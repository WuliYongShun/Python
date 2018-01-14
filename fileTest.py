#!/usr/bin/python
# _*_ coding:utf-8 _*_

import os

# file = open("info.txt", "wb")
# file.write("hellojava")
#
# file.close()
# print(file.closed)
# print(file.mode)
# print(file.name)
# print(file.softspace)


file = open("info.txt", "r")
line = file.read(2)
print(line)
position = file.tell()
print("position :", position)

file.seek(position)
x = file.read()
print(x)

file.close()

# os.rename("info.txt","t.txt")
# os.remove("t.txt")