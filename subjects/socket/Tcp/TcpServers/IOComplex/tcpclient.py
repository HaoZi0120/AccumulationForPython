#!/usr/bin/env python
# coding=utf-8

import socket

sk = socket.socket()
sk.connect(("192.168.109.111", 9999))
data = sk.recv(1024)
print data
while True:
    ret = input(">>>")
    if ret == 'exit':
        break
    print ret
    sk.sendall(ret)
    print sk.recv(1024)
sk.close()
