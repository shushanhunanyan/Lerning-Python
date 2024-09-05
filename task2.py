# 1. Create a dictionary to store image metadata
from PIL import Image
import os

def get_img_metadata(img_path):
    try:
        with Image.open(img_path) as img:
            metadata = { 
                    "width": img.width,
                    "height": img.height,
                    "file_size": os.path.getsize(img_path) // 1024,
                    "format": img.format,
                    "mode": img.mode
            }
        return metadata
    
    except Exception as e:
        print(f"Error: {e}")
        return None

image_path = "/home/shushan/Downloads/1.jpeg"
metadata = get_img_metadata(image_path)

if metadata:
    print("Image Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")



# 2. Use list comprehension to create a list of image file names from a directory.
def get_img_files(directory):
    img_extensions = ('.jpg', '.jpeg', '.png')

    img_files = [f for f in os.listdir(directory) if f.lower().endswith(img_extensions)]

    return img_files

dir_path = '/home/shushan/Downloads'
img_files = get_img_files(dir_path)

print("Image Files:")
for file in img_files:
    print(file)


# 3. 
