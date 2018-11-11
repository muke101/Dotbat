import urllib.request
import socket
import ssl
import sys
import time

file = sys.argv[1]
server = str(sys.argv[2])
s = socket.socket()
s.settimeout(60)
ws = ssl.wrap_socket(s)
ws.connect((server, 6697))
ws.send(b"USER BATDOT BATDOT BATDOT: bot for DAT commands\n\r")
ws.send(b"NICK BATDOT\n\r")
ws.send(b"JOIN #bots\n\r")
ws.send(b'ID options\n\r')

while True:
	msg = ""
	try:
		msg = ws.recv(8291)
	except socket.timeout:
		pass
	msg = msg.strip(b'\n\r')
	print(msg.decode('utf-8'))
	if b"PING" in msg:
		ws.send(b"PONG\n\r")
	if b"sending IDs" in msg:
		options = (msg.decode('utf-8')).split(',')
		IDs = {c:i for c, i in enumerate(options)}
		print(IDs)
		choice = input("select ID")
		ID = IDs[choice]
		ws.send(b"download "+str.encode(file))
	if b"Directory" in msg:
		directory = (((msg.decode('utf-8')).split('Directory'))[1].split('\''))[1]
		download = urlib.request.urlretrieve(file+ID+directory)
		downloadfile = open(file, 'wb')
		meta = download.info() 
		size = int(meta.getheaders("Content-Length")[0])
		print("Downloading: %s Bytes: %s" % (file, size))
		size_dl = 0
		block_sz = 8192 
		while True:
			buffer = download.read(block_sz)
			if not buffer:
				break 
			size_dl+= len(buffer)
			downloadfile.write(buffer)
			status = r"%10d  [%3.2f%%]" % (size_dl, size_dl * 100. / size)
			status = status + chr(8)*(len(status)+1)
			print(status)
		downloadfile.close()

