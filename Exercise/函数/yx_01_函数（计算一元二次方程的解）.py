# #定义好函数之后，只表示这个函数封装了一段代码而已
# #如果不主动调用函数，函数是不会主动执行的
# def say_hello():
#
#     print("hello 1")
#     print("hello 2")
#     print("hello 3")
# say_hello()

#计算一元二次方程的解
import math
def quadratic(a,b,c):
    if not isinstance(a, (int, float)):
        raise TypeError('a is not a number')
    if not isinstance(b, (int, float)):
        raise TypeError('b is not a number')
    if not isinstance(c, (int, float)):
        raise TypeError('c is not a number')
    d=b*b-4*a*c
    if a==0:
        if b==0:
            if c==0:
                return "方程根为全体实数"
            else:
                return  "无根"
        else:
            x1=-c/b
            x2=x1
            return x1,x2
    else:
        if d<0:
            return "无根"
        else:
            x1=(-b+math.sqrt(d))/2/a
            x2=(-b-math.sqrt(d))/2/a
            return x1,x2
print(quadratic(1,7,5))
