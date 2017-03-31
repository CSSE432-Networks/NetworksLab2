# Networks lab2
# Jesse Shellabarger & Tayler How

from socket import *
import re
import os

serverName = raw_input("Enter the server's IP ")
serverPort = int(raw_input("Enter the server's port "))

while(1): 
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    
    command = raw_input(':> ')
    if (command.startswith("iWant")):
        clientSocket.send(command)
        
        confirm = clientSocket.recv(256)
        if (not confirm == "Ready"):
            print "Invalid iWant command"
            break

        file = open('received/'+command.split(" ")[1],'wb')

        line = clientSocket.recv(1024)
        while (line):
            file.write(line)
            line = clientSocket.recv(1024)
        file.close()
        print command.split(" ")[1] + " received"
        
    elif (command.startswith("uTake")):
        clientSocket.send(command)
        
        confirm = clientSocket.recv(256)
        if (not confirm == "Ready"):
            print "Invalid uTake command"
            break
        
        filename = command.split(" ")[1]
        currentDir = os.getcwd()
        qualifiedFilename = currentDir+'/received/'+filename
        if (not os.path.isfile(qualifiedFilename)):
            print "No such file exists."
            break
        
        file = open(qualifiedFilename,'rb')
        line = file.read(1024)
        while (line):
            clientSocket.send(line)
            line = file.read(1024)
            
        file.close()
        print filename + " sent to server"
    else:
        print "Invalid command"

    clientSocket.close()
