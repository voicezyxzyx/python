import socket
udpClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=input("请输入数据：")
    udpClient.sendto(data.encode("utf-8"),('192.168.221.1',8900))

    # info=udpClient,recv(1024).decode("utf-8")
    # print("服务器说：",info)