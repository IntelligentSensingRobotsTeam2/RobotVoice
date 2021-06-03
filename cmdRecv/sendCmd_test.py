# -*- coding: utf-8 -*-

import time
import socket, fcntl, struct


#client 发送端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = '192.168.50.134'
PORT = 8000

# ip = get_ip('ens33')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'mask', b'start spray']:
    # 发送数据:
    s.sendto(data, (ip, PORT))
    # 接收数据:
    receive_data, _ =s.recvfrom(1024)
    print(receive_data)
    time.sleep(3)

s.close()
