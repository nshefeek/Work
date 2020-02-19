#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:11:02 2019

@author: nshefeek
"""
def print_triangle(n):
    if n<0:
        return
 
    for i in range(n+1):
       print((n-i)*' ', i*' *', sep='')
        
print_triangle(11)
