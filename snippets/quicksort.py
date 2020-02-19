#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 08:00:06 2019

@author: nshefeek
"""
A = [3, 2, 6, 8, 5, 1, 7, 4, 0]
n = len(A)
p = 0
count = 0

while p < n:
    i = 0
    while i < n:
        temp1, temp2 = A[p], A[i]
        count += 1
        if temp1 < temp2:
            A[p], A[i] = temp2, temp1
        print(A, count)
        i += 1
        
    p += 1
        