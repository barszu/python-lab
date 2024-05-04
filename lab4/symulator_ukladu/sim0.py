end = None

import msvcrt
import time
import sys
from random import shuffle

import socket
from socket import AF_INET, SOCK_DGRAM
import threading


UKLAD = []

with open(sys.argv[1]) as f:
  for row in f:
    # print(row)
    UKLAD.append(tuple(row.strip('\n').split('\t')))
  end
end

print(*UKLAD,sep='\n')


STAN = {}

STAN['1'] = 1
STAN['0'] = 0



def AND(*arg):
  N = len(arg)
  for i in range(N-1):
    if STAN[arg[i]]==0: 
      STAN[arg[-1]] = 0
      return
  STAN[arg[-1]] = 1 
end

def NAND(*arg):
  N = len(arg)
  for i in range(N-1):
    if STAN[arg[i]]==0: 
      STAN[arg[-1]] = 1
      return
  STAN[arg[-1]] = 0 
end


def OR(*arg):
  N = len(arg)
  for i in range(N-1):
    if STAN[arg[i]]==1: 
      STAN[arg[-1]] = 1
      return
  STAN[arg[-1]] = 0 
end

def NOR(*arg):
  N = len(arg)
  for i in range(N-1):
    if STAN[arg[i]]==1: 
      STAN[arg[-1]] = 0
      return
  STAN[arg[-1]] = 1 
end


def XOR(*arg):
  N = len(arg)
  STAN[arg[-1]] = sum([STAN[arg[i]] for i in range(N-1)])%2   # zmienic na generator
end

def XNOR(*arg):
  N = len(arg)
  STAN[arg[-1]] = 1 - sum([STAN[arg[i]] for i in range(N-1)])%2 
end

def NOT(*arg):
  N = len(arg)
  STAN[arg[1]] = 1 - STAN[arg[0]]
end


def BUF(*arg):
  N = len(arg)
  STAN[arg[1]] = STAN[arg[0]]
end

xm = None

def out(*arg):
  global xm

  x = bytearray([STAN[n] for n in arg[:-1]]+[int(arg[-1])])
  #print('==',arg,x)
  if x!=xm:
    server_socket.sendto(x, ("localhost", 9001))
    xm = x
  end
end

def init():
  for el in UKLAD:
    if el[0]=='inp': continue
    if el[0]=='out': continue
    for pin in el[1:]: 
      if pin=='1': continue
      STAN[pin]=0
    #print(*el[1:])
  end
end
  

def rcv(*arg):
  global server_socket

  while True:
    try:
      (buffer, address) = server_socket.recvfrom(256)
      #print(buffer,buffer[0])
      if buffer[-1]!=0: continue
      for i in range(len(arg)):
        STAN[arg[i]] = buffer[i]
      end  
    except:
      pass
    end
end



def sim():
  init()

  for el in UKLAD:
    if el[0]=='inp':
      #print('input',el)
      t1=threading.Thread(target=rcv,args=el[1:])
      t1.daemon=True
      t1.start() 

  while True:
    for el in UKLAD:
      if el[0]!='inp':
        eval(el[0])(*el[1:])
    end
  end

end

server_socket = socket.socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("localhost", 9002))

sim()
