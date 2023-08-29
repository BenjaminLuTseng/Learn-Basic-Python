# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:33:43 2023

@author: gg90180
"""
## Defind Cards(ex. Ace of Spades, 4 of Heart)
# Suit(spade heart diamond club)
def suit(n): #Spade: 0~12, Heart: 13~25, etc.
    x = n//13
    if x == 0:
        y = 'S'
    elif x == 1:
        y = 'H'
    elif x == 2:
        y = 'D'
    else:
        y = 'C'
    return y
print(suit(29))

# Rank(points)
def rank(n):
    x = n%13 + 1
    if x == 1:
        y = 'A'
    elif x == 11:
        y = 'J'
    elif x == 12:
        y = 'Q'
    elif x == 13:
        y = 'J'
    else:
        y = str(x) #str: straight number
    return y 
print(rank(29))

## Play Cards
# Hand(a hand of cards)
import random
def card(n):
    return suit(n) + rank(n)
def hand():
    a = random.sample(range(52), 5) #sample: no repeat numbers
    return[card(x) for x in a]
print(hand())

# Flush (same suit)
def flush(a):
    b = sorted(x[0] for x in a) #X is suit+rank, so x[0] will show rank only suit
    print(b)
    return b[0] == b[-1] #== now is True or False here
a = ['H1', 'D2', 'D3', 'D4', 'H5']
print(flush(a))

# Possibility of a flush
n = 10**7
c = 0 #Start from 0
for _ in range(n):
    a = hand()
    if flush(a):
        c += 1 #Plus 1 every time a flush emerged
print(c/n)

# Flush II
def flush(a):
    b = [x[0] for x in a]
    print(b)
    return b.count(b[0])==5 #One suit has beem counted for 5 times(no other suits)
a = ['C5', 'H4', 'D5', 'D4', 'H6']
flush(a)

#Four of a Kind(4 cards with the same rank)
def four_of_a_kind(a):
    b = [x[1:] for x in a]
    c = sum(b.count(x) for x in b)
    print('{}, count={}'.format(b,c))
    return c == 17
a = ['DK', 'D6', 'S10', 'C3', 'H3']
print(four_of_a_kind(a))

#Straight