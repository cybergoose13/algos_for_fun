#   Packet Sniffing Code from book "Black Hat Python"
'''
    To run:
        Start-Process powershell -Verb runAs
        python sniffer.py
    program must have admin otherwise will throw winError 10013
    network card must also be in monitor mode to sniff packets
    Change host IP to valid ip address
'''

import socket
import os

host= "192.168.x.x"

if os.name == "nt":
    socket_protocol= socket.IPPROTO_IP
else:
    socket_protocol= socket.IPPROTO_ICMP


sniffer= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

sniffer.bind((host, 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print( sniffer.recvfrom(65565))

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
