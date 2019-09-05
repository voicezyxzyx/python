'''
创建面板可以使用多种方式
1、从ndarrays创建
2、从DataFrames的dict创建
'''
#从3D ndarray创建
import pandas as pd 
import numpy as np 
data=np.random.rand(2,4,5)
p=pd.Panel(data)
print(p)

#从DataFrame对象的dict创建面板
import pandas as pd 
import numpy as np

data1={'Item1':pd.DataFrame(np.random.randn(4,3)),
		'Item2':pd.DataFrame(np.random.randn(4,2))}
p1=pd.Panel(data1)
print(p1)


'''
要从面板中选择数据，可以使用以下方式 -
1、Items
2、Major_axis
3、Minor_axis
'''
#使用Items选择数据
print(p1['Item1'])

#使用major_axis访问数据
print(p1.major_xs(1))

#使用minor_axis访问数据
print(p1.minor_xs(1))