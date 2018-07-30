import time

#print(time.localtime(time.time()))
#print(time.strftime('%Y-%m-%d',time.localtime(time.time()))) #输出结果 2018-06-06
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  #输出结果 2018-06-06 17:49:52
