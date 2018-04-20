#!/usr/bin/env python
#coding:utf-8

import threading
import time
import socket

ver='0.1'


'''
file name: scar_thread_socket_server.py
function:
'''

class thread_socket(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port
        #creat a socket by default param
        self.sock = socket.socket()
        #set timeout time, The port is occupied after the accident is prevented from exiting 
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host,self.port))

    def listen(self):
        #5 clients are allowed to connect at the same time 
        self.sock.listen(5)
        print("start listen!!")
        while True:
            clientfd, address = self.sock.accept()
            print("acess a connection:"+ str(address))
            #set timeout time
            clientfd.settimeout(10)
            threading.Thread(target=self.handle_client_request, args=(clientfd, address)).start()
            

    def handle_client_request(self, clientfd, address):
        while True:
            try:
                data = clientfd.recv(1024)
                if data:
                    print("got a message:"+data)
                    clientfd.sendall('server verion:'+ver+'\n')
                    clientfd.sendall('data:'+data+'\n')
            except: 
                clientfd.close()

def main():
    server = thread_socket('', 9000)
    server.listen()

if __name__ == "__main__":
    main()
