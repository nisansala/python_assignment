import sys, socket
from threading import Thread

host = sys.argv[1]
port = int(sys.argv[2])

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, port))



def RSD():
	while True:
		
		sdata=soc.recv(1024)
		print("server : "+sdata)

th2 = Thread(target=RSD).start()

while True:

	data = raw_input()
	soc.send("client : "data) 
