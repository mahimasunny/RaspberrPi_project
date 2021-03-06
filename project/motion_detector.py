import RPi.GPIO as gpio
import io
import picamera
import cv2
import time
import numpy
import face_recognition_impl
from IPython.display import display
from PIL import Image, ImageDraw

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.MIMEText import MIMEText
# from email.mime.MIMEBase import MIMEBase
# from email import encoders
# from email.mime.image import MIMEImage
 
# fromaddr = "mahimasunnym@gmail.co"    # change the email address accordingly
# toaddr = "mahimasunnym@gmail.com"
 
# mail = MIMEMultipart()
 
# mail['From'] = fromaddr
# mail['To'] = toaddr
# mail['Subject'] = "Attachment"
# body = "Please find the attachment"

led=17
pir=18
HIGH=1
LOW=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)            # initialize GPIO Pin as outputs
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input
data=""

# def sendMail(data):
#     mail.attach(MIMEText(body, 'plain'))
#     print(data)
#     dat='%s.jpg'%data
#     print(dat)
#     attachment = open(dat, 'rb')
#     image=MIMEImage(attachment.read())
#     attachment.close()
#     mail.attach(image)
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(fromaddr, "maredonrocks33")
#     text = mail.as_string()
#     server.sendmail(fromaddr, toaddr, text)
#     server.quit()

def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    # camera.start_preview()
    # time.sleep(5)
    #Create a memory stream so photos doesn't need to be saved in a file
    stream = io.BytesIO()

    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture(stream, format='jpeg')

    #Convert the picture into a numpy array
    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
    #Now creates an OpenCV image
    image = cv2.imdecode(buff, 1)
    pil_image = Image.fromarray(image)
    pil_image.save("./output/motion_detected.jpg") 
    if not face_recognition_impl.check_if_known_face('./output/motion_detected.jpg'):
        print("Intruder detected")

gpio.output(led , 0)
i=0
while 1:
    if gpio.input(pir)==1:
        gpio.output(led, HIGH)
        capture_image()
        while(gpio.input(pir)==1):
            time.sleep(1)
        
    else:
        gpio.output(led, LOW)
        time.sleep(0.01)
    # i+=1 

