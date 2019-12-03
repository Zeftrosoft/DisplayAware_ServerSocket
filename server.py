from websocket_server import WebsocketServer
from datetime import date
from datetime import time
from datetime import datetime
from pymongo import MongoClient
from urllib.parse import quote_plus
import time
# Called for every client connecting (after handshake)


def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 10:
		# message = message[:200]+'..'
		print("Data received from client "+str(message))
		data = str(message).split(';')
		print("Device Id: " + data[2])
		print("Gps Data: " + data[4])
		if(data[4]):
			gps = data[4].split('+')
			print("Lat: "+gps[2])
			print("Long: "+gps[3])
			print("Speed: "+gps[4])
			print("Heading: "+gps[5])
			print("EventId: "+gps[6])
			print("Battery Voltage: "+gps[7])
			print("Sequence: "+gps[8])
			data_type = data[3]
			imei = data[2]
			lat = gps[2]
			longitude = gps[3]
			speed = gps[4]
			event = gps[6]
			battery = gps[7]

			# MT;6;868446031850114;R0;2+190924185739+42.21552+-85.62254+61.67+90+2+4182+41.
			# MT;6;868446031850114;R2;190924185959+260,63112,11217,310+4+4182+55
			if(data_type == 'R0' and lat != 0 and longitude != 0):
				t = datetime.now()
				print("time", t)
				hour = t.hour
				minute = t.minute
				second = t.second
				day = t.day
				month = t.month
				year = t.year
				print("hour,time,second,day", hour, minute, second, day, month, year)
				'''user = quote_plus('azizahtas')
				pwd = quote_plus('gF0aiUCmNyag3gCQ')
				client = MongoClient("mongodb://{}:{}@cluster0-shard-00-00-eq3rd.mongodb.net:27017,cluster0-shard-00-01-eq3rd.mongodb.net:27017,cluster0-shard-00-02-eq3rd.mongodb.net:27017/locationDb?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority".format(user, pwd))
				#db = client.locationdb
				db = client["locationdb"]
				print("connection established", db)
				mycol = db["geo_location_10"]
				mydict = {"imei": data[2], "lat": gps[2], "longitude": gps[3],"speed": gps[4], "event": gps[6], "battery": gps[7]}
				x = mycol.insert_one(mydict)
				print("data inserted")'''
				time.sleep(5)
			print("Client(%s) said: %s" % (client['id'], message))
PORT=9001
server = WebsocketServer(PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
