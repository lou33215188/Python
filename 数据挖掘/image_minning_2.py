# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:53:29 2018

@author: 王磊
"""

from PIL import Image
import numpy as np

im_begin = Image.open('images/b270a58d9c.jpg')
imBegin = np.array(im_begin.convert('L'))
imChange = 255 - imBegin
imResult = Image.fromarray(imChange.astype(np.uint8))
imResult.save('images/testImage2.jpg')
