#导入随机数的包
import random
a=int(input("请输入您要出的拳 石头（1）/剪刀（2）/布（3）"))
#随机输出一个整数
computer = random.randint(1,3)
#("请输入您要出的拳 石头（1）/剪刀（2）/布（3）")
print("玩家选择的拳头是 %d  电脑出的拳是 %d" % (a,computer))
#比较胜负
#1.石头胜剪刀
#2.剪刀胜布
#3.布胜石头
if(a==1 and computer==2) or (a==2 and computer==3) or (a==3 and computer==1):
    print("恭喜玩家胜利")
#平局
elif a == computer:
    print("平局")
else:
    print("电脑胜利")