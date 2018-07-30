# name_list =["zhangsan","lisi"]
#
# name_list.append("wangxiao")
# name_list.insert(2,"wangma")
# temp_list = ["sunkukong","zhubajie","shashidi "]
# name_list.extend(temp_list)
# #pop方法可以从列表中删除栈顶元素
# #pop方法可以指定要删除元素的索引
# name_list.pop(1)
# name_list.remove("zhubajie")
# #clear方法可以清空列表
# name_list.clear()
# print(name_list)

name_list = ["张三","李四","王五","张三"]
list_len = len(name_list)
count = name_list.count("张三")
print(list_len)
print("张三出现了%d次" %count)

#从列表中删除第一次出现的元素，如果数据不存在，程序会报错
name_list.remove("张三")
print(name_list)