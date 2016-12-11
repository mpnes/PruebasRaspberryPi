import freenect
import cv2
import numpy as np

#function to get RGB image from kinect
def get_video():
    array, otro = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

img = get_video()

canny = cv2.Canny(img, 50, 240) #imagen, low trshold value, high treshold
cv2.imshow("original", img)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
