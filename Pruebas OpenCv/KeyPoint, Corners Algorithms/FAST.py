'''
requiere CV2_contrib

Detecta rapidamente los keypoints (kp)
'''
import cv2
import numpy as np

gray_image = cv2.imread("/home/pi/Desktop/Milker_robot/image11.jpg", 0)

fast = cv2.FastFeatureDetector_create()

keypoints = fast.detect(gray_image, None)
print("Number of keypoints with non max supression: ", len(keypoints))

img_keypoints_with_nonmax = gray_image
img_keypoints_with_nonmax = cv2.drawKeypoints(gray_image, keypoints, color = (0, 255, 0), outImage = img_keypoints_with_nonmax)
cv2.imshow("FAST Keypoints - with non max supressions", img_keypoints_with_nonmax)

fast.setNonmaxSuppression(0)
keypoints = fast.detect(gray_image, None)

print("Total keypoints without nonmaxSupression: ", len(keypoints))

img_keypoints_without_nonmax = gray_image
img_keypoints_without_nonmax = cv2.drawKeypoints(gray_image, keypoints, color = (0, 255, 0), outImage = img_keypoints_without_nonmax)
cv2.imshow("Without", img_keypoints_without_nonmax)

cv2.waitKey()
cv2.destroyAllWindows()
