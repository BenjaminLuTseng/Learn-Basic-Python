# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:58:59 2023

@author: BenjaminLuTseng
"""

## Sort and sequence
#
a = [4, 8, 1, 7, 9, 6, 3, 10, 5, 2]
b = sorted(a)
a.sort()
print(a)
print(b)
a == b #True, the elements in list(a) and list(b) are the same
a is b #True, the orders of both lists are different
id(a) #The postition of list(a) in the memory
id(b)

#
data = [4, 8, 1, 7, 9, 6, 3, 10, 5, 2]
key = 7
key in data #True
data.index(7) #The element index of 7 of the list(data)

## Sort a list in ascending order
# Loop
def selection_sort(a):
    n= len(a)
    for i in range(0, n-1): #i is the unsorted portion of the list
        k = i # The variable "k" keeps track of the index of the minimum element found in the unsorted portion of the list
        for j in range(i+1, n): # The variable "j" searches for the minimum element in the unsorted portion of the list
            if a[j] < a[k]:
                k = j # This process will update minimum element index to "j" if the element at index "j" is smaller than the element at index "k"
            a[i], a[k] = a[k], a[i]
    return(a)

r = [5, 9, 4, 3, 1]
selection_sort(r)
print(r)

import random
b = random.sample(range(10**6), 10**3)
b[:10]
selection_sort(b)
b[:10]

# Use "sort" code
c = [1, 4, 2, 6, 3, 8, 3, 9]
c.sort()
c

# Find the index of an element
data = [4, 8, 1, 7, 9, 6, 3, 10, 5, 2]
key = 7
key in data
data.index(7)

# Sort names and quantitative details together
JP = ('Judas Priest', 54)
IM = ('Iron Maiden', 49)
A7X = ('Avenged Sevenfold', 23)
BVB = ('Black Veil Brides', 17)
Bands = [JP, IM, A7X, BVB]
sorted(Bands) #From small to large (The capital letter in the alphabat)
sorted(Bands, reverse=True) #From large to small (The capital letter in the alphabat)
sorted(Bands, key=lambda x: x[1]) #In the lambda function, x represents each element in the bands and x[1] represents the years active of each band
sorted(Bands, key=lambda x: x[1], reverse=True) #The 'key' parameter specifies a function that will be used to extract a comparison key from each element in the list for the sorting operation

## Search
# Sequential Search
def sequential_search(a, x):
    for i in range(len(a)):
        if x == a[i]:
            return i
    return -1 #If not finding x, return "-1"
data = [1, 9, 8, 5]
print(sequential_search(data, 9))

# Binary Search
def binary_search(a, x):
    left, right = 0, len(a)-1
    while left <= right:
        mid = (left + right)//2 #quotient
        print('L={}, R={}, M={}, DATA[M]={}'.format(left, right, mid, a[mid]))
        if x == a[mid]:
            return mid
        elif x < a[mid]: #If "x" is on the left side of "a", then update "right" to "mid-1" to immediately cut the right side
            right = mid-1
        else:
             left = mid+1 
    return -1
data = [6, 19, 36, 43, 50, 52, 55, 65, 71, 81]
data.sort()
key = 43
binary_search(data, key)
