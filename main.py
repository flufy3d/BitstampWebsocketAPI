from BitstampWebsocketAPI import BitstampWebsocketAPI as bwapi
from time import sleep

def kenshin():
    client = bwapi.BitstampWebsocketAPI()


    client.subscribe("live_trades", "btc", "eur")
    #this will update client.lastprice["btc"]["eur"]
    #client.subscribe("order_book", "btc", "usd") #choose either this one, for accuracy
    #client.subscribe("diff_order_book", "btc", "usd") #or this one, for speed
    #both will keep client.orderbook["btc"]["usd"] up to date
    #client.subscribe("live_orders", "eur", "usd")
    #this will keep self.openorders["eur"]["usd"] up to date, and stores open orders
    #by id and by price
    while True:
        sleep(1)
        print(client.lastprice["btc"]["eur"])


import pysher

import json


index = 0.00000001

def channel_callback(data):
    global index
    print("Channel Callback: %s" % data)
    print("time %.2fs" % (index/100.0))
    index = 0

def connect_handler(data):
    print('connceted!')
    channel = pusher.subscribe("live_orders_bchusd")
    print(channel)

    channel.bind('order_created', channel_callback)


if __name__ == '__main__':


    appkey = "de504dc5763aeef9ff52"

    pusher = pysher.Pusher(appkey)

    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

    while True:
        index += 1
        sleep(0.01)

