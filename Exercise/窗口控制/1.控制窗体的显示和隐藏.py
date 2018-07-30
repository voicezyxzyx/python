import win32con
import win32gui
import time


#找出窗体的编号
QQWin=win32gui.FindWindow("新标签页 - UC浏览器","Chrome_WidgetWin_1")

#隐藏窗体
win32gui.ShowWindow(QQWin.win32con.SW_HIDE)