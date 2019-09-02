#创建一个新的空系列
'''
Pandas系列可以使用以下构造函数创建 -
pandas.Series( data, index, dtype, copy)。
构造函数的参数如下 -

编号 参数        描述
1   data    数据采取各种形式，如：ndarray，list，constants
2   index   索引值必须是唯一的和散列的，与数据的长度相同。 默认np.arange(n)如果没有索引被传递。
3   dtype   dtype用于数据类型。如果没有，将推断数据类型
4   copy    复制数据，默认为false。
'''
#使用默认索引
import pandas as pd 
import numpy as np 
data=np.array(['a','b','c','d'])
s=pd.Series(data)
print(s)

#添加指定索引
s=pd.Series(data,index=[100,101,102,103])
print(s)

#从字典创建一个系列（Series）
data1={'a':1,'b':2,'c':3}
s1=pd.Series(data1)
#dtype输出类型
print(s1.dtype)
print(s1)
#输出指定位置的数据
print(s1[1])
#利用切片获取数据
print(s1[0:2])

