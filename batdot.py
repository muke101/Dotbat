import urllib.request
import socket
import ssl
import sys
import time

mode = input("what would you like to do ")
file = sys.argv[1]
server = str(sys.argv[2])
s = socket.socket()
s.settimeout(60)
ws = ssl.wrap_socket(s)
ws.connect((server, 6697))
ws.send(b"USER BATDOT BATDOT BATDOT: bot for DAT commands\n\r")
ws.send(b"NICK BATDOT\n\r")
time.sleep(7)
ws.send(b'NOTICE DOTBAT '+str.encode(mode)+str.encode(file)+'\n\r')
ID ='eda6a77fd4da9444bf5b7afb254310687f3e6d8145d784f8ffb926131099644a' #default, gets changed

while True:
	try:
		msg = ""
		msg = ws.recv(4096)
		msg = msg.strip(b'\n\r')
		print(msg.decode('utf-8'))
		if b"PING" in msg:
			ws.send(b"PONG\n\r")
		if b"sending IDs" in msg:
			options = (msg.decode('utf-8')).split(',')
			print("hello")
			IDs = {c:i for c, i in enumerate(options)}
			print(IDs)
			choice = input("select ID")
			ID = IDs[choice]
			ws.send(b"download "+str.encode(file))
		if b"Directory" in msg:
			directory = (((msg.decode('utf-8')).split('Directory'))[1].split('\''))[1]
			print(directory)
			download = urllib.request.urlretrieve('http://'+server+':3000/'+ID+directory)
			downloadfile = open(file, 'wb')
			size_dl = 0
			block_sz = 8192 
			while True:
				buffer = download.read(block_sz)
				if not buffer:
					break 
				size_dl+= len(buffer)
				downloadfile.write(buffer)
				status = status + chr(8)*(len(status)+1)
				print(status)
			downloadfile.close()
		if b'upload' in msg:
			os.system('echo' + file + '>> demo')
			print(os.system('dat dat://'+ID+'./demo --http --sparse'))

	except socket.timeout:
		pass

