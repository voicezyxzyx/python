'''
人
类名：person
属性：gun（枪）
行为：fire（开火）
枪
类名：Gun
属性：bulletBox
行为：shoot

弹夹
类名：bulletBox
属性：bulletCount
行为
'''
#弹夹
class BulletBox(object):
    def __init__(self,count):
        self.bulletCount=count  #子弹数量
#枪
class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox=bulletBox   #枪拥有弹夹
    def shoot(self):
        if self.bulletBox.bulletCount==0:
            print("没有子弹了")
        else:
            self.bulletBox.bulletCount-=1
            print("剩余子弹%d 发" %(self.bulletBox.bulletCount))
#人
class Person(object):
    def __init__(self,gun):
        self.gun=gun
    def fire(self):
        self.gun.shoot()
    def fillBullet(self,count):
        self.gun.bulletBox.bulletCount=count()

#弹夹
bulletBox=BulletBox(5)

#枪
gun=Gun(bulletBox)

#人
per=Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.fire()
per.fillBullet(5)

per.fire()