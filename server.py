import sys, socket
from threading import Thread

host = sys.argv[1]
port = int(sys.argv[2])

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind((host, port))
soc.listen(1)
cli, addr = soc.accept()



def RCD():
	while True:
		
		cdata=cli.recv(1024)
		print("client : "+cdata)

th = Thread(target=RCD).start()

while True:

	data = raw_input()
	cli.send("server : "data) 
