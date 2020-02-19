#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:49:46 2019

@author: nshefeek
"""

import matplotlib.pyplot as plt
import math

a = [(2**2)**i for i in range(11)]
b = [(2**i)**2 for i in range(11)]
#c = [(math.log(i))*i**2 for i in range(11)]
d = [i for i in range(11)]
e = [(i**2)**i for i in range(11)]
n = [i for i in range(11)]

plt.subplot(2,1,1)
plt.plot(a, n)
plt.title('a')
#plt.subplot(2,1,2)
#plt.plot(b, n)
#plt.title('b')
#plt.subplot(2,2,1)
#plt.plot(d, n)
#plt.title('d')
#plt.subplot(2,2,2)
#plt.plot(e, n)
#plt.title('e')