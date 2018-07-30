import  itertools

mylist=list(itertools.combinations([1,2,3,4,5],4))
print(mylist)

'''

5个数选5个数  1种结果
5个数选4个数  5种结果
5个数选3个数  10种结果
5个数选2个数  10种结果
m个数选n个数  m！/(n！(m-n)！)
'''