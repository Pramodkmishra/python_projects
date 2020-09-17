import socket
import threading
soc=socket.socket()
port=12345
#ip=input("Enter Server IP Address=")
uname=input("Enter user name::")
def recmsg(sock):
	while True:
		msg=sock.recv(1024)
		print msg
soc.connect((socket.gethostname(),port))
soc.send(uname)
threading.Thread(target = recmsg, args=(soc,)).start()

while True:
	msg=input()
	msg=uname + ">>" +msg
	soc.send(msg)


