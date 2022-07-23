"""
@ File Name     :   client.py
@ Time          :   2022/07/21
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   通信系统客户端
@ Function List :   func1() -- func desc1
@ Class List    :   Class1 -- class1 desc1
@ Details       :   None
"""


import json
import socket
from threading import Thread


class CommuClient:
    def __init__(self, addr, port):

        self.addr = addr
        self.port = port
        self.name = input("请输入客户端名称: ")
        self.client = None
        self.is_exit = False

    def conn(self):

        self.client = socket.socket()
        self.client.connect((self.addr, self.port))
        print(self.client.recv(1024).decode(encoding="utf8"))
        self.send_msg("CONN", 0)

    def send_msg(self, type, msg):

        data_list = []
        data_list.append(str(self.name))
        data_list.append(str(type))
        data_list.append(str(msg))
        print(data_list)
        data_send = json.dumps(data_list)
        self.client.sendall(data_send.encode(encoding="utf8"))

    def comm(self):

        type = "DATA"
        msg = input("请输入消息: ")
        self.send_msg(type, msg)
        if msg == "exit":
            self.is_exit = True

    def recv(self):

        while True:
            msg = json.loads(self.client.recv(1024).decode(encoding="utf8"))
            client_name = msg[0]
            mode = msg[1]
            data = msg[2]

            if mode == "CONN":
                print("[{}] 上线".format(client_name))
            elif mode == "DATA":
                if data == "exit":
                    print("[{}] 下线".format(client_name))
                else:
                    print("[{}]: {}".format(client_name, data))


if __name__ == "__main__":
    client = CommuClient("", 0000)
    client.conn()
    thread = Thread(target=client.recv)
    thread.setDaemon(True)
    thread.start()
    while not client.is_exit:
        client.comm()
