import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

def turn_on_red_light():
    GPIO.output(14,GPIO.HIGH)

def turn_off_red_light():
    GPIO.output(14,GPIO.LOW)

def turn_on_green_light():
    GPIO.output(18,GPIO.HIGH)

def turn_off_green_light():
    GPIO.output(18,GPIO.LOW)

def red_light(sec):
    GPIO.output(14,GPIO.HIGH)
    sleep(sec)
    GPIO.output(14,GPIO.LOW)

def green_light(sec):
    GPIO.output(18,GPIO.HIGH)
    sleep(sec)
    GPIO.output(18,GPIO.LOW)

