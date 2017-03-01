import urllib2, json, time, sys, os, time, requests, picamera, threading
from uuid import getnode as get_mac

url = 'http://192.168.2.238:8080/data/'+str(get_mac())+'/video'
data = {
        "fichero": os.path.basename(__file__),
        "mac": get_mac()
        }
duracion_video = float(sys.argv[1])

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
                        

if __name__ == "__main__":
        Record_Video(duracion_video)
