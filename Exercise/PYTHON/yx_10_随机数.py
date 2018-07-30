# coding:utf-8
import random

a = random.randint(0, 99)
b = int(input("请输入你猜的数："))
print(a)
if a == b:
    print("猜对了")

else:
    print("猜错了")
    print(a)

