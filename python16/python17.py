
host = "127.168.2.75"
port=4446               
from socket import *           
server=socket(AF_INET, SOCK_STREAM)    
server.connect((host,port))         
message=server.recv(1024)            
print ("Message from server : " + msg.strip().decode('ascii'))
server.close()                           
