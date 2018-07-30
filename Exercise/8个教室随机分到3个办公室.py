
#一个学校，有3个办公室，现在有8位老师等待工位的分配
import random
office=[[],[],[]]
teacher=['a','b','c','d','e','f','g','h','i']
for name in teacher:
    index=random.randint(0,2)
    office[index].append(name)
print(office)
