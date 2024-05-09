import cv2
import matplotlib.pyplot as plt

img = cv2.imread('kucing.jpg')
blue_band = img[:, :, 0]  
green_band = img[:, :, 1]  
red_band = img[:, :, 2]    
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(blue_band, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(green_band, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(red_band, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')
plt.show()
