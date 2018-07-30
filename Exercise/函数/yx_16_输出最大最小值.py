l=list(range(0,10,2))
def findMinAndMax(l):
    if l==[]:
        return (None,None)
    else:
        my_min=l[0]
        my_max=l[0]
        for i in l:
            if my_min<i:
                my_min=i
            if my_max>i:
                my_max=i
        return (my_min,my_max)
print(l)
print(findMinAndMax(l))


