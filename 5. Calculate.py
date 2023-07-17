# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:12:12 2023

@author: BenjaminLuTseng
"""

## Calculation
# 1/Rt = 1/R1 + 1/R2 + ... + 1/Rn
R = [200, 100, 400, 300]
Rt = 1/(sum(1/x for x in R))
print(Rt)

# Maximum and minimum
data = [3, 6, 7, 2, 5, -2]
max(data)
min(data)

## The numbers of certain element in a list
#
data = [2, 4, 4, 1, 1, 1]
data.count(1) #1 appear three times in list(data)

## Interest rate
# Simple interest
P = 1000000
r = 5/100
t = 20
F = P*(1 + r*t)
print(F)

# Compound Interest
P = 1000000
r = 5/100
t = 20
F = P*(1 + r)**t
print(F)

## Find the roots of quadratic equations
# ax**2 + bx + c = 0
def roots(a = 2, b = -3, c = 1):
    d = b**2 - 4*a*c
    r1 = (-b + d**0.5)/(2*a)
    r2 = (-b - d**0.5)/(2*a)
    print('r1 = ', r1)
    print('r2 = ', r2)
roots() #Default is a = 2, b = -3, c = 1
roots(1, -5, 6)

