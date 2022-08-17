from asyncio.windows_utils import BUFSIZE

import socket

  

HOST= ''

PORT = 9999

BUFSIZE = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))

s.listen(1)

conn,addr = s.accept()

print('Connected by',addr)

while True:

   data = conn.recv(BUFSIZE)

   if not data: break

   conn.send(data)

conn.close()