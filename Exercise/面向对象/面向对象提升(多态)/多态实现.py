'''
多态：一种事物的多种形态
最终目标：人可以喂任何一种动物

'''
from cat import cat
from mouse import mouse
from person import person

tom=cat("tom")
jerry=mouse("jerry")
tom.eat()
jerry.eat()
print(tom.name)

#定义一个人，喂动物
per=person()
per.feedAnimal(tom)
per.feedAnimal(jerry)

per.findAnimal(tom)
#思考：100种动物，也都有name属性和eat方法
#可创建一个父类，都继承自父类。


#定义一个人类，可以喂猫和老鼠吃东西