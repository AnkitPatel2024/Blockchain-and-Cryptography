from web3 import Web3
from web3.contract import Contract
from web3.providers.rpc import HTTPProvider
import requests
import json
import time

bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
contract_address = Web3.toChecksumAddress(bayc_address)

#You will need the ABI to connect to the contract
#The file 'abi.json' has the ABI for the bored ape contract
#In general, you can get contract ABIs from etherscan
#https://api.etherscan.io/api?module=contract&action=getabi&address=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D
with open('/home/codio/workspace/abi.json', 'r') as f:
	abi = json.load(f) 

############################
#Connect to an Ethereum node
#token = "Mwb3juVAfI1g2RmA1JCGdYk-2_BmFrnLOtbomP1oDa4"
#api_url = f"https://c2emjgrvmi7cabd41mpg.bdnodes.net?auth={token}"
token = "29b079b2d75342509ffde033fdf47609"           #API key
api_url =f"https://mainnet.infura.io/v3/29b079b2d75342509ffde033fdf47609?auth={token}"      #YOU WILL NEED TO TO PROVIDE THE URL OF AN ETHEREUM NODE

provider = HTTPProvider(api_url)
web3 = Web3(provider)

def get_ape_info(apeID):
	assert isinstance(apeID,int), f"{apeID} is not an int"
	assert 1 <= apeID, f"{apeID} must be at least 1"
	#print(apeID);
	data = {'owner': "", 'image': "", 'eyes': "" }
	
	#YOUR CODE HERE	
	contract = web3.eth.contract(address=contract_address,abi=abi)

	owner_a = contract.functions.ownerOf(apeID).call();

	token_uri = contract.functions.tokenURI(apeID).call();
	
	data['owner']= owner_a;
	
	token_url_mod = token_uri.split("//");
	full_addr = 'https://gateway.pinata.cloud/ipfs/' + token_url_mod[1];

	r = requests.get(full_addr)

	data_all = json.loads(r.text)
	#print(data_all);
	#print(type(data_all));

	image_a = data_all.get("image");

	data['image'] = image_a;
	#print(data);
	
	list_attr = data_all.get("attributes");
	#print(list_attr);
	length = len(list_attr);
	eye_info = list_attr[1];
	#print(eye_info.keys());
	
	for i in range(length):
		if list_attr[i].get("trait_type") == "Eyes":
			eyes_a = list_attr[i].get("value")
	
	data['eyes'] = eyes_a;
	
	#print(data);
			  
	assert isinstance(data,dict), f'get_ape_info{apeID} should return a dict' 
	assert all( [a in data.keys() for a in ['owner','image','eyes']] ), f"return value should include the keys 'owner','image' and 'eyes'"
	return data
	
	



