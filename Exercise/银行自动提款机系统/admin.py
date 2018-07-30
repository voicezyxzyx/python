class Admin(object):
    admin="admin"
    passwd="1"
    def printAdminView(self):
        print("*****************************")
        print("                             ")
        print("       欢迎登录银行系统        ")
        print("*****************************")
    def sysFunctionView(self):
        print("*****************************")
        print("    开户（0）       查询（1）       ")
        print("    取款（2）       存款（3）       ")
        print("    转账(3)         改密(4)        ")
        print("    锁定(5)         解锁(6)        ")
        print("    补卡(7)         销户（8）      ")
        print("           退出（9）               ")
        print("*****************************")
    def adminOperation(self):
        inputadmin = input("请登录管理员账户：")
        if self.admin != inputadmin:
            print("账号输入有误")
            return -1
        inputpasswd = input("请输入管理员密码：")
        if self.passwd != inputpasswd:
            print("密码输入错误")
            return -1
        print("操作成功")
        return 0
