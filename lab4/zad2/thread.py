
import threading
import time


def prog1(n):
  for i in range(n):
    print('+',i)
    time.sleep(1)
    

def prog2(n):
  for i in range(n):
    print('-',i)
    time.sleep(1)



w1=threading.Thread(target=prog2,args=(10,))
w1.daemon = True
w1.start() 


prog1(10)
