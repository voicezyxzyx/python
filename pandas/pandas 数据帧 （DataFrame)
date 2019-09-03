'''
数据帧(DataFrame)是二维数据结构，即数据以行和列的表格方式排列。
数据帧(DataFrame)的功能特点：
	1、潜在的列是不同的类型
	2、大小可变标
	3、记轴(行和列)
	4、可以对行和列执行算术运算

pandas中的DataFrame可以使用以下构造函数创建 -
	pandas.DataFrame( data, index, columns, dtype, copy)
'''

#创建一个空的DataFrame
import pandas as pd 
df=pd.DataFrame()
print(df)

#从列表创建DateFrame
data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)

data1=[['Alex',15],["Bob",16],["Clarke",21]]
df1=pd.DataFrame(data1,columns=['Name','Age'])
print(df1)

#字典列表可作为输入数据传递以用来创建数据帧(DataFrame)，字典键默认为列名。
# 实例-1
# 以下示例显示如何通过传递字典列表来创建数据帧(DataFrame)。
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df2 = pd.DataFrame(data)
print (df2)
'''
执行上面示例代码，得到以下结果 - 
    a    b      c
0   1   2     NaN
1   5   10   20.0
'''

#从系列的字典来创建DataFrame  
import pandas as pd 
d={'one':pd.Series([1,2,3],index=['a','b','c']),
	'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df3=pd.DataFrame(d)
print(df3)
'''
执行上面示例代码，得到以下结果 - 
      one    two
a     1.0    1
b     2.0    2
c     3.0    3
d     NaN    4
'''

#删除指定列，可以用del删除也可以使用pop弹出
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df4 = pd.DataFrame(d)
print ("Our dataframe is:")
print (df)

# using del function
print ("Deleting the first column using DEL function:")
del (df4['one'])
print (df4)

# using pop function
print ("Deleting another column using POP function:")
df4.pop('two')
print (df4)