import cv2
import numpy as np

img = cv2.imread('/home/pi/Documents/Pruebas OpenCv/images/pruebas.jpg')
rows, cols = img.shape[:2]

kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
kernel_5x5 = np.ones((5, 5), np.float32) / 25.0

cv2.imshow('Original', img)

output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('identity filter', output)

output = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('kernel_3x3 filter', output)

output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow('kernel_5x5 filter', output)

output = cv2.blur(img, (8, 8)) #manera rápida
cv2.imshow('blur 8x8', output)

cv2.waitKey(0)

