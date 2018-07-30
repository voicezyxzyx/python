#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


######查询操作######
def select():
    name = input("请输入要查询的员工姓名（例如：Alex）:").strip()  # 空格分段
    flag = False  # 判断条件
    with open("info.txt", "r")as reads:
        for line in reads:  # 遍历
            if line.split()[0] == name:  ###[alex 1000],[Yuan 9999][0]==name
                flag = True
                print("员工信息", name, line.split()[1])  # [alex 1000][1]==1000
            else:  ###跳过，知道遍历结束为查询到，执行if not flag的判断
                continue
    if not flag:
        print("\033[31;1m未找到%s员工信息\033[0m" % name)


#####修改操作######
def revise():
    reff = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：").strip()  ##reff: "Alex 10000"
    reff_list = reff.split()  # reff_list : ['Alex','1000']  class list
    flag = False
    with open("info.txt", "r")as reads, open("info", 'w')as writes:
        for line in reads:  # 遍历  line "alex 10000'
            if line.split()[0] == reff_list[0]:  ##line "alex" == reff_list ["alex",""]
                writes.write(reff + "\n")  # 修改成功，True
                flag = True
            else:  ###
                writes.write(line)

    os.remove("info_bak.txt")
    os.rename("info.txt", "info_bak.txt")
    os.rename("info", "info.txt")
    if flag:
        print("修改成功")
    else:
        print("未找到需要修改的\033[31;1m%s\033[0m员工信息" % reff)


def app():
    rtff = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）：").strip()  ##以空格作为分隔符
    rtff_list = rtff.split()
    flag = False
    with open("info.txt", "r")as reads:
        for line in reads:
            if line.split()[0] == rtff_list[0]:  ##当相同时，print 以重复。
                flag = True
            else:
                continue
    if flag:
        print("\033[31;1m该%s用户已存在\033[0m" % rtff)
    else:
        with open("info.txt", "a") as writes:
            writes.write("\n" + rtff)
        print("增加成功")


######删除操作#######
def delete():
    name = input("请输入要删除的员工姓名（例如：Alex）:").strip()
    flag = False
    with open("info.txt", "r") as reads, open("info", "w")as writes:
        for line in reads:
            if line.split()[0] == name:
                flag = True
                continue
            else:
                writes.write(line)
    os.remove("info_bak.txt")
    os.rename("info.txt", "info_bak.txt")
    os.rename("info", "info.txt")
    if flag:
        print("删除成功")
    else:
        print("未找到需要修改的\033[31;1m%s\033[0m员工信息" % name)


#####菜单#####
def main():
    menu = {
        "1": select,
        "2": revise,
        "3": app,
        "4": delete,
        "5": exit,
    }
    while True:
        print("""
        请选择：
            1,查询员工信息
            2,修改员工工资
            3,增加员工信息
            4,删除员工信息
            5,退出工资系统
        """)
        choice = input(">>>").strip()  ##choice :"1,2,3,4"
        if choice in menu:  ###这里是menu字典的key值等于choice
            menu[choice]()  ###进入对应的value


if __name__ == "__main__":
    main()