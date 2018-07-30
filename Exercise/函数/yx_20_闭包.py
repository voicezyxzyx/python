# def createCounter():
#     s = [0]
#     def counter():
#         while True:
#             s[0] = s[0]+1
#         return s[0]
#     return counter
# print(createCounter())

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x += 1
        return x
    return counter

createA = createCounter()
print(counterA(),counterA(),counterA(),counterA())
counterB=createCounter()
if[counterB(),counterB(),counterB(),counterB()]==[1,2,3]:
    print('测试通过')
else:
    print('测试失败')