#i =0
#while i<10:
 #   if(i==3):
  #      break
   # print(i)
    #i +=1

i =0
while(i<10):

    #当continue某一条件满足时，不执行后续重复的代码
    if(i==9):
        #注意在循环中，如果使用continue这个关键词
        #在使用关键字之前，需要确认循环的计数是否修改
        #否则会导致死循环
        i +=1
        continue
    print(i)
    i += 1