# def factorial(n):
#     while n==1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(10))

def cal(n):
    print(n)
    return cal(n+1)
    if n ==1000:
        return 0
cal(1)