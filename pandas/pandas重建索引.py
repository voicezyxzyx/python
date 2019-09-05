'''
填充时重新加注reindex()采用可选参数方法，它是一个填充方法，其值如下：

	pad/ffill - 向前填充值
	bfill/backfill - 向后填充值
	nearest  - 从最近的索引值填充
'''

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print (df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print (df2.reindex_like(df1,method='ffill'))


#rename() 允许基于一些映射（字典或者系列）或任意函数来重新标记一个轴
print ("After renaming the rows and columns:")
print (df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))