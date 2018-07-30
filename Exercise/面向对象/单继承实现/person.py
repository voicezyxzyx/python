class Person(object):
    def __init__(self,name,age,__salary):
        self.name=name
        self.age=age
        self.__salary=__salary  #父类私有的属性，子类不能继承

    def setSalary(self,salary):
        self.__salary = salary
    def getsalary(self):
        return self.__salary

    def run(self):
        print("run")
    def eat(self,food):
        print("eat "+food)