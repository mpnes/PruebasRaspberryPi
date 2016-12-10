import cv2
import numpy as np

img = cv2.imread('/home/pi/Documents/Pruebas OpenCv/images/ima.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)

cv2.imshow('Original', img) #imagen original
cv2.imshow('Sobel horizontal', sobel_horizontal) #imagen detecetando edges horizontales
cv2.imshow('Sobel Vertical', sobel_vertical) #imagen detectando edges verticales

#manera para tanto horizontal como vertical, tiene mucho ruido en imagenes reales
laplacian = cv2.Laplacian(img, cv2. CV_64F)
cv2.imshow('Laplacian', laplacian)

#opcion para aminorar el ruido
canny = cv2.Canny(img, 50, 240) #imagen, low trshold value, high treshold
cv2.imshow('Canny', canny)

cv2.waitKey(0)

'''Motion horizontal Blurring effect kernel
    [0 0 0]
M = [1 1 1]
    [0 0 0]
'''
