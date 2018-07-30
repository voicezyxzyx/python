student =[
    {"name":"阿土",},
    {"name":"小美",}
]
findname = "张三"
for stu_dict in student:
    print(stu_dict)
    if stu_dict["name"] == findname:
        print("找到要查找的名字%s" %findname)
        #如果已经找到，应该直接退出循环，而不再遍历列表
        break
else:
    #如果希望在搜索列表时，所有的字典检查之后，都没有发现要搜索的目标
    #还希望得到一个统一的提示
    print("没有这个人")
print("搜索结束")