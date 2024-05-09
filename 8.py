import cv2

img_hsv = cv2.imread('kucing.jpg', cv2.IMREAD_COLOR)
h, s, v = cv2.split(img_hsv)
cv2.imshow('Hue', h)
cv2.imshow('Saturation', s)
cv2.imshow('Value', v)
cv2.waitKey(0)
cv2.destroyAllWindows()
