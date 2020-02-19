#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:21:27 2019

@author: nshefeek

Karatsuba


"""

X = 3141592653589793238462643383279502884197169399375105820974944592
Y = 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(X, Y):
    
    len_x = len(str(X))
    len_y = len(str(Y))
    n = max(len_x, len_y) // 2
    if (X < 10) | (Y < 10):
        return X * Y
    else:      
        a = X // 10**n
        b = X % 10**n
        c = Y // 10**n
        d = Y % 10**n
                
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        abcd = karatsuba(a+b, c+d)
        adbc = abcd - ac - bd
        product = 10 **(n*2) * ac + bd + 10**n  * adbc
        return product
    
print(karatsuba(X, Y))