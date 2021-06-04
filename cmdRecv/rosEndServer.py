# -*- coding: utf-8 -*-
## speech Command recieving UDP server. listen to data from socket.

import time 
import os,threading
import socket,signal
import fcntl, struct


DEBUG = True   ## print debug information 
speaker =  None
import time

lastWarningTime = time.time()
lastHelloTime = time.time()
firstHello = True

def server_exit(signum, frame):
    print('\nServer Stopped by keyboard interupt.')
    exit()


## get IP of current PC. (python3 Linux OS)
def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15],'utf-8')))[20:24])

def execute_config(data):
    global speaker,lastWarningTime,lastHelloTime,firstHello
    curTime = time.time()
    cmd = data.split(':')[0]

    if cmd == 'say':
        if speaker is not None:
            speaker._conversation.say(data.split(':')[1], True)

    elif cmd == 'mask':  
        if speaker is not None:
            if curTime - lastWarningTime > 2:
                speaker._conversation.say('请戴上口罩', True)
                lastWarningTime = curTime
    
    elif cmd == 'admin':
        if speaker is not None:
            speaker.adminVerifyTime = curTime
            if firstHello or curTime - lastHelloTime > 60:
                speaker._conversation.say('管理员您好', True)
                lastHelloTime = curTime
                firstHello = False

    elif cmd == 'hello':
        if speaker is not None:
            if curTime - max([lastHelloTime,lastWarningTime]) > 5:
                speaker._conversation.say(speaker.helloStr, True)
    return
    
def start_server():
    ip = get_ip('ens33') ## 
    if DEBUG:
        print('current ip:{}'.format(ip))
    PORT = 7000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = (ip, PORT)  
    server_socket.bind(address)  

    while True:

        now = time.time() 
                        # 默认是阻塞的
        receive_data, client = server_socket.recvfrom(1024)
        decode_data = receive_data.decode('utf-8')
        if DEBUG:
            # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now)))
            print("recv from %s, data: %s\n" % (client, decode_data))

            server_socket.sendto(b'server recieved.', client)
        execute_config(decode_data)




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

