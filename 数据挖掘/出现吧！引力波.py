# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:11:33 2018

@author: 王磊
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate_h, hstrain = wavfile.read('H1_Strain.wav', 'rb')
rate_l, lstrain = wavfile.read('L1_Strain.wav', 'rb')
reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose()

htime_interval = 1 / rate_h
ltime_interval = 1 / rate_l

htime_len = hstrain.shape[0] / rate_h
ltime_len = lstrain.shape[0] / rate_l
htime = np.arange(- htime_len/2, htime_len/2, htime_interval)
ltime = np.arange(- ltime_len/2, ltime_len/2, ltime_interval)

fig = plt.figure(figsize=(12,6))

plth = fig.add_subplot(221)
plth.plot(htime, hstrain, 'y')
plth.set_xlabel('Time(second)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

pltl = fig.add_subplot(222)
pltl.plot(ltime, lstrain, 'y')
pltl.set_xlabel('Time(second)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')

pltref = fig.add_subplot(212)
pltref.plot(reftime, ref_H1, 'y')
pltref.set_xlabel('Time(second)')
pltref.set_ylabel('Template Strain')
pltref.set_title('Template Strain')

fig.tight_layout()
