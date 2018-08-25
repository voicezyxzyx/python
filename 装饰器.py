# def line_conf(a,b):
#     def line(x):
#         return a*x+b
#     return line
#
# line1=line_conf(1,2)
# ret=line1(5)
# print(ret)

def w1(func):
    def inner():
        print("-----验证权限-----")
        func()
    return inner
def f1():
    print('11111111111')
def f2():
    print('22222222222')

# res=w1(f1)
# res()
#
# res2=w1(f2)
# res2()

f1=w1(f1)
f1()