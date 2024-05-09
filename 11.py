import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('kucing.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
hist_hue = cv2.calcHist([hsv_image], [0], None, [180], [0, 180])
plt.plot(hist_hue, color='orange')
plt.title('Hue Channel Histogram')
plt.xlim([0, 180])
plt.subplot(1, 3, 2)
hist_saturation = cv2.calcHist([hsv_image], [1], None, [256], [0, 256])
plt.plot(hist_saturation, color='green')
plt.title('Saturation Channel Histogram')
plt.xlim([0, 256])
plt.subplot(1, 3, 3)
hist_value = cv2.calcHist([hsv_image], [2], None, [256], [0, 256])
plt.plot(hist_value, color='blue')
plt.title('Value Channel Histogram')
plt.xlim([0, 256])
plt.tight_layout()
plt.show()
