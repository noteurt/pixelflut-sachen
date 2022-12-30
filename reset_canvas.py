import socket
import threading
import time


host = "192.168.100.222"
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#x ist zur seite

#y ist runter



def write_line(x, zurSeite):
    for x in range(x, 2000, 1):
        inital = 2
        #print(x )
        for  y in range(zurSeite, 1500, 10):
            if ((x // 10 % 10) % 2 == 0):
                if (inital == 1):
                    color = "00FF00"
                    inital = 2
                elif inital == 2:
                    color = "0000FF"
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
                    color = "00FF00"
                    inital = 3
                elif inital == 3:
                    color = "0000FF"
                    inital = 2
                else:
                    color = "FF0000"
                    inital = 2
                for keast2 in range (1, 11):
                    stringToSend = 'PX {} {} {}\n'.format(x , y + keast2, color)
                    #print(stringToSend)
                    s.send(str.encode(stringToSend))
    

while True:
    write_line(0, 0)
