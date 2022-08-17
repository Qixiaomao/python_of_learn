# 导入socket、sys 模块
import socket
import sys

# 创建socket 对象
sctcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
sctcp.bind((host,port))

# 设置最大连接数，超过后排队
sctcp.listen(5)

while True:
    # 建立客户端链接
    clientsocket,addr = sctcp.accept()
    
    print("连接地址: %s"% str(addr))
    
    msg = '欢迎访问seven！' + '\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()