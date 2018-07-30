

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end='')
#         j+=1
#     i+=1
#     print()

# for i in range(1,6):
#     print("*"*i)


#一个学校，有3个办公室，现在有8位老师等待工位的分配
import random
office=[[],[],[]]
teacher=['a','b','c','d','e','f','g','h','i']
for name in teacher:
    index=random.randint(0,2)
    office[index].append(name)
print(office)



# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sit(self):
#         print(self.name+" is now sitting")
#     def roll_over(self):
#         print(self.name+' rolled over!')
# my_dog=Dog('wille',6)
# my_dog1=Dog('zzz',7)
# my_dog.sit()
# my_dog.roll_over()
#
# my_dog1.sit()
# my_dog1.roll_over()


class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("餐馆的名字是："+self.restaurant_name,"餐馆的类型是："+self.cuisine_type)
    def open_restanrant(self):
        print("餐馆正在营业！")
res=Restaurant("zzz","zz")
res.describe_restaurant()
res.open_restanrant()