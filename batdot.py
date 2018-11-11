import urlib.request
import socket
import ssl

arg = "cat.gif"
argv = "192.168.0.102/"

s = socket.socket()
s.settimeout(60)
ws = ssl.wrap_socket(s)
ws.connect(('192.168.0.101', 6697))
ws.send(b"USER BATDOT BATDOT BATDOT: bot for DAT commands\n\r")
ws.send(b"NICK BATDOT\n\r")
ws.send(b"JOIN #bots\n\r")

ws.send(b"download "+str.encode(arg))

while True:
	msg = ""
	msg = ws.recv(8291)
	msg = msg.strip(b'\n\r')
	print(msg.decode('utf-8'))
	if b"PING" in msg:
		ws.send(b"PONG\n\r")
	if b"Directory" in msg:
		directory = (((msg.decode('utf-8')).split('Directory'))[1].split('\''))[1]
		download = urlib.request.urlretrieve(argv+directory)
		file = open(arg, 'wb')
		meta = download.info()
		size = int(meta.getheaders("Content-Length")[0])
		print("Downloading: %s Bytes: %s" % (arg, size))
		size_dl = 0
		block_sz = 8192
		while True:
			buffer = download.read(block_sz)
			if not buffer:
				break
			size_dl+= len(buffer)
			file.write(buffer)
			status = r"%10d  [%3.2f%%]" % (size_dl, size_dl * 100. / size)
			status = status + chr(8)*(len(status)+1)
			print(status)
		f.close()
		s.close()
		break

