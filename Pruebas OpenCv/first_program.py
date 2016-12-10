import cv2
img = cv2.imread('./images/input.jpg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('R image', rgb_img[:, :, 0])
cv2.imshow('G image', rgb_img[:, :, 1])
cv2.imshow('B image', rgb_img[:, :, 2])
cv2.waitKey()
