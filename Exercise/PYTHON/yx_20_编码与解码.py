path=("D:\python\pycharm文件\PYTHON\文件读写.txt")
with open(path,"wb") as f1:
    str = "zyx is a good man"
    f1.write(str.encode("utf-8"))
with open(path,"rb") as f2:
    data=f2.read()
    print(data)
    newData=data.decode("gbk")
    print(newData)
