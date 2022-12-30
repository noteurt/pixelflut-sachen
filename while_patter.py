import socket
import threading
import time


host = "192.168.100.222"
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def write_line(x, zurSeite):
    for x in range(x, x + 660, 1):
        inital = 2
        #print(x )
        for  y in range(zurSeite, zurSeite + 660, 10):
            if ((x // 10 % 10) % 2 == 0):
                if (inital == 1):
                    color = "ff5733"
                    inital = 2
                elif inital == 2:
                    color = "fffc33"
                    inital = 1
                else:
                    color = "FF0000"
                    inital = 1
                for keast in range (1, 11):
                    
                    stringToSend = 'PX {} {} {}\n'.format(x , y + keast, color)
                    #print(stringToSend)
                    s.send(str.encode(stringToSend))
            else:
                if (inital == 2):
                    color = "ff5733"
                    inital = 3
                elif inital == 3:
                    color = "fffc33"
                    inital = 2
                else:
                    color = "FF0000"
                    inital = 2
                for keast2 in range (1, 11):
                    stringToSend = 'PX {} {} {}\n'.format(x , y + keast2, color)
                    #print(stringToSend)
                    s.send(str.encode(stringToSend))
            #time.sleep(1)


while True:
    write_line(1140, 40)