import functools
#把一个参数固定，形成一个新的函数
int3=functools.partial(int,base=16)
print(int3("1010"))
def int2(str,base=2):
    return int(str,base)
print(int2("0101"))

