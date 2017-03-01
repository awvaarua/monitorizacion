##Instalacion dependencias externas
password = "fura4468AB\n"

def restart():
    import sys, os
    python = sys.executable
    os.execl(python, python, * sys.argv)

try:
    import Adafruit_DHT
    print "Paquete importado"
except ImportError:
	print "Instalando..."
	import os
	from subprocess import Popen, PIPE
	process = Popen(['sudo', 'git', 'clone', 'https://github.com/adafruit/Adafruit_Python_DHT.git'])
	process.communicate(password)
	process.wait()
	process = Popen(['sudo', 'python', 'Adafruit_Python_DHT/setup.py', 'install'])
	output = process.communicate(password)
	process.wait()
	print output
	process = Popen(['sudo', 'rm', '-R', 'Adafruit_Python_DHT'])
	process.communicate(password)
	process.wait()
	print "Instalado"
	restart()


import sys, os, urllib2, json
from time import sleep
from threading import Thread
from uuid import getnode as get_mac

sensor = Adafruit_DHT.DHT11
pin = int(sys.argv[1])
frec = float(sys.argv[2])*60
if frec < 60:
	frec = 60
url = "http://192.168.2.238:8080/data/add"
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