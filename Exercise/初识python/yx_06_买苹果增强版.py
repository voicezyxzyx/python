''''
1.输入苹果的单价
2.输入苹果的重量
3.计算支付金额
两个字符串之间是不能直接用乘法的
'''
#将价格转换成小数
price = float(input("请输入苹果单价："))
#将重量转化成小数
weight = float(input("苹果的总量："))
#用两个小数来计算最终金额
money = price * weight
print("需要支付金额为 %.1f 元"% money)