'''
析构函数：__del__() 两个下划线  释放对象是自动调用
'''
class Person(object):
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
    def __del__(self):
        print('这里是析构函数')

per=Person('zzzz',20,180,160)

#释放对象
#del per

#对象释放以后就不能再访问
#print(per.name)

#在函数里定义的对象，会在函数结束时自动释放，这样可以用来减少
#内存空间的浪费
def func():
    per2=Person('aaa',1,1,1)
func()









