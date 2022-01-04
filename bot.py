import websocket

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print('Opened Connection')
    
def on_close(ws):
    print('Closed Connection')
    
def on_message(ws, message):
    print('Received Message')
    
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()