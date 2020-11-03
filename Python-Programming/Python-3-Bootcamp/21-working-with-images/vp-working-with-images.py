# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:05:29 2020

@author: vivek
"""

# pip install pillow
# pillow is a fork of pil library, which is the Python Imaging Library
# https://note.nkmk.me/en/pillow/

from PIL import Image
mac=Image.open('example.jfif')
type(mac) 
mac # shows the images. in pycharm you might need to type mac.show()
mac.size # returns dimentions
mac.filename # returns filename
mac.format_description # returns format description

# cropping image
x=mac.size[0]*0.5
y=mac.size[1]*0.5
mac_cropped=mac.crop((0,0,x,y)) # cropping image

# paste an image on the image
mac_copy=mac.copy()  # paste() overwrites the base image itself, so if you want to keep the original image, use the copied image with copy()
mac_copy.paste(im=mac_cropped,box=(237,158)) # The position to paste is specified by a tuple (x coordinate in upper left, y coordinate in upper left) in the second parameter box
 
mac.resize((500,500)) # resize image
mac.rotate(90)  # rotate by 90 degrees

# color transparency
# rgba - red, green, blue, alpha (alpha = 0 (completely transparent) to 255 (completely opaque))
mac_copy.putalpha(128)

mac_copy.save('mac_copy.jpeg') # save image

