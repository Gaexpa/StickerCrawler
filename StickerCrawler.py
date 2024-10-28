import requests
from bs4 import BeautifulSoup
import json

url = 'https://steamcommunity.com/market/itemordershistogram?country=TW&language=english&currency=1&item_nameid=176420513'
pic_url = 'https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXQ9QVcJY8gulReXESCF7b5mNzSRGJzKghT-On9fFM11_aaIGkbuoTmkdnbxaL1Me3TxTMC7Jwkjr_Fp92jjgKw-hZyIzekec9Mwjs/360fx360f'

# mimic actual web user via user-agent
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36'}
response = requests.get(url, headers=headers)

global order_data

# check status
if response.status_code == 200:
	print('Writing web Success!')

	data = response.json()
	order_data = {
		'highest_buy_order':float(data['highest_buy_order'])/100,
		'lowest_sell_order':float(data['lowest_sell_order'])/100
	}
	print(order_data)

else:
	print('Didn\'t get the web :(')

def refresh():
	response = requests.get(url, headers=headers)
	# check status
	if response.status_code == 200:
		data = response.json()
		order_data = {
			'highest_buy_order':float(data['highest_buy_order'])/100,
			'lowest_sell_order':float(data['lowest_sell_order'])/100
		}

	else:
		print('Didn\'t get the web :(')
