#!/usr/bin/python
# _*_ coding:utf-8 _*_

if __name__ == "__main__":

    list = "string"
    print(list[0])
    print(list[-1])

    print("string"[2])

    number=[1,2,3,4,5,6,7,8,9,10]
    print(number[2:4])
    print(number[0])
    print(number[-1])
    print(number[-4:-1])
    print(number[-4:])
    print(number[:5])
    print(number[0:10:3])
    print(number[10:0:-1])
    print(number[10:0:-2])

    number2 = [20,50,80]
    print(number+number2)


    print(number2*2)

    if 20 in number2:
        print(True)

    print(max(number))
    print(min(number))
    print(len(number))