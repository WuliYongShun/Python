#!/usr/bin/python
# _*_ coding:utf-8 _*_



# try:
#     f = open("iX.txt", "r")
#     f.write("line")
# except IOError, Argument:
#     print("error", Argument)
# finally:
#     print("final")
#
# try:
#     f = open("sx.txt", "r")
#     f.read()
# except:
#     print("sdfas")
# else:
#     print("f.read")


try:
    raise IOError("io error")
except:
    print("io error")

exec('''for x in range(1,20):
    print x
''')

exec("print('dosx')")