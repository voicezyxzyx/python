Info_list=[]  #存储输入的所有名片信息
target_Info={}   #存储查找的名片信息
def show_menu():
    print("*"*30)
    print("    欢迎使用名片管理系统  ")
    print("1、添加名片    2、显示全部")
    print("3、查看名片    0、退出系统")
    print("*"*30)
def add_Info():
    print("请根据提示添加信息：")
    names=input("请输入名字：")
    age=input("请输入年龄：")
    sex=input("请输入性别：")
    address=input("请输入住址：")
    Info_list.append({"name":names,"age":age,"sex":sex,"address":address})
    print("添加%s的信息成功"%names)
    print(Info_list)

def show_all():
    print("显示所有名片信息")
    if len(Info_list)==0:
        print("当前信息系统中信息为空")
    show_title()
    for i in Info_list:
        print("%s\t\t%s\t\t%s\t\t%s" %(i["name"],i["age"],i["sex"],i["address"]))
    print("-"*30)


def find_Info():
    print("功能：查找要寻找的信息")
    if len(Info_list)>0:
        find_name = input("请输入您要查找名片的名字：")
        for Info in Info_list:
            if find_name==Info["name"]:
                print("找到了")
                show_title()
                print("%s\t\t%s\t\t%s\t\t%s" % (
                    Info["name"], Info["age"], Info["sex"], Info["address"]
                ))
                global target_Info  #使用的是全局的变量
                target_Info = Info #查到的信息放入全局变量target_Info中
                deal()
                break
        else:
            print("没有找到该信息！")
    else:
        print("列表中没有信息！")



def show_title():
    print("姓名\t\t电话\t\tqq\t\t邮箱")
    print("*"*30)

def deal():
    while True:
        print("请选择你要对信息的操作：1、修改 2、删除、3、返回")
        choice=input()
        if choice == '1':   #修改信息
            update()
            break
        elif choice == '2':  #删除信息
            del_Info()
            #Info_list.remove(target_Info)
            print("删除成功")
            break
        elif choice == '3':   #返回
            break
        else:
            print("选择错误，请重新选择")

def update():
    target_Info["name"] = input("请输入姓名：")
    target_Info["age"] = input("请输入年龄：")
    target_Info["sex"] = input("请输入性别：")
    target_Info["address"] = input("请输入住址：")
def del_Info():
    Info_list.remove(target_Info)

