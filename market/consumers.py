from channels import Group
from .models import Stocks

import json


# Connected to websocket.connect
def ws_add(message):
	message.reply_channel.send({"accept": True})
	Group("charts").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
	stock_list = list(Stocks.objects.values_list('name', flat=True))
	req = json.loads(message.content['text'])
	if req['text'] == 'get-init':
		# import pdb;pdb.set_trace()
		message.reply_channel.send({
			'text': json.dumps({"results" : [x for x in stock_list], 'type': 'init' }),
			'accept' : True
		})
	elif req['text'] == 'add':
		Stocks.objects.create(name = req['payload'])
		stock_list.append(req['payload'])
		Group("charts").send({
			'text': json.dumps({"results" : [x for x in stock_list], 'type' : 'update' }),
		})

# Connected to websocket.disconnect
def ws_disconnect(message):
	Group("charts").discard(message.reply_channel)