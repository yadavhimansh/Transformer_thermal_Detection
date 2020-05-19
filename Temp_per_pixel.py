#!/usr/bin/env python
# coding: utf-8

# Import necesssary libraries to extract the temperature per pixel
import flirimageextractor
from matplotlib import cm
from matplotlib import pyplot as plt
import cv2

# Read the image using OpenCV library
image = cv2.imread('Transformer.jpg')
plt.subplot(1,1,1)
plt.imshow(image)
plt.show()

# Find the shape of the image
rows,cols,color = image.shape
print(image.shape)

# Process the image using FlirImageExtractor library
flir = flirimageextractor.FlirImageExtractor(palettes=[cm.jet, cm.bwr, cm.gist_ncar])
flir.process_image('Transformer.jpg')
flir.save_images()
flir.plot()
thermal = flir.get_thermal_np()
flir.check_for_thermal_image('Transformer.jpg')

# Extract the temperature per pixel of the image Transformer.jpg
for i in range(image.shape[0]):
    for j in range(0,image.shape[1]):
        pixel=image[i,j]
        temperature = thermal[i,j]
        print(pixel,temperature )
        
      
        





