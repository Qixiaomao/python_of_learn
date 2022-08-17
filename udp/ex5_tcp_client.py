#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


HOST = 'localhost'
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ADDR)
    while True:
        data = input('> ')
        if not data:
            break
        s.sendall(bytes(data, 'utf-8'))
        data = s.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
