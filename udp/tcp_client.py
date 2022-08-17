from asyncio.windows_utils import BUFSIZE
from socket import *
import subprocess
import struct

HOST= 'localhost'
PORT= 9999
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpc = socket(AF_INET,SOCK_STREAM)
tcpc.connect(ADDR)

while True:
    cmd_data = input("请输入命令：")
    if not cmd_data:continue
    if cmd_data == 'quit':break
    tcpc.send(cmd_data.encode('utf-8'))
    
    length_data = tcpc.recv(4)
    head_data = struct.unpack('i',length_data)[0]
    
    # 处理数据
    res_length = 0
    res_msg = b''
    while res_length < head_data:
        res_msg += tcpc.recv(BUFSIZE)
        res_length += len(res_msg)
        print(res_length)
    print('命令的执行结果是: ',res_msg.decode('gbk'))
tcpc.close()