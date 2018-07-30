class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name+" is now sitting")
    def roll_over(self):
        print(self.name+' rolled over!')
my_dog=Dog('wille',6)
my_dog1=Dog('zzz',7)
my_dog.sit()
my_dog.roll_over()

my_dog1.sit()
my_dog1.roll_over()
