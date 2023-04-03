# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 22:20:19 2023

@author: BenjaminLuTseng
"""
##
#Random
import random
a = [random.randrange(1, 10) for x in range(5)] #randrange: Numbers are repeatable
print(len(a)) #list(a) contains 3 numbers
print(a) #list(a) contains 5 numbers which are drawn randomly from 1 to 9(not including the last number)
print(a[0:3]) #number 0 to number 3 from the list(a)

import random
b= random.sample(range(1, 50), 6) #sample: Numbers are NOT repeatable
print(len(b))
print(b) #list(b) contains 6 numbers which are drawn randomly from 1 to 49

import random
c = random.sample(range(1,100), 10)
print("apple=", c) #apple= list(c)
print("Invert=", c[::-1]) #Arithmetic sequence with a common difference of -1(Invert the list)
d = [x for x in c if x < 50] #The numbers in the list(c) which are below 50
print("d=", d)

