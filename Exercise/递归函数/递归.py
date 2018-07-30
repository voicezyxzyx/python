'''
方式：
写出临界条件
找这一次和上一次的关系
假设的当前函数已经能用，调用自身计算上一次的结果，再求出本次结果

'''
def sum(n):
    sum=0
    for x in range(1,n+1):
        sum+=x
    return sum

print(sum(3))




















