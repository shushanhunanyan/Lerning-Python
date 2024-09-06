# 2. Write a script that imports a custom module for basic image operations.
import cv2

def resieze_img(img_path, width=None, height=None):
    img = cv2.imread(img_path)

    if img is None:
        print(f"Error: Unable to open {img_path}")
        return None 


