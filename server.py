
from socket import *
import argparse 
import pathlib
import os
import sys



if len(sys.argv) != 2:
    print("Incorrect number of arguments")
    sys.exit(1)


parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str) 
args = parser.parse_args()


input_file = args.input_file

if input_file[len(input_file)-4:] != ".txt":
    print("Text file not inputed")
    sys.exit(1)

file_root= "input_file"

file=os.path.join(file_root, input_file)

if not os.path.isfile(file):
    print("File does not exist")
    sys.exit(1)


if not os.access(file, os.R_OK):
    print("File can not be acessed")
    sys.exit(1)


try:
    fd = open(file, "r")

except Exception as e: 
    print ("Error in opening the file")
    sys.exit(1) 


if not fd.readable():
    print("The file is not readable")
    sys.exit(1)

try:
    contents = fd.read()
    fd.close()

except Exception as e: 
    print ("Error in reading the file")
    sys.exit(1) 


if len(contents) > 80:
    print("File should be no more than 80 characters")
    sys.exit(1)

serverName = gethostname()
ip_adress = gethostbyname(serverName)
print("Server Name: ", serverName)

serverPort = 12023

try:
    serverSocket = socket(AF_INET, SOCK_STREAM)
except error as e: 
    print ("Error in socket creation") 
    sys.exit(1) 

try:
    serverSocket.bind((ip_adress,serverPort))
except error as e: 
    print ("Error in socket binding, server already exists") 
    sys.exit(1) 


serverSocket.listen(50)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        connectionSocket.sendall(contents.encode('utf-8'))
    except error as e: 
        print ("Error in sending data") 
        sys.exit(1) 
    try:
        connectionSocket.close()
    except error as e:      
        print ("Error in closing socket") 
        sys.exit(1) 

    



