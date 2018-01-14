#!/usr/bin/python
# _*_ coding:utf-8 _*_

import os
import sys
print("###############################")
print(os.environ)
print(os.environ["GOPATH"])
print(os.getcwd())
os.system("ls -al")
print("###############################")
print(sys.argv)
print(sys.stdin)
print(sys.stdout)
print(sys.stderr)
print(sys.platform)
print(sys.path)
print(sys.path_hooks)
print(sys.modules)
print(sys.version)
# x = sys.stdin.readline()
# print("write: "+x)
# sys.exit()
print("###############################")