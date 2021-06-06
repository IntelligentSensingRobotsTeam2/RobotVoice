# -*- coding: utf-8 -*-
## run in python3
import time
import socket, fcntl, struct
import argparse


#client 发送端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15],'utf-8')))[20:24])


# ip = '192.168.50.135'

def send_data(data, port=7001):
    ip = get_ip('ens33')
    #ip = get_ip('wlp3s0')
    print('ip:{} port {}'.format(ip,port))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # for data in [b'mask', b'start spray']:
    # 发送数据:
    enc_data = data.encode('utf-8')
    s.sendto(enc_data, (ip, port))
    print('udp send:',data)
    # 接收数据:
    # receive_data, _ =s.recvfrom(1024)
    # print(receive_data)
    s.close()


if __name__ == '__main__':
    
    '''
    run for help:  'python3 cmdRecv/udp_send.py -h'    
    run example :   python3 cmdRecv/udp_send.py -Port 7000 -Data admin:1

    '''
    parser = argparse.ArgumentParser(description="UDP client to send data")
    parser.add_argument('-Port', type=int, default=8000, help='UDP sent Port')
    parser.add_argument('-Data', type=str, default='angle:180', help='UDP sent Data')
    args = parser.parse_args()

    PORT =args.Port
    Data =args.Data

    send_data(Data,PORT)
