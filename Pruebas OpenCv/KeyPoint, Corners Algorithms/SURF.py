'''
Mas rapido que SIFT pero sin toda la precision
'''
import cv2
import numpy as np

if __name__ == "__main__":
	img = cv2.imread("/home/pi/Desktop/Milker_robot/image2.jpg")
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	surf = cv2.xfeatures2d.SURF_create()
	surf.setHessianThreshold(15000)
	
	kp, des = surf.detectAndCompute(gray, None)
	
	img = cv2.drawKeypoints(img, kp, None, (0, 255, 0), 4)
	
	cv2.imshow("SURF", img)
	cv2.waitKey()
	cv2.destroyAllWindows()
