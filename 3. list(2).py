# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:58:16 2023

@author: gg90180
"""
##
#Letters
ord('A') #The unicode code of the uppercase of 'A'  is 65
ord('E') - ord('A') + 1 #69 - 65 + 1 = 5 (E is the 5th letter in the alphabat)

a = 'iron maiden'
print(a[:5]) #Number 0 to number 4 of the list(a)
b = [x for x in a] #Every letter in list(a) including space in['','']
print(b)
c = ''.join(b) #Join the letters and the space together in the list(b) 
print(c)
d = '-'.join(b) #Join the letters and the space together in the list(b) with "-" between each letter 
print(d)
e = a.split() #split every word in the list(a)
print(e) #['iron', 'maiden']

x='riff,    '
x.strip() #delete the space

#Upper and lower case
a = "I love melodic death metal."
a.upper() #Make each letter uppercase
a.lower() #Make each letter lowercase
a.capitalize() #Make number 0 of the list(a) uppercase
a.title() #Capitalize the first letter of each word

##
#The order of each letter in the list
b = 'metal forever'
[x for x in b]
[x for x in b.upper()] #Make every letter uppercase in list(a) including space in['','']
[x for x in b.upper() if x>= 'A'] #A=0, B=1, C=3, ...
[x for x in b.upper() if x >= 'O']
[x for x in b.upper() if 'A' <= x <= 'M']

c = 'shredding'
d = sum([ord(x) - ord('A') + 1 for x in c.upper() if 'A' <= x <= 'Z'])
print(d) #Sum HARDWORK if A=1, b=2, C=3, ...

#Sum the order of each letter of each word in the list
def f(a):
    return sum([ord(x) - ord('A') + 1 for x in a.upper() if 'A' <= x <= 'Z'])
a = 'INSOMNIUM'
print(a, f(a)) #INSOMNIUM 96 (f(a) is the sum of the order of the letter starts from A=1)
b = 'AMORPHIS'
print(b, f(b))

def f(c):
    return sum(ord(x) - ord('A') + 1 for x in c.upper() if 'A' <= x <= 'Z')
c = ['MAYHEM', 'ENSLAVED', 'EMPORER']
for x in c: #Use 'for' if you want to define the new algebra 'x'
    print('f({})={}'.format(x, f(x))) #f(x)= the answer of f(x), say x is MAYHEM>>> f(MAYHEM)= 65
