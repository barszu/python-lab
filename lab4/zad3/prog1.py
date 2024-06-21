import threading
import time
import socket
from socket import AF_INET, SOCK_DGRAM



def rcv():
  while True:
    buffer, address = s.recvfrom(256)
    data = str(buffer,'utf-8')
    if data=='q': 
      print("Program has exited!")
      break 
    else: 
      print(data,address[0])

    

def prog2(n):
  for i in range(n):
    print('-',i)
    time.sleep(1)


s = socket.socket(AF_INET, SOCK_DGRAM)
s.bind(("localhost", 9001))



w1=threading.Thread(target=rcv)
w1.daemon = True
w1.start() 


while (True): 
  data = input('>>')
  if not data: 
    break 
  else: 
    s.sendto(bytes(data,'utf-8'), ('127.0.0.1', 9001)) 
  # end if 
# end while 
