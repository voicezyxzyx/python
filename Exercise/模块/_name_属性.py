'''
_name_属性：
模块就是一个可执行的.py文件，一个模块被另一个程序引用。
我们不想让模块中的某些代码执行，可以用_name_属性来使程序仅调用模块中的一部分


每个模块都有一个_name_属性，当其值等于“_main_”时，表明该模块自身在执行。否则被引入其他
文件
'''
if __name__ == '__main__':
    print("i will go to beijin")
else:
    def sayHello():
        print("hello")
        print("hello")
        print("hello")
    def sayGood():
        print("Good")











