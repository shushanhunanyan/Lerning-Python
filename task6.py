# 1. Load and display an image using Matplotlib.
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = '/home/shushan/Downloads/1.jpeg'
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title('Loaded Image')
plt.show()

# 2. Plot the histogram of image pixel intensities.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
histogram, bin_edges = np.histogram(img_gray, bins=256, range=(0, 256))

plt.figure(figsize=(10, 5))
plt.title('Histogram of Pixel Intensities')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.bar(bin_edges[:-1], histogram, width=1, edgecolor='black')
plt.show()

