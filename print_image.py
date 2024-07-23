from PIL import Image

from os import *

import os

# file name with extension
file_name = 'C:\\Users\\mohannad\\Desktop\\image' #file path of the images


images=[]


# file name without extension
for file_path in os.listdir(file_name):
    if '.png' in file_path and '.1.' in file_path:
        images.append(file_path)
        


# print(images)
img = []

for i in range(len(images)):
    imge = Image.open('C:\\Users\\mohannad\\Desktop\\image\\'+images[i])
    print(images[i])
    img.append(imge)



img_size = img[0].size

# Calculate the size of the final merged image
grid_width = 4
grid_height = 4
new_im = Image.new('RGB', (grid_width * img_size[0], grid_height * img_size[1]), (250, 250, 250))

# Paste each image onto the new image
for i in range(len(img)):
    row = i // grid_width
    col = i % grid_width
    new_im.paste(img[i], (col * img_size[0], row * img_size[1]))

# Save the merged image as "merged_images.png" and display it
new_im.save("merged_images.png", "PNG")
new_im.show()






# Read the twelve images
#img_01 = Image.open('10.165.120.10.png')
#img_02 = Image.open('10.165.5.8.png')
#img_03 = Image.open('10.165.2.12.png')
#img_04 = Image.open('10.166.9.18.png')
#img_05 = Image.open('10.165.105.120.png')
#img_06 = Image.open('10.165.5.5.png')
#img_07 = Image.open('10.165.5.6.png')
#img_08 = Image.open('10.165.5.9.png')
#img_09 = Image.open('10.166.99.5.png')
#img_10 = Image.open('10.166.1.60.png')
#img_11 = Image.open('10.166.2.57.png')
#img_12 = Image.open('10.165.12.175.png')
#
## Get the sizes of the images
#img_size = img_01.size
#
## Create a new blank image with a size large enough to fit all the images in a 4x3 grid
#new_im = Image.new('RGB', (4 * img_size[0], 3 * img_size[1]), (250, 250, 250))
#
## Paste each image onto the new image
#new_im.paste(img_01, (0, 0))
#new_im.paste(img_02, (img_size[0], 0))
#new_im.paste(img_03, (2 * img_size[0], 0))
#new_im.paste(img_04, (3 * img_size[0], 0))
#new_im.paste(img_05, (0, img_size[1]))
#new_im.paste(img_06, (img_size[0], img_size[1]))
#new_im.paste(img_07, (2 * img_size[0], img_size[1]))
#new_im.paste(img_08, (3 * img_size[0], img_size[1]))
#new_im.paste(img_09, (0, 2 * img_size[1]))
#new_im.paste(img_10, (img_size[0], 2 * img_size[1]))
#new_im.paste(img_11, (2 * img_size[0], 2 * img_size[1]))
#new_im.paste(img_12, (3 * img_size[0], 2 * img_size[1]))
#
## Save the merged image as "merged_images.png" and display it
#new_im.save("merged_images.png", "PNG")
#new_im.show()