'''
ORB busca la mayor velocidad de todas
'''
import cv2
import numpy as np

input_image = cv2.imread("/home/pi/Desktop/Milker_robot/image11.jpg")
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()

kp = orb.detect(gray_image, None)

kp, ds = orb.compute(gray_image, kp)

finalKP = input_image
finalKP = cv2.drawKeypoints(input_image, kp, color = (0, 255, 0), flags = 0, outImage = finalKP)

cv2.imshow("ORB", finalKP)
cv2.waitKey()
cv2.destroyAllWindows()
