import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5007
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def fac(number):
    num = 1
    while number >= 1:
        num *= number
        number = number - 1
    return num

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data=fac(int(data))
    print "received message:", data
