#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:48:24 2019

@author: nshefeek
"""

def solve(X, Y, N, K):
	# write your code here
    dist = 0
    counter = 0
    for i in range(N):
        if K >= dist + abs(ord(X[i]) - ord(Y[i])):
            dist += abs(ord(X[i]) - ord(Y[i]))
            counter += 1
            
    return counter

	
N = int(input())
X = input()[:N]
Y = input()[:N]
T = int(input())

for i in range(T):
	K = int(input())
	
	res = solve(X,Y,N,K)
	print(res)