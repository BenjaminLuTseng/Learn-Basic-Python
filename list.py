# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:18:00 2023

@author: gg90180
"""
##
#A list of n number is start from 0(1st number) and end at n-1(nth number)
a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[3]) #The (3+1)th number
print(a[-2]) #The 2nd number from the last
print(a[0:3]) #The (0+1)th number to the 3rd number
print(a[:]) #All the numbers from a
print(a[:4]) #The 1st number to the 4th number
print(a[-3:]) #The 3rd number from the last to the last number of the list
#top10=[:10] last10=[-10:]

##
b = [x for x in range(10)]
print(b) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b[::2]) #[0, 2, 4, 6, 8]
print(b[::3]) #Multiples of 3 [(0+1)th, (3+1)th, (6+1)th, ...]
print(b[1::3]) #Multiples of 3 (Start from the 2nd number)
c= [x for x in range(0, 30, 2)]
print(c) #0 ~ 29