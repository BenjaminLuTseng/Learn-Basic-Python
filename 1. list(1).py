# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:18:00 2023

@author: BenjaminLuTseng
"""
##
#A list of n number is from number 0(1st number) to number n-1(nth number)
a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[3]) #The (3+1)th number A.K.A number 3
print(a[-2]) #The 2nd number from the last number in the list(a)
print(a[0:3]) #The (0+1)th number(number 1) to the 3rd number(number 2)
print(a[:]) #All the numbers from list(a)
print(a[:4]) #The 1st number(number 0) to the 4th number(number 3)
print(a[-3:]) #The 3rd number from the last to the last number of the list(number 9)
#top10=[:10] last10=[-10:]

##
#Range 1
a = [x for x in range(10)] #Show the numbers between 0 to 9(show 10 numbers start from 0 so 10 will not be included)
print(a[:]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #All the numbers in a
print(a[::2]) #[0, 2, 4, 6, 8] 
print(a[::3]) #Arithmetic sequence which starts from number 0 of list(a) with a common difference of 3
print(a[1::3]) #Arithmetic sequence which starts from number 1 of list(a) with a common difference of 3
b= [x for x in range(0, 30, 2)]
print(b) #Arithmetic sequence which starts from number 0 of a list, which contains 30 numbers from 0 to 29, with a common difference of 3

##
#Range 2
a=[x for x in range(1, 11)]
print(a) #list(a) is from 1 to 10

b=[x for x in range(2, 11, 2)]
print(b) #Arithmetic sequence which starts from number 0 of a list, which contains 9 numbers from 2 to 10, with a common difference of 2

sum(x for x in range(1, 100+1)) #Sum 1 to 100

c = tuple(range(10)) #tuple means ()
print(c)

##
#Replace the number of the list
a=(2, 1, 5, 9, 3) #The numbers of the "()" list CANNOT be replaced
a[0]= 100 #Try to replace number 0 of the list(a)>>>Error

b=[2, 1, 5, 9, 3] #The numbers of the "[]" list CAN be replaced
b[0]= 100
