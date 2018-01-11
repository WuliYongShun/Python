#!/usr/bin/python
# _*_ coding:utf-8 _*_

lists = ["a", "b", "c", "d"]

print(lists)
print(lists[2])

lists[2]="tree"
print(lists)

del lists[0]
print(lists)

print(lists+["1","2","3"])
print(lists * 3)
print(len(lists))

print("b" in lists)

for n in lists:
    print(n)

print(lists[-2])