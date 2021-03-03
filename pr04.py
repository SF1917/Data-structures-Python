# -*- coding: utf-8 -*-
"""
@author: SF1917
"""

word = 'SF1917'
letters = list(word)
for ch in letters[:9]:
    print('\t', ch)
for ch in letters[-7:-1]:
    print('\t'*2, ch)
for ch in letters[4:23:3]:
    print('\t'*3, ch)    