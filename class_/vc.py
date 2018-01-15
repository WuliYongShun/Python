#!/usr/bin/python
# _*_ coding:utf-8 _*_

class vc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return vc(self.a + other.a,self.b + other.b)
    def __str__(self):
        return "vc: a=" + str(self.a) + " b=" + str(self.b)

if __name__ == "__main__":
    vc1 = vc(1, 2)
    vc2 = vc(3, 5)
    print(vc1 + vc2)