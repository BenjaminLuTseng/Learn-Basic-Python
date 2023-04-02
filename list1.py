# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:18:00 2023

@author: BenjaminLuTseng
"""
##
#A list of n number is from number 0(1st number) to number n-1(nth number)
a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[3]) #The (3+1)th number
print(a[-2]) #The 2nd number from the last number in the list(a)
print(a[0:3]) #The (0+1)th number(number 1) to the 3rd number(number 2)
print(a[:]) #All the numbers from list(a)
print(a[:4]) #The 1st number(number 0) to the 4th number(number 3)
print(a[-3:]) #The 3rd number from the last to the last number of the list(number 9)
#top10=[:10] last10=[-10:]

##
b = [x for x in range(10)] #Show the numbers below 10(not include 10)
print(b[:]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] All the numbers in b
print(b[::2]) #[0, 2, 4, 6, 8] 
print(b[::3]) #Multiples of number 3( including number 0)
print(b[1::3]) #Multiples of 3 start from number 1(treat number 1 as number 0)
c= [x for x in range(0, 30, 2)]
print(c) #Multiples of number 3 start from number 0 of list(c) which contains 30 numbers(number 1 to number 29)
