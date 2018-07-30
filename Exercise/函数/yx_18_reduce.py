# from functools import reduce
# def add(x,y):
#     return x+y
# print(reduce(add,[1,3,5,7,9]))
def by_score(t):
    return t[1]
L=[('Dob',75),('Adam',92),('Bart',66),('Cisa',88)]
L1=sorted(L,key=by_score,reverse=True)
print(L1)