import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('kucing.jpg')
normalized_image = image.astype(np.float32) / 255.0
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(normalized_image, cv2.COLOR_BGR2RGB))
plt.title('Normalized Image')
plt.axis('off')
plt.subplot(1, 2, 2)
hist = cv2.calcHist([normalized_image], [0], None, [256], [0, 1])
plt.plot(hist, color='gray')
plt.title('Normalized Image Histogram')
plt.xlabel('Pixel Value (0-1)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
