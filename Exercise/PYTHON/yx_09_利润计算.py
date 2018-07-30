def get():
	i=int(input("请输入当月利润为:"))
	salary = 0
	if i<=10:
		salary=i*0.1
        print("应发放奖金为%d"% salary)
    elif i>10 and i<=20:
		salary=(10*0.1)+(i-10)*0.075
		print("应发放奖金为%d" %salary)
	elif i>20 and i<=40:
		salary=(10*0.1)+(10)*0.075+(i-20)*0.05
		print("应发放奖金为%d" %salary)
    else:
		salary=(10*0.1)+(10)*0.075+(20)*0.2+（i-40）*0.03
		print("应发放奖金为%d" %salary)
get()
