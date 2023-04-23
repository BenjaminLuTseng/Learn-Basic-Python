# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:21:27 2023

@author: BenjaminLuTseng
"""

## BMI
# If
bmi = 23
if bmi < 18.5: # ":" means unfinished
    status = "Underweight"
elif bmi < 30:
    status = "Normalweight"
else:
    status = "Overweight"
print(status)

# Calculate
def bmi(w = 65, h = 1.7):
    return w/h**2
bmi(60, 1.7)

# def
def bodyfat_status(bodyfat):
    if bodyfat < 10: 
        status = "shredded"
    elif bodyfat < 14: 
        status = "lean"
    elif bodyfat < 24: 
        status = "normal"
    elif bodyfat < 30: 
        status = "slightly obese"
    elif bodyfat < 35: 
        status = "median obese"
    else: 
        status = "severe obese"
    return status
result = bodyfat_status(25)  # Call the function with bodyfat value of 25
print(result)  # Print the result

## 1 + 2 + ... + 10
# for (If you know how many times it has to be done)
s = 0
n = 10
for i in range(1, n+1): #i ranges from 1 to n
    s += i #s = s + i
print(s)

# While (If you don't know how many times it has to be done)
s = 0
n = 10
i = 1
while i <= n: 
    s += i # There are n(10) loops, each loop has two steps. The first step of the first loop starts from s = 0 and i = 1 so s = 0 + 1.
    i += 1 # The second step of the loop is i = 1 + 1 = 2. Then use i = 2 and s = 1 to run the second loop, and so on.
print(s) #s = 0 + 1 = 1 >>> i = 1 + 1 = 2 >>> s = 1 + 2 = 3 >>> i = 2 + 1 = 3 >>> ... 

#
n = 10
sum(range(1, n+1)) #from 1 to n

## A number can be divided by how many 2s before the remainder is no longer 0?
# 360 = 2**x * y (i.e., 360/2=180, 180/2=90, 90/2=45. So x is 3)
n = 360 #(n starts at 360)
count = 0 # We do not know how many times we have to count to the number x, so using "while" loop is an appropriate way to do
while n % 2 == 0: # %: remainder
    n//=2 # //: quotient
    count += 1
print(count)

## Minimum
# Full
a = 5
b = 3
if a < b:
    min = a
else:
    min = b
print(min)

# Simplified
a = 5
b = 3
min = a if a < b else b
print(min) 

## Intersection
#
import random
a = set(random.sample(range(1, 50), 6))
b = set(random.sample(range(1, 50), 6))
print(a)
print(b)
c = a & b # The intersaction of list(a) and list(b)
print(c)
print(sorted(c))
print(len(c)) # How many numbers are there in the list(c)
 
# Lotto (The lotto contains 6 main numbers and a bonus number)
import random 
def test(n = 10**6): # Using a large number of times to increase the accuracy of the result. 
    count = [0]*2 # Equals to "count = [0, 0]", which means that the two elements of "count" both start at 0
    a = random.sample(range(1, 50), 7)
    lotto, special = set(a[:6]), a[-1]
    for _ in range(n):
        a = set(random.sample(range(1, 50), 6))
        if len(a & lotto) == 3:
            if special in a:
                count[0] += 1 # Sixth price
            else:
                count[1] += 1 # Normal price
    return [x/n for x in count]
x, y = test ()
print(x*100, y*100)



