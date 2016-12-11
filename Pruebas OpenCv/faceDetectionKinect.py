import freenect
import cv2
import numpy as np

#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

if __name__ == "__main__":
    face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_alt.xml')

    cap = get_video()
    scaling_factor = 0.5

    while True:
        cap = get_video()
        frame = cv2.resize(cap, None, fx = scaling_factor, fy = scaling_factor, interpolation = cv2.INTER_AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in face_rects:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        cv2.imshow("face Detector", frame)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cv2.destroyAllWindows()
