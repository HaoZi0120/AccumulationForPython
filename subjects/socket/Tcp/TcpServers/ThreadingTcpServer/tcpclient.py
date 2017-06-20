#!/usr/bin/env python
# coding=utf-8

import socket

ip_port = ('192.168.109.111', 8000)

s = socket.socket()
s.connect(ip_port)
welcome_msg = s.recv(1024)
print(welcome_msg.decode())
while True:
    send_data = raw_input(">> input message: ").strip()
    if len(send_data) == 0: continue
    s.send(send_data)  # 发送输入的命令
    tag = s.recv(1024)  # 接收tag
    tag = str(tag)
    if tag == 'exit':
        break
    elif tag.startswith('Ready'):  # 如果收到Ready和包长度
        msg_size = int(tag.split('|')[-1])
    else:
        print tag
        continue
    start_tag = 'Start'
    s.send(start_tag)  # 发送开始标志
    recv_size = 0
    recv_data = b''
    while recv_size < msg_size:
        recv_msg = s.recv(1024)
        recv_data += recv_msg
        recv_size += len(recv_msg)
        print 'MSG SIZE %s RECV_SIZE %s' % (msg_size, recv_size)

    print recv_data
s.close()