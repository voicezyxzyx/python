'''
self代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表那个对象

self._class_ 代表类名
'''
class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat "+ food)
    def say(self):
        print('My name is %s,i am %d years old' %(self.name,self.age))
    def __init__(self,name,age,height,weight):
        print(name,age,height,weight)
        # 定义属性
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
#self不是关键字 换成其他标识符也是可以的，但是一般都是用self。

per=Person('zyx',20,170,160)
per.say()

per2=Person('zzz',25,180,160)
per2.say()