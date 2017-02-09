from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import sys
import colorsys
from time import gmtime, strftime

# Function RGB to HLS
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

# Function RGB to Lab
def rgbToLab(vr, vg, vb):
    r = (vr + 0.0) / 255
    g = (vg + 0.0) / 255
    b = (vb + 0.0) / 255

    if (r > 0.04045):
        r = pow((r + 0.055) / 1.055, 2.4)
    else:
        r = r / 12.92
    if (g > 0.04045):
        g = pow((g + 0.055) / 1.055, 2.4)
    else:
        g = g / 12.92
    if (b > 0.04045):
        b = pow((b + 0.055) / 1.055, 2.4)
    else:
        b = b / 12.92

    r = r * 100.0
    g = g * 100.0
    b = b * 100.0

    var_x = r * 0.4124 + g * 0.3576 + b * 0.1805
    var_y = r * 0.2126 + g * 0.7152 + b * 0.0722
    var_z = r * 0.0193 + g * 0.1192 + b * 0.9505

    var_x = var_x / 95.047
    var_y = var_y / 100.00
    var_z = var_z / 108.883

    if (var_x > 0.008856):
        var_x = pow(var_x, (1.0 / 3.0))
    else:
        var_x = (7.787 * var_x) + (16.0 / 116.0)
    if (var_y > 0.008856):
        var_y = pow(var_y, (1.0 / 3.0))
    else:
        var_y = (7.787 * var_y) + (16.0 / 116.0)
    if (var_z > 0.008856):
        var_z = pow(var_z, (1.0 / 3.0))
    else:
        var_z = (7.787 * var_z) + (16.0 / 116.0)

    var_L = (116.0 * var_y) - 16.0
    var_a = 500.0 * (var_x - var_y)
    var_b = 200.0 * (var_y - var_z)
    if (var_L >= 0 and var_L <= 100 and var_a == 0 and var_b == 0):
    	return 0.0, 0.0, 0.0
    else:
    	return var_L, var_a, var_b    

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
arrayColors = []

# Start processing time
startProcessing = strftime("%Y-%m-%d %H:%M:%S")

for u in range(1, x):
    for v in range(1, y):
        vR, vG, vB = pix[u, v]
        pixelValue = convertColors(vR, vG, vB)
        if (pixelValue == 0):
        	tempText = str(u) + "-" + str(v)
        	arrayColors.append(tempText)
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
print("Area hoja: %.2f centimetros cuadrados" % round(areaPixeles,2))
print("Numero de colores a evaluar: %d" % len(arrayColors))

for coordenadas in arrayColors:
	tempCoordenadas = coordenadas.split("-")
	valueX = tempCoordenadas[0]
	valueY = tempCoordenadas[1]
	vR, vG, vB = pix[u, v]

# End processing time
endProcessing = strftime("%Y-%m-%d %H:%M:%S")

print("Start %s" % startProcessing)
print("End %s" % endProcessing)