# -*- coding: utf-8 -*-
"""
@author: SF1917
"""

w = input('Type Text:  ')
v = set('aeiou')
found = v.intersection(set(w))
for vowel in found:
    print(vowel)