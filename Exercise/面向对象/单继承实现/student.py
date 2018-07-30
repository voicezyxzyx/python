from person import Person

class Student(Person):
    def __init__(self,name,age,__salary,stuId):
        #调用父类中的__init__
        super(Student, self).__init__(name,age,__salary)
        #子类可以拥有自己特别的属性
        self.stuId=stuId


