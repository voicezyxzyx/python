import tkinter
#创建主窗口
win=tkinter.Tk()
win.title("这是标题")
win.geometry("500x500+192+100")    #设置大小和位置

'''
文本控制，用于显示多行文本
'''
text=tkinter.Text(win,width=30,height=4) #height 表示显示的行数
text.pack()
str='''asdascascas asdc ca cas casc asc as cdcdc asd as das das  sdv s vs vsd vs dvs dvs dvs v'''
text.insert(tkinter.INSERT,str)

win.mainloop()





