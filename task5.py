#1 + 2 Load an image using Pillow or OpenCV and convert it to a Numpy array + flip rotate
import cv2
import numpy as np

img_path = '/home/shushan/Downloads/1.jpeg'
img = cv2.imread(img_path)

img_array = np.array(img)
print("Image as NumPy Array:\n", img_array)

flip = np.fliplr(img_array)
cv2.imwrite('/home/shushan/Downloads/flipped_horizontal.jpeg', flip)

rotate = cv2.rotate(img_array, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('/home/shushan/Downloads/rotated_90_ccw.jpeg', rotate)

