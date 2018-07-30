#对文件的操作分为读文件和写文件
'''
过程：
1.打开文件
open(path.flag[,encoding][,errors])
path:文件路径    flag：打开方式  （r(只读方式的打开)\rb（以二进制格式打开文件用于只读）\
r+（打开一个文件用于读写）\w\wb（打开一个文件值用于写入二进制，如果存在则覆盖，不存在则新建））
a（打开一个文件应用于追加，如果存在，则会放在文件末尾）
2.读文件
3.关闭文件
'''
#打开文件
path=("D:\python\pycharm文件\PYTHON\文件读写.txt")
f=open(path,"r+",encoding="utf-8")
#读文件

#1、读取文件的全部内容
#str1=f.read()
#f.write("zzbbbbbbbbbbbbbbz")
#print(str1)
#2、读取部分内容(指定字符数）
# str2=f.read(10)
# print(str2)
#3、读取整行，包括“\n”字符

str4=f.readlines()
print(str4)
with open("D:\python\pycharm文件\PYTHON\测试.txt","w")as f2:
    f2.writelines(str4)

#关闭文件
f.close()