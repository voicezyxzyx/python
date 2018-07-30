xiaoming_dict={"name":"小明",
               "age":18}

#1.统计键值对的数量
print(len(xiaoming_dict))

#2.合并字典
zyx_dict={"state":"student",
          "height":1.70}
xiaoming_dict.update(zyx_dict)
print(xiaoming_dict)

#清空字典
xiaoming_dict.clear()
print(xiaoming_dict)