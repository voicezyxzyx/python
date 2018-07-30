#假设：以下内容是从网络上抓取的
#要求：
#1.将字符串中的空白字符全部去掉
#2.在使用  ”“ 作为分隔符，拼接成一个整齐的字符串
poem_str = "登鹳雀楼\t王之涣 \t白日依山尽\t\n黄河入海流\t\t欲穷千里目\t更上一层楼\t"
print(poem_str)
#1.拆分字符串
poem_list = poem_str.split()
print(poem_list)

#2.合并字符串
# join 返回一个字符串  需要再定义一个变量来接收
result = " ".join(poem_list)
print(result)