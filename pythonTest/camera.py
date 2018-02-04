from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('/home/pi/Documents/pythonTest/photo.jpg')
camera.stop_preview()
