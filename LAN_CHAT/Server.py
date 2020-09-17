import socket
import threading
soc=socket.socket()
serverRunning=True
ip=socket.gethostname()
port=12345
client_list={}
soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
def handleClient(client,uname):
	clientConnected=True
	keys=client_list.keys()
	while True:
		msg=client.recv(1024)
		found=False
		for name in keys:
			if('**'+name) in msg:
				msg=msg.replace('**'+name,'')
				client_list.get(name).send(msg)
				found=True
				print found
			if(not found):
				client.send("Error Msg")
		print client_list
soc.bind((ip,port))
soc.listen(5)
print "Server Ready..."
print "Ip address of Server",ip
while serverRunning:
	client,address=soc.accept()
	uname=client.recv(1024)
	print str(uname)," connected to the server"
	if(client not in client_list):
		client_list[uname]=client
		threading.Thread(target = handleClient,args=(client,uname,)).start()

