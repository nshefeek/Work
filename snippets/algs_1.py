#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:41:54 2019

@author: nshefeek
"""

import math
import matplotlib.pyplot as plt

n = [i for i in range(11)]
a = [(2**2)**i for i in range(11)]
b = [(2**i)**2 for i in range(11)]
#c = [(i**2)*math.log(i) for i in range(11)]
d = [i for i in range(11)]
e = [(i**2)**i for i in range(11)]

plt.subplot(4,1,1)
plt.plot(a, n)
plt.subplot(4,1,2)
plt.plot(b, n)
plt.subplot(4,1,4)
plt.plot(d, n)
plt.subplot(4,1,4)
plt.plot(e, n)