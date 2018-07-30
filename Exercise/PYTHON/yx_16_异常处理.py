'''
当程序遇到错误时，不让程序结束，让程序越过错误继续向下执行
'''
#  try...except...else
'''
格式：
try：
    语句a
except 错误码 as e：
    语句1
except 错误码 as e：
    语句2
......
except 错误码 as e：
    语句n
else:
    语句e
注意：else语句可有可无


'''
try:
    print(3/0)
except ZeroDivisionError as e:
    print("除数为0")

print("222222222")
