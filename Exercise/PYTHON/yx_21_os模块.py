import os
#os.rename("yx_21_os.py","yx_21_os模块.py")

#运行shell命令
# os.system("write")  #打开写字板
# os.system("shutdown -s -t 500")  #关机  500是500秒后关机
# os.system("shutdown -a") #取消关机计划
#os.system("taskkill /f /im write.exe") #关闭后台应用


#有些方法存在于os中，有些方法存在于os.path中
#print(os.path.abspath("./文件写"))  #文件的绝对路径

#拆分路径
#path2=(os.path.split("D:\python\pycharm文件\PYTHON\文件写"))

#判断文件是否存在
# path2=(os.path.isfile("D:\python\pycharm文件\PYTHON\文件写.txt"))
# print(path2)

#获取文件大小(字节)
print(os.path.getsize("D:\python\pycharm文件\PYTHON\文件写.txt"))













