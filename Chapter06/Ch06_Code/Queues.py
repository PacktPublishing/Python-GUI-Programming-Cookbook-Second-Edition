'''
May 2017
@author: Burkhard A. Meier
'''

# def write_to_scrol(inst):
#     print('hi from Queue', inst)
#     for idx in range(10): 
#         inst.gui_queue.put('Message from a queue: ' + str(idx)) 
#     inst.create_thread(6)


# using TCP/IP
from socket import socket, AF_INET, SOCK_STREAM 
 
def write_to_scrol(inst): 
    print('hi from Queue', inst) 
    sock = socket(AF_INET, SOCK_STREAM) 
    sock.connect(('localhost', 24000)) 
    for idx in range(10): 
        sock.send(b'Message from a queue: ' + bytes(str(idx).encode()) ) 
        recv = sock.recv(8192).decode() 
        inst.gui_queue.put(recv)       
    inst.create_thread(6) 
    
    



















