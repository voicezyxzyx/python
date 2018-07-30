#不同的类型用加法会有不同的解释
print(1+2)
print('1'+'2')

class Person(object):
    def __init__(self,num):
        self.num=num
    def __add__(self, other):
        return Person(self.num+other.num)
    def __str__(self):
        return 'num=' + str(self.num)
per1=Person(1)
per2=Person(2)
print(per1+per2) # ==>print(per1.__add__()per2)