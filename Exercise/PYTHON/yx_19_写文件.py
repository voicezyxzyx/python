import time
path=("D:\python\pycharm文件\PYTHON\测试.txt")
f=open(path,"r+",encoding="utf-8")
#写文件
# 1.将文件写入缓冲区
while True:

    f.write("zyx is a good man")
    time.sleep(0.001)
#2.刷新缓冲区，直接把缓冲区的内容立刻写入文件
#f.flush()

f.close()