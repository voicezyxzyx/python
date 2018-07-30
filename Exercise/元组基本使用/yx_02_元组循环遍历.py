info =("zhangsan",18,1.75)
#元组中的数据不允许被修改和删除

#元组和列表进行转换
#  新定义的变量=list（元组）   元组转换成列表
#  新定义的变量=tuple（列表）  列表转换成元组
info2 = list(info)
info2.remove(1.75)
for item in info2:
    print(item)

