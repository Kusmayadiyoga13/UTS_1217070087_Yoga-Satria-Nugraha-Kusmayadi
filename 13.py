import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('kucing.jpg')
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
