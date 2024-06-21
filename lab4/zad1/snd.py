import socket
from socket import AF_INET, SOCK_DGRAM

s = socket.socket(AF_INET, SOCK_DGRAM)


while (True): 
  data = input('>>')
  if not data: 
    break 
  else: 
    s.sendto(bytes(data,'utf-8'), ('127.0.0.1', 9002)) 
  # end if 
# end while 
