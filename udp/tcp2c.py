import socket
import sys

HOST= 'localhost'
PORT= 9999
s = None

for res in socket.getaddrinfo(HOST,PORT,socket.AF_UNSPEC,
                             socket.SOCK_STREAM):
    af, socktype,proto, canonname,sa = res
    try:
        s = socket.socket(af, socktype,proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is not None:
    print('could not open socket')
    sys.exit()
with s:
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received',repr(data))