from pydoc import cli
from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime




HOST = ''
PORT = 9999
ADDR = (HOST, PORT)
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
print('服务器开始监听……')
while True:
    client,addr = server.accept()
    print(str(addr)+"连接到了服务器.")
    client.send(str(datetime.now()).encode('utf-8'))
    client.close()
        
        

