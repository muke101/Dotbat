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
	if b'download' in msg:
		file = (((msg.decode('utf-8')).split("download"))[1].split('\''))[1]
		directory = ''.join([i for i in str(os.system('find . -name' + '\'' + file + '\'')).split('0')[0]][2:])
		ws.send(b'Directory \''+str.encode(directory)+b'\'')

# from web3 import Web3, HTTPProvider

# #create instance of web3 object connected to the Ethereum Ropsten test network
# web3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/f02b45891a7a4a2dbd3f3913f690b719'))

# #store the JSON interface of the smart contract
# contract_abi = '[{"constant":false,"inputs":[{"name":"_name","type":"string"}],"name":"removeDatName","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"string"},{"name":"_datId","type":"string"}],"name":"addDatName","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_name","type":"string"}],"name":"getDatId","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"}],"name":"OwnershipTransferred","type":"event"}]'

# #create instance of the DAT name service smart contract
# contract = web3.eth.contract(
#     address = "0x68f8f849Df2faEe01639aadeEb98828B6B53262F",
#     abi=contract_abi
# )

# #function returns the DAT ID of string. If the string does not exist on the smart contract
# #then an empty string will be returned
# def get_dat_id(dat_name):
#     id = contract.functions.getDatId(dat_name).call()
#     return id



# print(get_dat_id("dat_gif"))