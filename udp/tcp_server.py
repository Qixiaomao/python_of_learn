from asyncio.windows_utils import BUFSIZE
from socket import *
import struct
import subprocess

HOST = ''
PORT = 9999
ADDR = (HOST,PORT)
BUFSIZE = 1024

tcps = socket(AF_INET,SOCK_STREAM)
tcps.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcps.bind(ADDR)
tcps.listen(5)

while True:
    conn,addr = tcps.accept() #建立连接，堵塞端口
    print(addr)
    while True:
        try:
            data_cmd = conn.recv(BUFSIZE)
            if not data_cmd:break  #避免接受到空消息
            print("收到客户端的命令")
            res = subprocess.Popen(data_cmd.decode('utf-8'),shell=True,stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,stdin=subprocess.PIPE)
            err = res.stderr.read() #通过res.stderr.read()读取错误信息
            if err:
                res_data = err
            else:
                res_data=res.stdout.read() ## 通过res.stdout.read()读取标准输出信息
            if not res_data:
                res_data = '执行成功'.encode('gbk') # 防止操作系统执行命令后，返回值为空
            length = len(res_data)
            data_length = struct.pack('i',length)
            conn.send(res_data)
        except Exception as e:
            print(e)
            break
                