import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
print("Hello, pandas")

#通过传递值列表来创建一个系列，让Pandas创建一个默认的整数索引：
s=pd.Series([1,3,5,np.nan,6,8])
print(s)

dates= pd.date_range('20190902',periods=7)
print(dates)

df=pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('ABCD'))
print(df)
#查看前3行数据
print(df.tail(3))
#描述显示数据的快速统计概要
print(df.describe())
#按值排序
print(df.sort_values(by='B'))
#通过切片获取数据 
print(df[0:3])
print(df['20190902':'20190903'])

