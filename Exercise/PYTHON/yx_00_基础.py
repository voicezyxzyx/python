# print("life is so short you need python")
# print("hello meimei ")
# print("人生苦短  我用python")

# import keyword
# a=keyword.kwlist
# #for i in a:
# print("关键词有：%s \t"%a)

# UserName="zyx"
# age=20
# print("my name is %s,i am %d years old"%(UserName,age))

# tb_User=input("请输入账户名：")
# tb_Password=input("请输入密码：")
# print("该淘宝账号的用户名是%s,账号密码是%s"%(tb_User,tb_Password))

# apple_price=8.5
# apple_weigh=7.5
# sum=apple_price*apple_weigh
# print(sum)

# import datetime
# #print("当前年月日为：",datetime.date.today())
# print(datetime.date(1997,9,24))

# name="zyx "
# print(name*10)

# price=9.00
# weight=5.0
# money=price*weight
# print("总金额为：%.3f"%money)

# scale=10
# print('%2f%%' %scale)

# ojb=input("是否有对象 1（有对象） 0（无对象），请输入你的选择：")
# if ojb=='1':
#     print("嗯嗯")
# else:
#     print("给你介绍")

# for i in  range(1,11):
#     print("*"*i)
#     i+=1
#运行结果：
'''
*
**
***
****
*****
******
*******
********
*********
'''

# for a in range(1,11):
#
#     if a%2==0:
#         break
#     a += 1
#     print(a)

# print("请选择自己要添加的配料,Enter 'quit' when you finished")
# peiliao=''
# while peiliao !="quit":
#     peiliao=input()
#     if peiliao!='quit':
#         print("添加所选配料 %s到披萨里 " % peiliao)


# print("请输入你的年龄：")
# age=int(input())
# if age<3:
#     print("免费观影")
# elif age>=3 and age<=12:
#     print("票价为10美元")
# else:
#     print("票价为15美元")

unconfirmed_users={'zyx',"zzz",'zxcv'}
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    confirmed_users.append(current_user)
    for confirmed_user in confirmed_users:
        print(confirmed_user)
