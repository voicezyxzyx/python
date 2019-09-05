'''
创建一个Series
'''
import numpy as np 
import pandas as pd 
s= pd.Series(np.random.randn(4))
print(s)
print('------------------')

#axes示例  返回系列的标签列表
import numpy as np 
import pandas as pd 
s= pd.Series(np.random.randn(4))
print("The axes are:")
print(s.axes)


#empty 示例  返回布尔值，表示对象是否为空
import numpy as np 
import pandas as pd 
s= pd.Series(np.random.randn(4))
print("Is the object empty？")
print(s.empty)


#ndim示例  返回对象的维数。根据定义，一个系列是一个1D数据结构
import numpy as np 
import pandas as pd 
s= pd.Series(np.random.randn(4))
print("The dimensions of the object:")
print(s.ndim)

#size示例  返回系列的大小（长度）
print(s.size)

#values示例，以数组的形式返回系列中的实际数据值
print(s.values)

#head(n)示例  返回前n行的值
print(s.head(2))

#tail(n)示例 返回后n行的值,如果不输入元素数，则默认显示数量为5，但是可以传递自定义数值
print(s.tail(1))


'''DataFrame基本功能
编号         属性或方法        描述
1              T            转置行和列。
2             axes          返回一个列，行轴标签和列轴标签作为唯一的成员。
3            dtypes         返回此对象中的数据类型(dtypes)。
4             empty         如果NDFrame完全为空[无项目]，则返回为True; 如果任何轴的长度为0。
5             ndim          轴/数组维度大小。
6             shape         返回表示DataFrame的维度的元组。
7             size          NDFrame中的元素数。
8             values        NDFrame的Numpy表示。
9             head()        返回开头前n行。
10            tail()        返回最后n行。
'''
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print (df)
print(df.T)    #  T转置



























