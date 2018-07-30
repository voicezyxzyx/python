'''
重写：将函数重新定义写一遍
__repr__()
__str__()  是给机器用的，在python解释器里面直接敲对象在回车
后调用的方法   （黑屏中断中使用）
注意：在没有str时，且有repr.str=repr
'''
class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat "+ food)
    def __init__(self,name,age,height,weight):
        #print(name,age,height,weight)
        # 定义属性
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

#在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法
    def __str__(self):
        return '%s   %d-%d-%d\n' %(self.name,self.age
                               ,self.height,self.weight)
per=Person('aaaa',1,2,3)
per2=Person('bbbb',2,2,2)
per3=Person('cccc',3,3,3)
#print(per.name,per.age,per.height,per.weight)
print(per,per2,per3)

#优点：当一个对象的属性值有很多，并且都需要打印，重写了__str__方法后，
#简化了代码。



