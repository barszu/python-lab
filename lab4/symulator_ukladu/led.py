end = None

import tkinter as tk
import threading
import socket
from socket import AF_INET, SOCK_DGRAM


def create_led(canvas, x, y, r=8):
    return canvas.create_oval(x-r, y-r, x+r, y+r, fill="#7F0000")


def create_switch(canvas, x, y, r=10):
    return canvas.create_rectangle(x-r, y-r, x+r, y+r, fill="#FFFFFF")


def rcv():
  global server_socket
  global canvas,leds

  while True:
    (buffer, address) = server_socket.recvfrom(256)
    # print(buffer[0])
    if buffer[-1]!=0: continue
    for i in range(len(buffer)-1): 
      canvas.itemconfig(leds[i], fill= ["#7F0000","#FF0000"][buffer[i]])
    end
  end  
end

def clicked(event):
    global states,canvas,switches

    x, y = event.x, event.y
    #print(x,y)
    if y<85-6 or y>85+6: return
    x0 = round(x/35)*35
    if abs(x-x0)<=10:
      # print(x0//35-1)
      n = x0//35-1
      states[n] = 1-states[n]
      canvas.itemconfig(switches[n], fill= ["#FFFFFF","#000000"][states[n]])
      x = bytearray([states[i] for i in range(16)]+[0])
      server_socket.sendto(x, ("localhost", 9002))
 

def main():
    global canvas,leds,states,switches

    t1=threading.Thread(target=rcv)
    t1.daemon=True
    t1.start() 

    window = tk.Tk()
    canvas = tk.Canvas(window, width=600, height=160, bg='gray')
    canvas.pack()

    led_radius = 8
    start_x = start_y = 35

    switch_radius = 10
    dist = 35


    leds = []
    for i in range(16):
        led = create_led(canvas, start_x + i*dist, start_y, led_radius)
        leds.append(led)

    switches = []
    states = []
    for i in range(16):
        states.append(0)
        switch = create_switch(canvas,start_x + i*dist, start_y+50, switch_radius)
        switches.append(switch)
    end

    canvas.bind("<Button-1>", clicked)


    window.mainloop()
end

if __name__ == "__main__":
  server_socket = socket.socket(AF_INET, SOCK_DGRAM)
  server_socket.bind(("localhost", 9001))
  main()
end