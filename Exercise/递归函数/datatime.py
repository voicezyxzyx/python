'''datatime是基于time进行了封装，提供了可使用的函数，
datetime模块的接口更直观，更容易调用

模块中的类：
datetime    同时有时间和日期
timedelta  主要用于计算时间的跨度
tzinfo      时区相关
time        只关注时间
date        只关注日期
'''
import datetime
#获取当前的时间
d1=datetime.datetime.now()
print(d1)
#获取指定的时间
d2= datetime.datetime(1999,10,1,10,10,10)
print(d2)

#将时间转为字符串
d3=d1.strftime("%Y-%m-%d %H:%M:%S")  #%H:%M:%S  ==>>   %X
print(d3)
print(type(d3))

#将字符串转为datetime对象
#注意：转换的格式要和字符串一致
d4=datetime.datetime.strptime(d3,"%Y-%m-%d %H:%M:%S")
print(d4)
print(type(d4))


d5= datetime.datetime(1999,10,1,10,10,10)
d6=datetime.datetime.now()
d8=datetime.datetime(2000,10,1,10,10,10)
d7=d6-d5
d9=d8-d5
print(d7)
print(d9)




