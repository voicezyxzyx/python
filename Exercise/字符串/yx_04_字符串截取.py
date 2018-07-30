num_str = "0123456789"
num_str1 = num_str[2:6]
num_str2 = num_str[2:]
num_str3 = num_str[::2]   #从0开始，步长为2
num_str4 = num_str[1::2]  # 从1开始，步长为2
num_str5 = num_str[9::-1] #逆序输出
print(num_str1)
print(num_str2)
print(num_str3)
print(num_str4)
print(num_str5)