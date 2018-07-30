import tkinter
#创建主窗口
win=tkinter.Tk()
win.title("这是标题")
#win.geometry("500x500+192+100")    #设置大小和位置

'''
文本控制，用于显示多行文本
'''
#创建滚动条
scroll=tkinter.Scrollbar()
text=tkinter.Text(win,width=50,height=5) #height 表示显示的行数
text.pack()
#将滚动条放到哪一侧
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


str='''asdascascas asdc ca cas casc asc
 as cdas按时吃按时吃 按时
 吃asadv收到v是大V是不是大V
 收到v是DVD绑定不是大V是大V是大V 
 cdc asd as das das  sdv s vs vsd vs dvs
  dvs
   sdvds sdsd sd
   ssdvsd sd s sdvsdsd  svsdsdsd
   sdsdsdvsdvsdvvvvvvvvvvvsdv     sdvsdvsv dvs v'''
text.insert(tkinter.INSERT,str)
win.mainloop()





