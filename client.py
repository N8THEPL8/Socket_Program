from socket import *
import argparse 
import pathlib
import os
import sys


if len(sys.argv) != 3:
    print("Incorrect number of arguments")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('server', type=str) 
parser.add_argument('output_file', type=str) 
args = parser.parse_args()




serverName = args.server
output_file = args.output_file


if output_file[len(output_file)-4:] != ".txt":
    print("Text file not inputed")
    sys.exit(1)



file_root="output_file"
file=os.path.join(file_root, output_file) 

if not os.path.isfile(file):
    print("File does not exist")
    sys.exit(5)


try:
    ip_adress = gethostbyname(serverName)
except Exception as e:
    print("Error in getting ip adress, make sure server name is correct")
    sys.exit(1)
serverPort =  12023
try:
    clientSocket = socket(AF_INET,SOCK_STREAM)
except error as e: 
    print ("Error in socket creation") 
    sys.exit(1) 

try:
    clientSocket.connect((ip_adress,serverPort))
except error as e: 
    print ("Error in socket connection, socket does not exist") 
    sys.exit(1) 





try:
    modifiedSentence = clientSocket.recv(1024).decode('utf-8')
except error as e: 
    print ("Error in socket reciving") 
    sys.exit(1) 


clientSocket.close()





try:
    fd2 = open(file, "w")
except Exception as e: 
    print ("Error in opening the file") 
    sys.exit(1) 
if not (fd2.writable()):
    print("The file is not writable")
    sys.exit(1)
try:
   fd2.write(modifiedSentence)
   fd2.close()
except Exception as e: 
   print ("Error in writing to the file") 


print("done")
