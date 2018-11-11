# -*- coding: utf-8 -*-
"""
Created on Wed May  2 18:16:13 2018

@author: 王磊
"""

from PIL import Image
import numpy as np

img = Image.open('images/psbe.jpg')
imgCov = img.convert('L')
imageArray = np.array(imgCov).astype(np.float)

depth = 10      # (0-100)
grad = np.gradient(imageArray)
gradx,grady = grad
gradx = gradx*depth/100
grady = grady*depth/100

TEMP = np.sqrt(gradx**2 + grady**2 + 1)
uni_x = gradx/TEMP
uni_y = grady/TEMP
uni_z = 1./TEMP

vec_el = np.pi/2.2
vec_az = np.pi/4
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)

imageArrayResult = 255*(dx*uni_x + dy*uni_y + dz*uni_z)
imageArrayResult = imageArrayResult.clip(0,255)

im = Image.fromarray(imageArrayResult.astype(np.uint8))
im.save('images/TestImageC.jpg', 'JPEG')

