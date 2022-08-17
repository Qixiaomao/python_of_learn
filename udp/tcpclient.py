from pydoc import cli
from socket import AF_INET, SOCK_STREAM, socket


HOST = '172.19.83.237'
PORT = 9999
ADDR = (HOST, PORT)
client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)

while True:
    data = input('> ').encode('utf-8')
    if not data:break
    client.send(data)
    print(data)
    #print(client.recv(1024).decode('utf-8'))
    client.close()
    

