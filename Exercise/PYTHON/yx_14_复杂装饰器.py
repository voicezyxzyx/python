def say(name,age):
    if age<0:
        print("年龄信息出错，请重新输入")
    else:
        print("%s is a good man,and he is %s years old" %(name,age))


say("zyx",20)

# def outer():
#     def inner():
#
#
#         pass
#     return inner()