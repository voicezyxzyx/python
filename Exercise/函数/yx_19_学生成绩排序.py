'''假设我们用一组 tuple 表示学生名字 和 成绩：
L = [ ( ‘Bob,75’ ) , ( ‘Adam’,92 ) , ( ‘Bart’,66 ) , ( ‘Lisa’,88 ) ]
请用 sorted() 对上述列表分别按名字和成绩高到低排序
'''

#按照名字排序
def by_name(t):
    return t[0].lower()
L=[('Dob',75),('Adam',92),('Bart',66),('Cisa',88)]
L1=sorted(L,key=by_name)
print(L1)

#按照成绩排序
def by_score(t):
    return t[1]
L=[('Dob',75),('Adam',92),('Bart',66),('Cisa',88)]
L1=sorted(L,key=by_score)
print(L1)