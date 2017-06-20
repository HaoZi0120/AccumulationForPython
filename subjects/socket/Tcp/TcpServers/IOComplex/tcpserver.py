#!/usr/bin/env python
# coding=utf-8

import socket
import select

sk = socket.socket()
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('192.168.109.111', 9999,))
sk.listen(5)
inputs = [sk, ]
messages = {}
# messages = {
#  hexm: [消息1，消息2】
#  zhuxj: [消息1，消息2】
# }
# inputs = [sk, hexm, zhuxj, ly] # 服务端sk，客户端对象
outputs = []
outputs.append(sk)
while True:
    # sk监听哪个对象，只要有变化,新连接来了，rlist = [sk], 否则rlist=[], 如果一个连接sk来了，rlist=[sk],如果两个sk1,sk2同时来了，rlist=【sk1，sk2】
    # 1 超时时间

    # 监听sk（服务器端）对象，如果sk对象发生变化，表示有客户端来连接了,此时rlist值为服务端[sk]
    # 监听conn对象，如果conn发生变化，表示客户端有新消息发送过来，此时rlist值为[客户端]
    rlist, wlist, e = select.select(inputs, outputs, [], 1)
    # wlist所有给我发消息的人
    # r就是sk
    # rlist = [hexm]
    # rlist = [zhuxij, ly]
    print len(inputs), len(rlist), len(outputs),len(wlist)  # inputs里面多少对象， rlist表示多少客户端对象发生变化
    # 只有连接进来才for循环，不然rlist一直为空
    for r in rlist:
        if r == sk:
            # 新客户端来连接
            print r 
            # conn 是socket对象， 每个客户端的socket对象
            conn, address = r.accept()
            conn.sendall('hello')
            # 新客户来连接，
            messages[conn] = []
            inputs.append(conn)
        else:
            print '-----' 
            try:
                ret = r.recv(1024)
                if not ret:  # 接受空消息，主动抛出异常，断开连接
                    raise Exception('断开连接')
                else:
                    outputs.append(r)
                    # 客户发的消息加入这个客户的消息列表
                    messages[r].append(ret)
            # 有人发消息
            except Exception as e:
                # 断开连接，移除
                inputs.remove(r)
                del messages[r]  # 删除这个用户消息

    # 所有给我发过消息的人
    for w in wlist:
        msg = messages[w].pop()
        resp = msg + 'response'
        w.sendall(resp)
        outputs.remove(w)
