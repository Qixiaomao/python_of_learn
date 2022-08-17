# 这是一个TCP客户端


import socket
import json


# 设置端口以及IP
IP = '127.0.0.1'
PORT = 50000
BUF = 1024
HOST = (IP,PORT)

# 建立socket实例对象
dataSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接服务端socket
dataSocket.connect(HOST)

# 循环发送信息
while True:
    # 从终端读入用户输入的字符串
    toSend = input('>>> ')
    if toSend =='exit':
        break
    
    # 发送消息，也要编码为bytes
    dataSocket.sendall(toSend.encode())
    
    # 等待接受服务器的消息
    recved = dataSocket.recv(BUF)
    # 如果返回空bytes,表示对方关闭了连接
    if not recved:
        break
    # 打印读取的信息
    print(recved.decode())
    
dataSocket.close()