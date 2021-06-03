# -*- coding: utf-8 -*-
## speech Command recieving UDP server. listen to data from socket.

import time 
import os,threading
import socket,signal
import fcntl, struct


DEBUG = True   ## print debug information 
speaker =  None


def server_exit(signum, frame):
    print('\nServer Stopped by keyboard interupt.')
    exit()


## get IP of current PC. (python3 Linux OS)
def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15],'utf-8')))[20:24])

def start_server():
    global speaker
    ip = get_ip('ens33')
    if DEBUG:
        print('current ip:{}'.format(ip))
    PORT = 8000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = (ip, PORT)  
    server_socket.bind(address)  

    while True:

        now = time.time() 
                        # 默认是阻塞的
        receive_data, client = server_socket.recvfrom(1024)

        if DEBUG:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now)))
            print("recv from %s, data: %s\n" % (client, receive_data.decode('utf-8')))

            server_socket.sendto(b'server recieved.', client)
        if speaker is not None:
            speaker._conversation.say(receive_data.decode('utf-8'), True)



def run(wk=None):
    global speaker
    speaker = wk
    t = threading.Thread(target=lambda: start_server(),daemon=True)
    t.start()


if __name__ == '__main__':
    print('UDP server started. ctrl-c to stop.')
    signal.signal(signal.SIGINT, server_exit)
    signal.signal(signal.SIGTERM, server_exit)
    DEBUG = True
    run()
    while(1):
        time.sleep(1)
