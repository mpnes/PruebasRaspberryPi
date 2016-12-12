import cv2
import numpy as np

img = cv2.imread('/home/pi/Documents/Pruebas OpenCv/images/pruebas.jpg')
kernel = np.ones((5, 5), np.uint8)

#iteration = cuanto se quiere dilatar o erosionar
img_erosion = cv2.erode(img, kernel, iterations = 1)
img_dilation = cv2.dilate(img, kernel, iterations = 1)

cv2.imshow('input', img)
cv2.imshow('erosion', img_erosion)
cv2.imshow('dilation', img_dilation)

cv2.waitKey(0)
