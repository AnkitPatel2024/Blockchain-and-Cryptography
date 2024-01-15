from flask import Flask, request, jsonify
from flask_restful import Api
import json
import eth_account
import algosdk
from eth_account import Account

app = Flask(__name__)
api = Api(app)
app.url_map.strict_slashes = False


@app.route('/verify', methods=['GET', 'POST'])
def verify():
	content = request.get_json(silent=True)

	platform = content['payload']['platform']

	public_key = content['payload']['pk']

	sig_obj = content.get('sig')

	payload = json.dumps(content['payload'])

	# Check if signature is valid
	# if (platform =='Ethereum'):
	# eth_account.Account.enable_unaudited_hdwallet_features()
	# eth_encoded_msg = eth_account.messages.encode_defunct(text=payload)
	# if eth_account.Account.recover_message(eth_encoded_msg,signature=sig_obj.signature.hex()) == public_key:
	# print( "Eth sig verifies!" )
	# result = True #Should only be true if signature validates
	# else:
	# result = False

	if (platform == 'Algorand'):
		algo_sig_str = sig_obj

		if algosdk.util.verify_bytes(payload.encode('utf-8'), algo_sig_str, public_key):
			result = True

		else:
			result = False

		return jsonify(result)

	elif (platform == 'Ethereum'):

		eth_encoded_msg = eth_account.messages.encode_defunct(text=payload)

		if eth_account.Account.recover_message(eth_encoded_msg, signature=sig_obj) == public_key:
			result = True

		else:
			result = False

		return jsonify(result)

# result = True
# return jsonify(result)

if __name__ == '__main__':
	app.run(port='5002')




