# -*- coding: utf-8 -*-
"""
@author: SF1917
"""

#w = 'inside'
w = input('Type Text: ')
v = ['a', 'e', 'i', 'o', 'u']
found = []

for letter in w:
   if letter in v:
       if letter not in found:
           found.append(letter)
for vowel in found:
    print(vowel)       