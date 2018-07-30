# def prin_line(char,times):
#     print(char*times)
# prin_line("-",10)
def print_line(char,times):
    """打印多行分割线
    :param char:分割字符
    :param times: 分割线重复的次数
    """
    i=1
    while i<=5:
        print(char*times)
        i +=1
print_line("-",10)