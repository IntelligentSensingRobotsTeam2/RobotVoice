# -*- coding: utf-8 -*-
## run in python3
import time
import socket, fcntl, struct


#client 发送端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15],'utf-8')))[20:24])


# ip = '192.168.50.135'
PORT = 7000 ## ros udp server port

def send_data(data, port=7000):
    ip = get_ip('ens33')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # for data in [b'mask', b'start spray']:
    # 发送数据:
    enc_data = data.encode('utf-8')
    s.sendto(enc_data, (ip, PORT))
    print('udp send:',data)
    # 接收数据:
    # receive_data, _ =s.recvfrom(1024)
    # print(receive_data)
    s.close()


if __name__ == '__main__':
    info = 'angle:90'
    send_data(info)
