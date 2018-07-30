from card import Card
from  user import User
import random
class ATM():
    def __init__(self):
        self.allUsers={}
    def createUser(self):
        '''向用户字典中添加一对键值对'''
        name=input("请输入您的姓名：")
        idCard=input("请输入您的身份证号码：")
        phone=input("请输入您的电话号码：")

        prestoreMoney=int(input("请输入预存金额："))
        if prestoreMoney<0:
            print("预存款有误，开户失败！")
            return -1
        onePasswd=input("请设置密码：")
        if not self.check(onePasswd):
            print("密码输入错误，开户失败")

        cardID=self.randomCardId()
        card=Card(cardId,onePasswd,prestoreMoney)
    #随机生成卡号
    def randomCardId(self):
        str=''
        for i in range(6):
            ch = chr(random.randrange(ord('0'),ord('9')+1))
            str+=ch
            return str



    def searchUserInfo(self):
        pass
    def getMoney(self):   #取款
        pass
    def saveMoney(self):
        pass
    def transferMoney(self):
        pass
    def changePasswd(self):
        pass
    def lockUser(self):
        pass
    def unlockUser(self):
        pass
    def newCard(self):
        pass
    def killUser(self):
        pass

    def checkPasswd(self,realPasswd):
        for i in range(3):

            tempPasswd=input("请输入密码：")
            if tempPasswd==realPasswd:
                return 0
        return False