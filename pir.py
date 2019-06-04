import RPi.GPIO as GPIO
import time
import datetime
from picamera import PiCamera
import send_sms
SENSOR_PIN = 23

# for record video in CLI
# raspivid -o record.h264 -t 3000
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
count = 0
i = 0
camera = PiCamera()

def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    global count
    count = count + 1
    global i 
    if (count > 1):
        notif = "There was a movement at " +  str(datetime.datetime.now().strftime("%H:%M:%S (%Y-%m-%d)"))
        print(notif)
        #send_sms.send_text("+19495465129", notif, None)
        send_sms.send_text("+19495465129", notif, None)
        print("Taking picture(s)!");
        camera.capture('/home/pi/Desktop/storage/image%s.jpg' % i)
        i = i + 1
        count = 0

try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    print ("Finish...")
GPIO.cleanup()

