import socket
import ssl
import os

s = socket.socket()
s.settimeout(60)
ws = ssl.wrap_socket(s)

ws.connect(('192.168.0.101', 6697))
ws.send(b"USER DOTBAT DOTBAT DOTBAT: bot for DAT commands\n\r")
ws.send(b"NICK DOTBAT\n\r")
ws.send(b"JOIN #bots\n\r")

while True:
	msg = ""
	msg = ws.recv(4096)
	msg = msg.strip(b'\n\r')
	print(msg.decode('utf-8'))
	if b"PING" in msg:
		ws.send(b"PONG\n\r")

