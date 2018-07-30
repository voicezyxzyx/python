import os
def getAllDirDE(path):
    stack=[]
    stack.append(path)

    #处理栈
    while len(stack) != 0:
        #从栈中去取数据
        dirPath=stack.pop()
        #目录下所有文件
        fileList = os.listdir(dirPath)

        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                print("目录", fileName)
                stack.append(fileAbsPath)
            else:
                print("普通文件",fileName)
getAllDirDE(r"D:\桌面文件存放处")