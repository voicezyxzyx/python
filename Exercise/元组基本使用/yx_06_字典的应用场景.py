#使用多个键值对，存储描述一个物体的相关信息-描述更复杂的数据信息
#将多个字典放在一个列表中，再进行遍历
card_list = [
    {"name":"张三",
     "qq":"450538542",
     "phone":"138389"},
    {"name":"李四",
     "qq":"450",
     "phone":"1523873"},

]
for card_info in card_list:
    print(card_info)