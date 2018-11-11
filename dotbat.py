import socket
import ssl
import os
from web3 import Web3, HTTPProvider
import csv

web3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/f02b45891a7a4a2dbd3f3913f690b719'))
contract_abi = '[{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_datName","type":"string"},{"name":"_URL","type":"string"}],"name":"addDat","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_datName","type":"string"}],"name":"getDatURL","outputs":[{"name":"URL","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_datName","type":"string"}],"name":"removeDat","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"}],"name":"OwnershipTransferred","type":"event"}]'

contract = web3.eth.contract(
    address = "0x43C605A5C30169d775a585c58E8bA1e74D253e9D",
    abi=contract_abi
)

def get_dat_url(dat_name):
    id = contract.functions.getDatURL(dat_name).call()
    return id


print(get_dat_url("make me rich"))



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

	if b'ID options' in msg:
		with open('names.csv', 'r') as IDs:
			reader = csv.reader(IDs, delimiter=',')
			for row in reader:
				ws.send(str.encode(row)+b',')

	if b'download' in msg:
		file = (((msg.decode('utf-8')).split("download"))[1].split('\''))[1]
		directory = ''.join([i for i in str(os.system('find . -name' + '\'' + file + '\'')).split('0')[0]][2:])
		ws.send(b'Directory \''+str.encode(directory)+b'\'')

