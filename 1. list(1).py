# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:18:00 2023

@author: BenjaminLuTseng
"""
## what is a list?
# A list of n number is from the element index 0(1st number) to element index n-1(nth number)
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[3]) #The (3+1)th element A.K.A number 3
print(a[-2]) #The 2nd number from the last element in the list(a)
print(a[0:3]) #The (0+1)th element(number 1) to the 3rd element(number 2)
print(a[:]) #All the elements from list(a)
print(a[:4]) #The 1st element(number 0) to the 4th element(number 3)
print(a[-3:]) #The 3rd element from the last to the last element of the list(number 9)
#top10 = [:10] last10 = [-10:]

# Add up lists
[1, 2] + [3, 4] #[1, 2, 3, 4]
sum([1, 2, 3]) #1 + 2 + 3 = 6

## Range
# Range 1
a = [x for x in range(10)] #Show the numbers between 0 to 9(show 10 numbers start from 0 so 10 will not be included)
print(a[:]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #All the elements in a
print(a[::2]) #[0, 2, 4, 6, 8] 
print(a[::3]) #Arithmetic sequence which starts from element 0 of list(a) with a common difference of 3
print(a[1::3]) #Arithmetic sequence which starts from element 1 of list(a) with a common difference of 3
b= [x for x in range(0, 30, 2)]
print(b) #Arithmetic sequence which starts from element 0 of a list, which contains 30 numbers from 0 to 29, with a common difference of 3

# Range 2
a=[x for x in range(1, 11)]
print(a) #list(a) is from 1 to 10

b=[x for x in range(2, 11, 2)]
print(b) #Arithmetic sequence which starts from element 0 of a list, which contains 9 numbers from 2 to 10, with a common difference of 2

sum(x for x in range(1, 100+1)) #Sum 1 to 100

c = tuple(range(10)) #tuple means ()
print(c)

## Replace
# Replace the element of the list
a=(2, 1, 5, 9, 3) #The elements of the "()" list CANNOT be replaced
a[0]= 100 #Try to replace element 0 of the list(a)>>>Error

b=[2, 1, 5, 9, 3] #The elements of the "[]" list CAN be replaced
b[0]= 100
