import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	jstonStr = json.dumps(data)
	files = {
	'file': jstonStr
	}
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=('2FVUX6FruMiR12OhR9FALKgmZaD','c16c5170bc376381c339d4892f908b06'))
	p = response.json()
	cid = p['Hash']
	#cid = response.text
	#print(cid)
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	params = (('arg', cid),)
	#print(cid)
	response = requests.post('https://ipfs.infura.io:5001/api/v0/cat', params=params, auth=('2FVUX6FruMiR12OhR9FALKgmZaD','c16c5170bc376381c339d4892f908b06'))
	#print(response)
	#print(response.text)
	data = response.json()
	#data = json.loads(response)
	#print(data)
	#data = json.loads(jdata)
	#print("gets here3")
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data


