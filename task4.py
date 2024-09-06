#2. Write a script that imports a custom module for basic image operations.
import img_operation as img_ops

img_path = '/home/shushan/Downloads/1.jpeg'

width = 300
height = 300

resized_img = img_ops.resieze_img(img_path, width=width, height=height)


#3. Practice using Python’s built-in libraries for handling dates, random numbers

import datetime

cur_datetime = datetime.datetime.now()
print("Current Date and Time:", cur_datetime)

cur_date = cur_datetime.date()
print("Current Date:", cur_date)


