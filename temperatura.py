import Adafruit_DHT, sys, os, urllib2, json
from time import sleep
from threading import Thread
from uuid import getnode as get_mac

sensor = Adafruit_DHT.DHT11
pin = int(sys.argv[1])
frec = float(sys.argv[2])*60
if frec < 60:
	frec = 60
url = "http://192.168.2.105:8080/data/add"
data = {"fichero": os.path.basename(__file__), "mac": get_mac(), "valor": ""}

def Send(value):
	data["valor"] = value
	req = urllib2.Request(url)
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))

if __name__ == "__main__":
	while True:
		temperature = Adafruit_DHT.read_retry(sensor, pin)
		if temperature is not None:
			temp = '{0:0.1f}'.format(temperature[1])
			Thread(target = Send, args=(temp,)).start()
		sleep(frec)