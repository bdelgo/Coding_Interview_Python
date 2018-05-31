#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:49:43 2018

@author: behruz
"""

def replace_space(string):
    return '%20'.join(string.split(' '))

print replace_space('b e h rooz')