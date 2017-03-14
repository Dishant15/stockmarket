#!/usr/bin/python
import websocket, json

def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
	ws.send(json.dumps({ 
		'event': "subscribe", 
		'channel': "trades", 
		'symbol': 'tBTCUSD' 
	}))


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
    		"wss://api2.bitfinex.com:3000/ws",
            on_message = on_message,
            on_error = on_error,
            on_close = on_close
        )
    ws.on_open = on_open

    ws.run_forever()