from tool import *
while True:
    show_menu()
    operation=int(input("请输入您的操作："))
    print("您选择的操作是：%s"%operation)
    if operation==1:  #添加名片操作
        add_Info()
    elif operation ==2:  # 显示全部操作
        show_all()
    elif operation == 3:  #查看名片操作
        find_Info()
    elif operation == 0:  #退出系统
        print("退出系统")
        break
    else:
        print("输入错误，请重新输入")
        continue

