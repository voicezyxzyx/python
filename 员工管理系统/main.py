from tool import *
while True:
    show_menu()
    operation=int(input("请输入您的操作："))
    if operation==1:  #添加员工信息
        add_Info()
    elif operation ==2:  # 删除员工信息
        del_Info()
    elif operation == 3:  # 修改员工信息
        change_Info()
    elif operation == 4:  # 显示所有信息
        show_all()
    elif operation == 5:  # 退出员工系统
        print("退出员工系统")
        break
    else:
        print("输入错误，请重新输入")
        continue

