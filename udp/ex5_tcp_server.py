
# -*- coding: utf-8 -*-

import os
import re
import socket
from time import ctime


HOST = ''
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

ls_patt = re.compile(r'^ls(?:\s+(\S+))?$')


def command_handler(command):
    if command == 'date':
        return ctime()
    if command == 'os':
        return os.name
    ls_m = ls_patt.match(command)
    if ls_m:
        _dir = ls_m.group(1) if ls_m.group(1) else os.curdir
        try:
            return repr(os.listdir(_dir))
        except BaseException as be:
            return repr(be)
    return command


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(BUFSIZ)
            if not data:
                break
            result = command_handler(data.decode('utf-8'))
            conn.sendall(bytes(result, 'utf-8'))
