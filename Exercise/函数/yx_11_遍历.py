name_list = ["张三sansna ","李四","王五","王小二"]
#迭代遍历
"""
顺序的从列表中一次获取数据，每一次循环过程中，数据
都会保存在my——name这个变量中，在循环体内部可以访
问到当前这一次获取到的数据
"""
for my_name in name_list:
    print("我的名字叫 %s" %my_name)