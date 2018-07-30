import time

# 返回当前程序的cpu执行时间
# unix始终返回全部的运行时间
# windows从第二次开始，都是以第一次调用此函数开始时间戳为基数
a=time.clock()
print(a)
time.sleep(2)
b=time.clock()
print(b)


