import itertools

mylist=list(itertools.permutations([1,2,3,4],3))
print(mylist)
print(len(mylist))


'''
排列的可能次数：
比如：4个数选3个数  24种
     4个数选2个数   12种
     4个数选1个数   4种
     n个数选m个数   n！/（m-n）！

'''