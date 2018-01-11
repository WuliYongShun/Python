#!/usr/bin/python
# _*_ coding:utf-8 _*_

if __name__ == "__main__":
    # s = range(20)
    # for n in s:
    #     print n

    list1 = ["app","nodejs","webkit"]
    for line in range(len(list1)):
        print(list1[line])

    rows = int(raw_input('输入行数：'))
    for i in range(0, rows):
        for k in range(0, 2 * rows - 1):
            if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
                print " * ",
            elif i == rows - 1:
                if k % 2 == 0:
                    print " * ",
                else:
                    print "   ",
            else:
                print "   ",
        print "\n"

    for i in range(1,11):
        for k in range(1,i):
            print k,
            k +=1
        i +=1
        print "\n"