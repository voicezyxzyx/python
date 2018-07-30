#sum = 0
#i=0
#while i<=100:
#   sum += i
#    i +=1
#print("0-100相加的和为： %d" %sum)



#计算0-100之间偶数的和
sum = 0
i = 0
while i<= 100:
    if i%2 == 0:
        print(i)
        sum += i
        i += 2
print("0-100之间的偶数和为 ：%d" % sum)