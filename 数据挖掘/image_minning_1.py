# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:37:34 2018

@author: 王磊
"""

from PIL import Image
import numpy as np

im = np.array(Image.open("images/2a369c69d6.jpg"))

im_change = [255, 255, 255] - im


im_result = Image.fromarray(im_change.astype(np.uint8))

im_result.save('images/testImage1.jpg')
