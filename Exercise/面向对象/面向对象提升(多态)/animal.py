class Animal(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name + " 吃")
    def run(self):
        print(self.name + " 跑")