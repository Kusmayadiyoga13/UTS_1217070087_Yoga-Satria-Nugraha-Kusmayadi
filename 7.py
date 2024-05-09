import cv2

img = cv2.imread('kucing.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
