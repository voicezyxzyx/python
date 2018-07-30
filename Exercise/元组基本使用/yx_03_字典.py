#字典是一个无序的数据集合，使用print函数输出字典时，通常输出的
#顺序和定义的顺序是不一致的
xiaoming_dict = {"name":"xiaoming",
            "age":20,
            "gender":True,
            "height":1.75}
 #1.取值
 #2.在取值时，如果指定的值不存在，程序会报错
print(xiaoming_dict["name"])

#3.增加/修改
#如果元素不存在，则增加，如已存在，则修改
xiaoming_dict["age"] = 21
xiaoming_dict["name"] = "xiaoxiaoming"
print(xiaoming_dict)

#4.删除
xiaoming_dict.pop("name")
print(xiaoming_dict)
