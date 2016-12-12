'''
Para poder utilizar SIFT, SURF y otros algoritmos se necesitan
modulos extras de CV2 (openCV2_contrib); se pueden encontrar aqui:
https://github.com/opencv/opencv_contrib

mas informacion sobre al algrotimo en:
http://docs.opencv.org/3.1.0/da/df5/tutorial_py_sift_intro.html
'''
import cv2
import numpy as np

input_image = cv2.imread("/home/pi/Desktop/Milker_robot/image11.jpg")
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

#sift = cv2.xfeatures2d.SIFT_create() #funcion nueva
#sift = cv2.SIFT() #funcion vieja
keypoints = sift.detect(gray_image, None)

input_image = cv2.drawKeypoints(input_image, keypoints, flags = cv2.DRAW_MATCHES_RICH_KEYPOINTS)

cv2.imshow("SIFT features", input_image)
cv2.waitKey()
