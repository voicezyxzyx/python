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
'''
Entry是一个输入控件，用于显示简单的文本内容
'''
#绑定变量
e=tkinter.Variable()
entry=tkinter.Entry(win,show="*")#show  密文显示  可用于输入密码时
entry2=tkinter.Entry(win,textvariable=e) #e就代表输入框的对象
#设置e的值
e.set("my name is zyx")
#取值
print(e.get())
entry2.pack()


#显示label
label.pack()

win.mainloop()
