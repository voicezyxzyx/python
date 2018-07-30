# #打印9行小星星
# i = 1
# while i<=9:
#     j = 1
#     while j<= i:
#         print("*",end="")
#         j +=1
#     print("%d" %i)
#     i +=1
#


i=1
while i<=9:
    j = 1
    s =0
    while j<= i:
        print("%d*%d=%d" %(j,i,j*i),end="\t")
        j +=1
    print("")
    i +=1
