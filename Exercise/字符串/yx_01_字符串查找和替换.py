hello_str = "hello world"
#判断啊是否以指定字符串开始
print(hello_str.startswith("hello"))

#判断是否已指定字符串结束
print(hello_str.endswith("worl"))

#查找指定字符串
print(hello_str.find("llo"))

#index同样可以查找指定的字符串在最大字符串中的索引
#index如果指定字符串不存在，会报错
#find如果指定字符串不存在。会返回-1
print(hello_str.find("abc"))

#4替换字符串
#replace方法执行完成之后，会返回一个新的字符串
#注意：不会修改原有字符串的内容
print(hello_str.replace("hello","nihao"))
print(hello_str)