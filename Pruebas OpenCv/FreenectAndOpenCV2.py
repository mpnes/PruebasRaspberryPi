import freenect
import cv2
import numpy as np

#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

if __name__ == "__main__":
    while True:
        cap = get_video()
        cv2.imshow('Kinect', cap)
        parar = cv2.waitKey(5) #espera 5 milisegundos, regresa la tecla presionada
        #presionar "esc" para salir, esc = 27 en ASCII
        if parar == 27:
            break
    cv2.destroyWindow('Kinect')
