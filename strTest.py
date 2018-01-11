#! /usr/bin/python
# _*_ coding:utf-8 _*_

if __name__ == "__main__":
    str = "lovepythoner"
    print(str)
    print(str[0])
    print(str[0:5])

    users = ["zys", "zhuli", "robs", "domls"]
    print(users)
    print(users[0])

    for user in users:
        print("userName: "+user )

    nums = [20,60,10,5,12]
    print(nums+users)
    print(nums * 2)
    nums.sort()
    print(nums)

    scripts = ("java", "js", "vbs", "dart", "php")
    print(scripts)

    users[0] = ".net"
    print(users)

    for s in scripts:
        print(s)

    print(type(scripts))

    # print("tuple" in str(type(scripts)))

    # if type(scripts) in "tuple":
    #     print(True)
    #
    # else:
    #     print(False)


    dis = {"one", "dss", "sadf"}

    for d in dis:
        print(d)

    dism = {"1":"zhangweis", "2":"domlso"}


    print(dism.keys())
    print(dism.values())

    if "java" in scripts:
        print(True)
    else:
        print(False)

    if not ("sdfa" not in scripts):
        print(True)
    else:
        print(False)

    if (scripts[0] == "java"): print("true java....")

    length = len(scripts)
    print(length)

    print(len(dis))