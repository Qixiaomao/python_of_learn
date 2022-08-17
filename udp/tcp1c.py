from asyncio.windows_utils import BUFSIZE

import socket

  

HOST= 'localhost'

PORT = 9999

BUFSIZE = 1024

  

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))

s.send(b'Hello,world')

data = s.recv(BUFSIZE)

s.close()

print('Received',repr(data))