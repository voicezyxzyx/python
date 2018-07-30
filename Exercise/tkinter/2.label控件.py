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

win.mainloop()
