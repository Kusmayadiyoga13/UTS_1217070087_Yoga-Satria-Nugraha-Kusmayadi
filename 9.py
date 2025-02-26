import cv2
import matplotlib.pyplot as plt

image = cv2.imread('kucing.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(h, cmap='hsv')
plt.title('Hue Channel')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(s, cmap='gray')
plt.title('Saturation Channel')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(v, cmap='gray')
plt.title('Value Channel')
plt.axis('off')
plt.tight_layout()
plt.show()
