# This file implements the motion detector functionality

import RPi.GPIO as gpio
import io
import picamera
import cv2
import time
import numpy
import face_recognition_impl
from IPython.display import display
from PIL import Image, ImageDraw
import datetime

led=17
# pin 18 is connected to the PIR sensor OUT pin
pir=18
HIGH=1
LOW=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)            # initialize GPIO Pin as outputs
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input
data=""

# This function is used to capture the image when the PIR sensor detects motion
# Inpout arguments: None
# Output arguments: None
def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    print('Camera taking picture')
    camera = picamera.PiCamera()
    camera.start_preview()
    time.sleep(5)
    camera.capture('./output/motion_detected.jpg')
    camera.stop_preview()
    print('Picture saved')
    if not face_recognition_impl.check_if_known_face('./output/motion_detected.jpg'):
        print("Intruder detected")
    b = datetime.datetime.now()
    print('Total time taken is ', b-a)

gpio.output(led , 0)
i=0
while 1:
    if gpio.input(pir)==1:
        # motion detected
        # pin 18 is high
        # starting timer
        a = datetime.datetime.now()
        gpio.output(led, HIGH)
        print('Motion detected')
        capture_image()
        while(gpio.input(pir)==1):
            time.sleep(1)
        
    else:
        # motion not detected
        gpio.output(led, LOW)
        time.sleep(0.01)
    
