class Student(object):
    def __init__(self,name,score):
        '''
    注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
    因此，在__init__方法内部，就可以把各种属性绑定到self，
    因为self就指向创建的实例本身。

    有了__init__方法，在创建实例的时候，就不能传入空的参数了，
    必须传入与__init__方法匹配的参数，但self不需要传，
    Python解释器自己会把实例变量传进去：
    '''
        self.name=name
        self.score=score
bart=Student('zyx',100)
print(bart.name)
print(bart.score)