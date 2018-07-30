'''
re模块   提供了正则表达式

re match函数
原型：match（pattern，string，flags=0）
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式
re.I 忽略大小写
re.L 做本地户识别
re.M 多行匹配
re.S  是匹配包括换行符在内的所有字符
re.U  根据Unicode字符集解析字符  影响\w  \W  \b \B
re.X  使我们更灵活的格式理解正则表达式
参数：尝试从字符串的起始位置匹配一个模式，如果不是起始位置，匹配成功的话，返回None

功能：
'''
import re
#www.baidu.com  判断是否是网址
result = re.match("www","www.baidu.com")
print(result)