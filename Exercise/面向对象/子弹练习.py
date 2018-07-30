#弹夹
class BulletBox(object):
    def __init__(self,count):
        self.bulletCount=count
#枪
class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox=BulletBox
    def shoot(self):
        if self.bulletBox.bulletCount==0:
            print("子弹打光了")
        else:
            self.bulletBox.bulletCount-=1
            print("子弹还剩余%d发" %self.bulletBox.bulletCount)
#人
class Person(object):
    def __init__(self,gun):
        self.gun=gun
    def fire(self):
        self.gun.shoot()
    def FillBulletBox(self,count):
        self.gun.BulletBox.bulletCount=count()

BulletBox=BulletBox(5)

gun=Gun(BulletBox)

per=Person(gun)
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.FillBulletBox(5)
