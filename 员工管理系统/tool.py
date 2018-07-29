employee=[]  #存储输入的所有员工信息
target_Info={}   #存储查找的员工信息
need_change_user={}  #存储需要修改的员工
def show_menu():
    print("*"*30)
    print("    欢迎使用员工管理系统  ")
    print("1、添加员工信息    2、删除员工信息")
    print("3、修改员工信息    4、显示所有信息")
    print("        5、退出员工系统         ")
    print("*"*30)

def add_Info():
    print("请根据提示添加信息：")
    id=input("请输入编号：")
    name=input("请输入姓名：")
    salary=input("请输入工资：")
    sex=input("请输入性别：")
    employee.append({"id":id,"name":name,"salary":salary,"sex":sex})
    print("添加%s的信息成功"%name)
    print(employee)


def del_Info():
    if len(employee)>0:
        print("请输入你要删除的员工编号：")
        find_id=input()
        for find in employee:
            if find_id==find["id"]:
                global target_Info
                target_Info=find
                employee.remove(target_Info)
                print("删除成功！")
    else:
        print("信息系统为空！")


def show_all():
    print("显示所有员工信息")
    if len(employee)==0:
        print("当前信息系统中信息为空")
    show_title()
    for i in employee:
        print("%s\t\t%s\t\t%s\t\t%s" %(i["id"],i["name"],i["salary"],i["sex"]))
    print("-"*30)



def change_Info():
    print("功能：修改员工信息")
    if len(employee)>0:
        employee_id = input("请输入您要查找员工的id：")
        for I in employee:
            if employee_id==I["name"]:
                print("找到了")
                show_title()
                print("%s\t\t%s\t\t%s\t\t%s" %
                      (I["id"], I["name"], I["salary"], I["sex"])
                      )
                global target_Info  #使用的是全局的变量
                target_Info = I #查到的信息放入全局变量target_Info中
                deal()
                break
        else:
            print("没有找到该信息！")
    else:
        print("列表中没有信息！")


def deal():
    while True:
        print("请选择你要对信息的操作：1、修改 2、删除、3、返回")
        choice=input()
        if choice == '1':   #修改信息
            update()
            break
        elif choice == '2':  #删除信息
            employee.remove(target_Info)
            print("删除成功")
            break
        elif choice == '3':   #返回
            break
        else:
            print("选择错误，请重新选择")

def update():
    target_Info["id"] = input("请输入编号：")
    target_Info["name"] = input("请输入名字：")
    target_Info["salary"] = input("请输入工资：")
    target_Info["sex"] = input("请输入性别：")


def show_title():
    print("id\t\t姓名\t\t工资\t\t性别")
    print("*"*30)