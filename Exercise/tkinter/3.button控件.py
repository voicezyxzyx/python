import tkinter
#创建主窗口
win=tkinter.Tk()
win.title("这是标题")
win.geometry("500x500+192+100")    #设置大小和位置

#label显示在win窗体上
label=tkinter.Label(win,text="hello world hello world",bg="black",
                    fg="white",
                    font=("黑体",15),
                    wraplength=200,#wraplength  指定文本中多宽进行换行
                    justify='right',#justify 设置对其格式
                    anchor="s"  #anchor 位置 n：靠北  w：靠西  e:靠东 s：靠南  center：居中
                   )
#显示label
label.pack()

def func():
    print("hello hello hello hello hello")
def showInfo():
    print(entry.get())
#创建按钮
button = tkinter.Button(win,text="按钮1",command=func,#按一下按钮，执行一次func程序
                        width=10,height=5#设置按钮宽和高
                        )
button2 = tkinter.Button(win,text="输出",
                         command=lambda :print("world world"))#lambda 是一个匿名函数
button3 = tkinter.Button(win,text="检测",command=showInfo)
button4 = tkinter.Button(win,text="退出",command=win.quit)

e=tkinter.Variable()
entry=tkinter.Entry(win,textvariable=e)
e.set("my name is zyx")
entry.pack()
button.pack()
button2.pack()
button3.pack()


win.mainloop()
