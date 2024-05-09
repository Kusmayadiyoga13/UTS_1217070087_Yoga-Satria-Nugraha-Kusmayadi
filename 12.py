import cv2
import numpy as np

image = cv2.imread('kucing.jpg')
brightness_increase = 100
brightened_image = cv2.add(image, np.array([brightness_increase]))
cv2.imshow('Original Image', image)
cv2.imshow('Brightened Image', brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
