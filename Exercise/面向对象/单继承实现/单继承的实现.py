from student import Student
from person import Person
stu=Student("zyx",20,10000,541513430253)
print(stu.name,stu.age,stu.stuId)
#print(stu.stuId)
stu.run()
stu.eat('banana')

#父类的对象
per1=Person('zzzz',20,'50000')
print(per1.name,per1.age,per1.getsalary)

