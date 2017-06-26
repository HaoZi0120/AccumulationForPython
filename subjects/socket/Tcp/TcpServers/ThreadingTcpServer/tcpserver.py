#!/usr/bin/env python
# coding=utf-8

import SocketServer
import subprocess

class MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        self.request.sendall('welcome')
        while True:
            data = (self.request.recv(1024)).strip()
            if len(data) == 0: break
            print self.client_address, data
            cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            cmd_res = cmd.stdout.read()
            if not cmd_res:
                cmd_res = cmd.stderr.read()
            if len(cmd_res) == 0:  # cmd has not output
                cmd_res = b"cmd has output"
            self.request.send(cmd_res)

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)
    server.serve_forever()
