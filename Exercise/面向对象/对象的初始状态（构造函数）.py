class Person(object):
    name='zyx'
    age=20
    height=170
    weight=160
    def run(self):
        print("run")
    def eat(self,food):
        print("eat "+ food)

    def __init__(self,name,age,height,weight):
        print(name,age,height,weight)
        # 定义属性
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
# per=Person()
# print(per.name,per.age,per.height,per.weight)
'''
构造函数：_init_()  在使用类创建对象的时候自动调用
'''
per=Person("zzz",22,180,60)

per2=Person("xxx",20,170,50)



