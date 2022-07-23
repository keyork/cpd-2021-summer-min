"""
@ File Name     :   server.py
@ Time          :   2022/07/21
@ Author        :   Cheng Kaiyue
@ Version       :   1.0
@ Contact       :   chengky18@icloud.com
@ Description   :   通信系统服务端
@ Function List :   func1() -- func desc1
@ Class List    :   Class1 -- class1 desc1
@ Details       :   交换的数据为List: [客户端名称, 信息种类, 信息]
"""

import sys

sys.path.append("..")

import json
import socket
import time
from threading import Thread
from utils.setlog import LOGGER


class CommuServer:
    def __init__(self, addr, port, is_chat):

        self.addr = str(addr)
        self.port = int(port)
        self.is_chat = is_chat
        self.server = None
        self.status = False
        self.client_list = {}

    def start_server(self):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.addr, self.port))
        self.server.listen(128)
        LOGGER.info("Server Start")
        self.status = True

    def acc_conn(self):

        while self.status:

            client_socket, client_addr = self.server.accept()
            print("Connect")
            client_thr = Thread(
                target=self.process_msg, args=(client_socket, client_addr)
            )
            client_thr.setDaemon(True)
            client_thr.start()

    def process_msg(self, client_socket, client_addr):

        client_socket.sendall("Connect".encode(encoding="utf8"))
        while True:
            try:
                raw_msg = client_socket.recv(1024).decode(encoding="utf8")
                msg = json.loads(raw_msg)
                client_name = msg[0]
                mode = msg[1]
                data = msg[2]
                # TODO: 通知所有客户端

                if mode == "CONN":
                    self.client_list[client_name] = client_socket
                elif mode == "DATA":
                    print("[{}]: {}".format(client_name, data))
                if data != "exit":
                    for other_client in self.client_list:
                        if other_client != client_name:
                            self.client_list[other_client].sendall(
                                raw_msg.encode(encoding="utf8")
                            )

            except:
                self.remove_client(client_name)

                data_list = []
                data_list.append(client_name)
                data_list.append("DATA")
                data_list.append("exit")
                data_send = json.dumps(data_list)
                for other_client in self.client_list:
                    self.client_list[other_client].sendall(
                        data_send.encode(encoding="utf8")
                    )

                break

    def remove_client(self, client_name):

        remove = self.client_list[client_name]
        if remove:
            remove.close()
            self.client_list.pop(client_name)
            LOGGER.info("客户端[{}]下线".format(client_name))


if __name__ == "__main__":

    server = CommuServer("", 0000, True)
    server.start_server()
    thread = Thread(target=server.acc_conn)
    thread.setDaemon(True)
    thread.start()
    while True:
        time.sleep(1)
