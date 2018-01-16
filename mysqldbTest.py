#!/usr/bin/python
# _*_ coding:utf-8 _*_

if __name__ == "__main__":
    import MySQLdb
    db = MySQLdb.connect("127.0.0.1","root","root","mysql")
    cursor = db.cursor()
    sql = "select Host,User,Password from user"
    cursor.execute(sql)
    # data = cursor.fetchone()
    # print(data)

    datas = cursor.fetchall()
    for row in datas:
        print(row[0]+" | "+row[1]+" | "+row[2])