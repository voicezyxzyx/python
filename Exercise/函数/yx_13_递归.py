# import sys
# a=1
# b=2
#
# s=a+b
# sys.setrecursionlimit(2000)  #可以限制递归次数
#
# def sum(s):
#     print(s)
#     sum(s+1)
# sum(s)
def s(n):
    a=int(n/2)
    if a==0:
        return 0
    print(a)
    s(a)
s(10)
