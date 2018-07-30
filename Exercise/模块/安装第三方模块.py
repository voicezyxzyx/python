'''
安装三方模块，需要知道模块的名字

Pillow   非常强大的处理图像的工具库
pip install Pillow
报错 :输入 pip instal --upgrade pip

'''
from PIL import Image
#打开图片
im = Image.open("nfs挂载.PNG")
#查看图片信息  图片类型、图片大小  图片模式
print(im.format,im.size,im.mode)
#设置图片的大小
im.thumbnail((550,200))
#保存成新图片
im.save("nfs.jpg","JPEG")


import numpy as np
a=np.array([1,2,3])
print(a)






