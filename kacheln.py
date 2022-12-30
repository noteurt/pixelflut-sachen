import socket
import threading
import time


host = "192.168.100.222"
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def write_line(amountX, amountY):
    xAchse = 0
    yAchse = 0
    for kacheln in range(0, amountY):
        for kacheln in range(0, amountX): 
            for x in range(xAchse, xAchse + 100, 1):
                inital = 2
                for  y in range(yAchse, yAchse + 100, 10):
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
            xAchse = xAchse + 110
        xAchse = 0
        yAchse = yAchse + 110


while True:
    write_line(10, 10)