#!/usr/bin/python
# _*_ coding:utf-8 _*_

import itertools
counter = itertools.count(start=13)
print(counter.next())
print(counter.next())

lists = ["11", "22", "33", "44"]
print(lists)
list_iter = iter(lists)
print(list_iter.next())
print(list_iter.next())