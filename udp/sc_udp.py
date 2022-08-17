#这是一个UDP的服务器

# 导入包

from re import S
import socket
import sys
from time import ctime

host = ''
port = 9999
BUFSIZE = 1024
ADDR = (host,port)

udpsc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpsc.bind(ADDR)

while True:
    print("等待消息……")
    data,addr = udpsc.recvfrom(BUFSIZE)
    s = data.decode()
    udpsc.sendto(s.encode(),addr)
    print("……接受的信息来自于：",addr,"信息是：",data.decode())
    print()

udpsc.close()
