'''
Es mejor que el algoritmo de Harris , busca solo un cierto numero de esquinas
Tanto este como el Harris algorithm son suceptibles al tamaño
'''
import cv2
import numpy as np

img = cv2.imread("/home/pi/Desktop/Milker_robot/image11.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 30, 0.05, 25) #el segundo parametro dicta cuantas esquinas se deben buscar
corners = np.float32(corners)

for item in corners:
    x, y = item[0]
    cv2.circle(img, (x, y), 5, 255, -1)

cv2.imshow("Top 'k' features", img)
cv2.waitKey()
