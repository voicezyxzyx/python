class Person(object):
    name="person"
    def __init__(self,name):
        #对象属性
        self.name=name
print(Person.name)
#对象属性的优先级高于类属性
per=Person("tom")
per.age=20 #只针对当前对象生效。对于类创建的其他对象没有作用
print(per.age)
print(per.name)


#删除对象中的name属性，在调用会使用到同名的类属性
del per.name
print(per.name)

#注意：千万不要将对象属性与类属性重名，因为对象属性会
#屏蔽掉类属性。但是当删除对象属性后，在使用又能使用类属性了。