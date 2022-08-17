# 这是一个TCP服务器端

import socket
from time import ctime

def sever():
     # 设置好IP,HOST等信息
    IP = '127.0.0.1'
    PORT = 50000
    BUF = 1024
    HOST = (IP,PORT)

    # SOCKET实例化
    listenSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # socket绑定地址和端口
    listenSocket.bind(HOST)

    # 使socket处于监听状态，等待客户端的连接请求
    # 参数5表示最多接受多少个等待连接的客户端
    listenSocket.listen(5)
    print(f'服务端启动成功，在{PORT}端口等待客户端连接……')

    dataSocket,addr = listenSocket.accept()
    print('接受一个客户端连接：',addr)

    while True:
        # 尝试读取对方发送的消息
        # BUF 指定从接收缓冲里最多读取多少字节
        recved = dataSocket.recv(BUF)
        
        # 如果返回空bytes，表示对方关闭了连接
        # 退出循环，结束消息收发
        if not recved:
            break
        # 如果客户端接受到的信息是pause，暂停数据采集
        if recved.decode() =='pause':
            dataSocket.send(f'暂停数据采集'.encode())
            
        # 如果客户端接受到的信息是resume 恢复数据采集
        if recved.decode() =='resume':
            dataSocket.send(f'恢复数据采集'.encode())
        
        # 读取的字节数据是bytes类型，需要解码为字符串
        info = recved.decode()
        print(f'收到对方信息：{info}')
        
        # 发送的数据类型必须是bytes，所以要编码
        dataSocket.send(f'服务端收到了信息{info}'.encode())
        #dataSocket.send('[%s] %s' %(bytes(ctime(),'utf-8'),recved))
       
    # 服务端也调用close()关闭socket
    dataSocket.close()
    listenSocket.close()


if __name__ =='__main__':
    sever()