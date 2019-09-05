import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print (df)

#sum()
print(df.sum())  #计算每一行的值的总和

#mean()  返回平均值
print(df.mean())   

#std()  返回数字列的标准方差
print(df.std())


'''
pandas 中描述性统计信息的函数
编号         函数            描述
1           count()        非空观测数量
2           sum()          所有值之和
3           mean()         所有值的平均值
4           median()       所有值的中位数
5           mode()         值的模值
6           std()          值的标准偏差
7           min()          所有值中的最小值
8           max()          所有值中的最大值
9           abs()          绝对值
10          prod()         数组元素的乘积
11          cumsum()       累计总和
12          cumprod()      累计乘积原
'''


# describe() 函数  计算有关DataFrame列的统计信息的概要
print(df.describe())  

'''
输出结果如下：
             Age     Rating
count  12.000000  12.000000
mean   31.833333   3.743333
std     9.232682   0.661628
min    23.000000   2.560000
25%    25.000000   3.230000
50%    29.500000   3.790000
75%    35.500000   4.132500
max    51.000000   4.800000
'''