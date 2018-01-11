#!/user/bin/python
# _*_ coding:utf-8 _*_

if __name__ == "__main__":

    list1 = {12, 3, 51, 45, 78, 100,11}
    list2 = []
    list3 = []

    while len(list1)>0:
        number = list1.pop()
        if number%2 == 0:
            list2.append(number)
        else:
            list3.append(number)
    print(list2)
    print(list3)

    list2.sort()
    print(list2)

    list3.sort()
    print(list3)


    count = 0
    while count < 5:
        print("cnt: "+str(count))
        count += 1
    else:
        print(">: "+str(count))

    # while True:
    #     print("true")

    i = 1
    while i<9:
        i += 1
        if i%2 == 0:
            continue
        print(i)


    n = 0
    while n<10:
        n += 1
        if n%2 == 0:
            break
        print(n)

    # while (n) : print("loading...")