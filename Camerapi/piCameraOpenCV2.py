from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.rotation = 180
#camera.resolution = (640, 480)
#camera.framerate = 32
rawCapture = PiRGBArray(camera)#, size = (640, 480))

time.sleep(0.1)
scaling_factor = 0.5
for frame in camera.capture_continuous(rawCapture, format = "bgr", use_video_port = True):

    image = frame.array
    frame = cv2.resize(image, None, fx = scaling_factor, fy = scaling_factor, interpolation = cv2.INTER_AREA)
    cv2.imshow("PiCamera", frame)

    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    
    if key == 27:
        break

cv2.destroyAllWindows()
