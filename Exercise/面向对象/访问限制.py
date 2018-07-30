class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat "+ food)
    def __init__(self,name,age,height,weight):
        # 定义属性
        self.name=name
        self.age=age
        self.height=height
        self.__weight=weight
    #通过内部的方法，去修改私有属性
    #通过自定义的方法实现私有属性的赋值和取值
    def setweight(self,weight):
        self.__weight=weight
    def getweight(self):
        return self.__weight
per=Person("zzz",22,180,60)
# per.age=20
# print(per.age)

#如果要让内部的属性不被外部直接访问  在外部直接访问修改，
#信息不安全了。
'''
要让内部的属性不被外部直接访问，在属性前加两个
下划线(__weight),在python中如果在属性前加两个下滑线，
这个属性就编程了私有属性
'''
#外部使用  不能访问到
#print(per.__weight)
 #内部可以访问

per.setweight(100)
print(per.getweight())

#在python中，_xxx 变量，这样的实例变量外部是可以访问到的。
#但是按照约定的规则，当我们看到这样的变量时，意思是：虽然我可以被访问，
#但是请把我视为私有变量，不要直接访问我。