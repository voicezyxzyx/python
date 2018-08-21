import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('192.168.119.1',8080))
#监听
server.listen(5)
print("服务器启动成功！")
#等待连接
clientSocket,clientAddress=server.accept()
print("%s------%s连接成功"%(clientSocket,clientAddress))
while True:
    data=clientSocket.recv(1024)
    print("客户端说:"+data.decode("utf-8"))
    sendDate=input("请输入返回给客户端的数据：")
    clientSocket.send(sendDate.encode("utf-8"))
