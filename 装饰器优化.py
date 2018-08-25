
def w1(func):
    def inner():
        print("-----验证权限-----")
        if True:
            func()
        else:
            print("没有权限")
    return inner
@w1
def f1():
    print('11111111111')
@w1
def f2():
    print('22222222222')

f1()
f2()