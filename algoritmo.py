from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import sys
import colorsys

def convertColors(vr, vg, vb):
	r = vr/255.0
	g = vg/255.0
	b = vb/255.0
	colorPixel = 0
	h, l, s = colorsys.rgb_to_hls(r, g, b)
	if(l >= 0.5):
		#lighter color
		colorPixel = 1
		return colorPixel
	elif (l < 0.5):
		#darker color
		colorPixel = 0
		return colorPixel
    

tempTitleImage = "images/3.jpg"
im = Image.open(tempTitleImage) # Can be many different formats.
pix = im.load()
                # import image  
x, y = im.size  # size of the image
print (x)       # Print X
print (y) 
totalPixeles = x * y      # Print Y
counter = 0.0
counterBackground = 0
counterColors = 0
for u in range(1, x):
    for v in range(1, y):
        vR, vG, vB = pix[u, v]
        pixelValue = convertColors(vR, vG, vB)
        if (pixelValue == 0):
        	counterColors += 1
        elif (pixelValue == 1):
        	counterBackground += 1
        if (counter % 1000000 == 0):
            tempValue = (counter / (x * y)) * 100.0
            print("%.2f %%" % round(tempValue, 2))
        counter += 1

# convertir pixeles a cm^2
areaCentimetros = 28.0 * 21.7
areaPixeles = areaCentimetros * counterColors / (totalPixeles * 1.0)
print("Pixeles Color: %d" % counterColors)
print("Pixeles Background: %d" % counterBackground)
print("Total de pixeles: %d" % totalPixeles)
print("Area hoja: %f centimetros cuadrados" % areaPixeles)