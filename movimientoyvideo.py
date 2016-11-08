import urllib2, json, time, sys, os, time, requests, picamera
from uuid import getnode as get_mac
import threading, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIN_MOVIMIENTO = int(sys.argv[1])
GPIO.setup(PIN_MOVIMIENTO, GPIO.IN)

url = 'http://192.168.2.192:8080/data/'+str(get_mac())+'/video'
data = {
        "fichero": os.path.basename(__file__),
        "mac": get_mac()
        }
espera_nuevo_aviso = float(sys.argv[2])
duracion_video = float(sys.argv[3])

def sendVideo():
    from subprocess import Popen, PIPE
    process = Popen(['MP4Box', '-fps','30', '-add', os.getcwd()+'/video.h264', os.getcwd()+'/video.mp4'])
    process.wait()    
    files = {'file': open('video.mp4')}
    response = requests.post(url, data=data, files=files)
    os.remove(os.getcwd()+'/video.h264')
    os.remove(os.getcwd()+'/video.mp4')

def Record_Video(duracion):
    with picamera.PiCamera() as picx:
        picx.start_preview()
        picx.start_recording('video.h264')
        picx.wait_recording(duracion)
        picx.stop_recording()
        picx.stop_preview()
        picx.close()
    sendVideo();

def Movimiento_Infrarojos(espera_nuevo_aviso, duracion_video):
        while True:
                if GPIO.input(PIN_MOVIMIENTO):
                        time.sleep(0.5)
                        Record_Video(duracion_video)
                        time.sleep(espera_nuevo_aviso)
                else:
                        time.sleep(1)
                        

if __name__ == "__main__":
        Movimiento_Infrarojos(espera_nuevo_aviso, duracion_video)
