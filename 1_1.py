#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:29:28 2018

@author: behruz
"""

def unique_char(word):
    """
    Checks if all the characters in a given word are unique
    """
    word_array = list(word)
    for char in word:
        if word_array.count(char) > 1:
            return False
    return True

print unique_char('')   

def unique_char1(word):
    """
    Checks if all the characters in a given word are unique
    """
    word_array = list(word)
    for letter in word:
        if letter in word_array.remove(letter):
            return False
    return True

print unique_char('')  
