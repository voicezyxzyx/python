'''
人
类名：Person
属性：姓名、身份证号、电话 、 卡
方法：

卡
类名：Card
属性：卡号、密码、余额
方法：

提款机
类名:ATM
属性：
方法：开户、查询、取款、存款、转账、改密、锁定、解锁、补卡、销户、退出

界面
类名：admin
属性：
行为：管理员界面、 管理员验证、系统功能界面
'''
from admin import  Admin
from atm import ATM
def main():

    admin = Admin()#管理员对象
    admin.printAdminView() #管理员开机
    if admin.adminOperation():
        return -1

    atm=ATM()

    while True:
        #等待用户操作
        admin.sysFunctionView()
        option=input("请输入你的操作:")
        if option=='0':
            atm.createUser()
        if option=='1':
            pass
        elif option=='2':
            pass
        elif option=='3':
            pass
        elif option=='4':
            pass
        elif option=='5':
            pass
        elif option=='6':
            pass
        elif option=='7':
            pass
        elif option=='8':
            pass
        elif option=='9':
            if admin.adminOperation():
                return -1

if __name__=="__main__":
    main()
