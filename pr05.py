# -*- coding: utf-8 -*-
"""
@author: SF1917
"""

w = input('Type Text: ')
v = ['a', 'e', 'i', 'o', 'u']
found = {}


for letter in w:
    if letter in v:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in found.items():
    print(k, 'was found', v, 'time(s).')        
        