import cv2

img = cv2.imread('kucing.jpg')
blue_band = img[:, :, 0]  
green_band = img[:, :, 1]  
red_band = img[:, :, 2]    
cv2.imshow('Blue Band', blue_band)
cv2.imshow('Green Band', green_band)
cv2.imshow('Red Band', red_band)
cv2.waitKey(0)
cv2.destroyAllWindows()
