class Anmial(object):
    def run(self):
       print("Running")
class dog(Anmial):
    def run(self):
        print("dog is running")
    def eat(self):
        print("dog is eating")
class cat(Anmial):
    def run(self):
        print("cat is running")
    def eat(self):
        print("cat is eating")

def run_twice(anmial):
    anmial.run()
    anmial.run()

a = Anmial()
Dog = dog()
Cat = cat()

Dog.run()
Cat.run()
run_twice(a)

