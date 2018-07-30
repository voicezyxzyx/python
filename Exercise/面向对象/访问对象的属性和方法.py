

class Person(object):
    def run(self):
        print("run")
    def eat(self,food):
        print("eat "+ food)
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经将大象装进冰箱")
    def close(self):
        print("我已经关闭了冰箱")
per=Person()
print(id(per))
'''
访问属性
格式：
对象名.属性名
赋值：对象名.属性名=新值
'''
per.name='zyx'
per.age=20
per.height=170
print(per.name,per.age,per.height)

'''
访问方法
格式：对象名.方法名（参数列表）

'''
per.openDoor()
per.fillEle()
per.close()
per.eat("apple")