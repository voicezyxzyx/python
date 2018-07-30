#判断空白字符
#isspace 如果字符串中包含字符，则返回true
# space_str = "   "
# print(space_str.isspace())

#判断数字的三种方法
#判断字符串中是否   只   包含数字
#三个方法都不能判断小数
str = "123"
print(str)
print(str.isdecimal()) #只能判断只包含数字的字符串
print(str.isdigit())  #unicode字符串  如：“（1）”“\u00b2"
print(str.isnumeric())#还可以判断中文数字