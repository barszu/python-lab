import socket
from socket import AF_INET, SOCK_DGRAM

server_socket = socket.socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("localhost", 9002))

while True:
  buffer, address = server_socket.recvfrom(256)
  print(buffer)
  data = str(buffer,'utf-8')
  if data=='q': 
    print("Program has exited!")
    break 
  else: 
    print(data,address[0])


# close socket
server_socket.close()