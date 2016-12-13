import cv2
import numpy as np

img = cv2.imread("/home/pi/Desktop/PruebasRaspberryPi/Pruebas OpenCv/images/img.jpg")

cv2.imshow("img", img)

arr = img[180:350, 50:250]

#rotar la imagen
num_rows, num_cols = arr.shape[:2]

rotation = cv2.getRotationMatrix2D((num_cols /2, num_rows/2), 90, 1)
img_rotation = cv2.warpAffine(arr, rotation, (num_cols, num_rows))
cv2.imshow("crop rotated", img_rotation)
cv2.imwrite("/home/pi/Desktop/PruebasRaspberryPi/Pruebas OpenCv/images/cropRotated.jpg", img_rotation)

cv2.imshow("crop", arr)
cv2.imwrite("/home/pi/Desktop/PruebasRaspberryPi/Pruebas OpenCv/images/crop.jpg", arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
