import socket

s = socket.socket()
host = socket.gethostname()
port = 4444
s.bind ((host,port))

s.listen(5)
client = None

while True:
    if client is None:
        print ("Waiting ...")
        client,addr = s.accept()
        print ("Connected to ",addr)
    else:
        print ("Waiting ...")
        print ("Client: ",client.recv(1024).decode())
        q = input("Enter message to Client: ")
        client.send(q.encode())

