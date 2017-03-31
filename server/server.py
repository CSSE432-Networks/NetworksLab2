# Networks lab2
# Jesse Shellabarger & Tayler How

import socket
import re

serverPort = int(raw_input("Enter the local port "))
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
    connectionSocket, addr = serverSocket.accept()
    command = connectionSocket.recv(256)
    
    if(command.startswith('iWant')):
        pattern = re.compile("iWant (.*)")
        if(not pattern.match(command)):
            print "Invalid iWant received"
            connectionSocket.send("Not Ready")
            break
        connectionSocket.send("Ready")
        filename = command.split(" ")[1]
        file = open('store/'+filename,'rb')
        line = file.read(1024)
        while (line):
            connectionSocket.send(line)
            line = file.read(1024)
        #serverSocket.shutdown(socket.SHUT_WR)
        print filename + " sent to client"
        file.close()
        
    elif(command.startswith('uTake')):
        pattern = re.compile("uTake (.*)")
        if(not pattern.match(command)):
            print "Invalid uTake received"
            serverSocket.send("Not ready")
            break
        
        file = open('store/'+command.split(" ")[1],'wb')
        
        connectionSocket.send("Ready")
        
        line = connectionSocket.recv(1024)
        while (line):
            file.write(line)
            line = connectionSocket.recv(1024)
        file.close()
        print command.split(" ")[1] + " received"
        
    else:
        print "Invalid command received. Ignoring"

    connectionSocket.close()