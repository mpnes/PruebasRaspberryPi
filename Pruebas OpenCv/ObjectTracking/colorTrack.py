import cv2
import numpy as np
import freenect

#function to get RGB image from kinect
def get_video():
    array,_  = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

def get_frame(cap, scaling_factor):
    frame = get_video()
    frame = cv2.resize(frame, None, fx=scaling_factor, 
            fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return frame

if __name__=='__main__':
    cap = get_video()
    scaling_factor = 0.5

    while True:
        frame = get_frame(cap, scaling_factor) 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define blue range
        lower = np.array([60,100,100])
        upper = np.array([180,255,255])

        # Threshold the HSV image to get only blue color
        mask = cv2.inRange(hsv, lower, upper)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)
        res = cv2.medianBlur(res, 5)

        cv2.imshow('Original image', frame)
        cv2.imshow('Color Detector', res)
        c = cv2.waitKey(5) 
        if c == 27:
            break

    cv2.destroyAllWindows()
