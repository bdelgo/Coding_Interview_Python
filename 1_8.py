#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:35:37 2018

@author: behruz
"""

def is_substring(s1, s2):
    if s2 in s1:
        return True
    return False

def rotate(s):
    return s[-1] + s[0:len(s)-1]

def is_rotate(s1, s2):
    if len(s1) != len(s2):
        return False
    elif len(s2) == 0:
        return True
    else:
        i = len(s2)
        while i > 0 :
            if s2 in s1:
                return True
            s2 = rotate(s2)
            i -= 1
        return False
        
print is_rotate('a', 'b')
print is_rotate('','')
print is_rotate('erbottlewat', 'waterbottle')

def is_rotation(s1, s2):
    s11 = s1+s1
    if len(s1) != len(s2):
        return False
    elif s2 not in s11:
        return False
    else:
        return True
    
print is_rotation('a', 'b')
print is_rotation('','')
print is_rotation('erbottlewat', 'waterbottle')
