#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:58:33 2018

@author: behruz
"""



def reversed_string(string):
    array = list(string)
    reversed_array = array[::-1]
    return ''.join(reversed_array)

print reversed_string('behrooz')

