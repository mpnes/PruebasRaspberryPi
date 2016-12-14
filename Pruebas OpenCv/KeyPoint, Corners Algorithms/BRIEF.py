'''
Usando BRIEF junto con FAST creamos algo muy rapido al momento de detectar y "compute" los kp
'''

import cv2
import numpy as np

gray_image = cv2.imread("/home/pi/Desktop/Milker_robot/image11.jpg", 0)

fast = cv2.FastFeatureDetector_create()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

keypoints = fast.detect(gray_image, None)

keypoints, descriptors = brief.compute(gray_image, keypoints)

gray_keypoints = gray_image
gray_keypoints = cv2.drawKeypoints(gray_image, keypoints, color = (0, 255, 0), outImage = gray_keypoints)

cv2.imshow("BRIEF", gray_keypoints)
cv2.waitKey()
cv2.destroAllWindows()
