# 这是一个UDP的客户端

# 导入包

from asyncio.windows_utils import BUFSIZE
import socket
import time


host = 'localhost'
port = 9999
BUFSIZE = 1024
ADDR = (host,port)

udpclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input('> ').encode()
    
    if not data:break
    udpclient.sendto(data,ADDR)
    data,ADDR = udpclient.recvfrom(BUFSIZE)
    if not data:break
    print(data)
    
    
udpclient.close()