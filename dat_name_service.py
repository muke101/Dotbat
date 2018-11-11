from web3 import Web3, HTTPProvider

#create instance of web3 object connected to the Ethereum Ropsten test network
web3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/f02b45891a7a4a2dbd3f3913f690b719'))

#store the JSON interface of the smart contract
contract_abi = '[{"constant":false,"inputs":[{"name":"_name","type":"string"}],"name":"removeDatName","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"string"},{"name":"_datId","type":"string"}],"name":"addDatName","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_name","type":"string"}],"name":"getDatId","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"}],"name":"OwnershipTransferred","type":"event"}]'

#create instance of the DAT name service smart contract
contract = web3.eth.contract(
    address = "0x68f8f849Df2faEe01639aadeEb98828B6B53262F",
    abi=contract_abi
)

#function returns the DAT ID of string. If the string does not exist on the smart contract
#then an empty string will be returned
def get_dat_id(dat_name):
    id = contract.functions.getDatId(dat_name).call()
    return id



print(get_dat_id("dat_gif"))