import websocket, json, pprint

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

closes = []

def on_open(ws):
    print('Opened Connection')
    
def on_close(ws):
    print('Closed Connection')
    
def on_message(ws, message):
    global closes
    
    print('Received Message')
    json_message = json.loads(message)
    pprint.pprint(json_message)
     
    candle = json_message['k']
    
    is_candle_closed = candle['x']
    close = candle['c']
    
    if is_candle_closed:
        print("Candle Closed at {}".format(close))
        close.append(float(close))
        print("Closes")
        print(closes)
                              
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
