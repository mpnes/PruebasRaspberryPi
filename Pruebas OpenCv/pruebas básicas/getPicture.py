import cv2
import freenect
import time

def get_video():
    array,_  = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

img = get_video()
cv2.imshow("img", img)
cv2.imwrite("/home/pi/Desktop/PruebasRaspberryPi/Pruebas OpenCv/images/img2.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
