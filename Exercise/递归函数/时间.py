import time
#返回当前时间的时间戳，浮点数形式，不需要参数
c=time.time()
print(c)

# #
#将时戳转为字符串将时间戳作为UTC时间元组
# t=time.gmtime(c)
# print(t)
#
#将时间戳转为当地时间元组
b=time.localtime(c)
print(b)
#
# #将本地时间元组转为时间戳
# m=time.mktime(b)
# print(m)
#
# #将时间元组转换为字符串
# s=time.asctime(b)
# print(s)
#

p=time.ctime(c)
print(p)
#获取系统当前时间(将时间元组转换成给定格式的字符串)
l=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(l)


m=time.strftime('%Y-%m-%d %X', b)
print(b)
