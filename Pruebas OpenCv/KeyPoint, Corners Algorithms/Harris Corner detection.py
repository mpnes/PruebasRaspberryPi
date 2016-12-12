'''
Ver tambien el algortimo de Shi-Tomasi
'''
import cv2
import numpy as np

img = cv2.imread("/home/pi/Desktop/Milker_robot/image11.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 4, 5, 0.04) #detect sharp corners
#dst = cv2.cornerHarris(gray, 14, 5, 0.04) #detect soft corners

dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 0]

cv2.imshow("Harris Corners", img)
cv2.waitKey()
