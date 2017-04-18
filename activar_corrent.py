import RPi.GPIO as GPIO
import sys, os

GPIO.setmode(GPIO.BCM)
pin = int(sys.argv[1])
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)