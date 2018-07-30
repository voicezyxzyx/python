import os

def getAllDir(path):
    filesList = os.listdir(path)  #得到当前目录下的所有文件

    for fileName in filesList:
        #判断是否是路径

        fileAbsPath=os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print("目录",fileName)
            getAllDir(fileAbsPath)
        else:
            print("普通文件",fileName)
getAllDir(r"E:\win10 系统")