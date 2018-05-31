#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:15:50 2018

@author: behruz
"""


def is_anagram(str1, str2):
    
    str1_array = list(str1)
    str2_array = list(str2)
    
    for char in str1_array:
        if char in str2_array:
            str2_array.remove(char)
        else:
            return False
        
    if len(str2_array) == 0:
        return True
    else:
        return False

            
        
            