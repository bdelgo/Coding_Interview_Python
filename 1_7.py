#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:22:49 2018

@author: behruz
"""
import numpy as np

a = [[1,2,3],[4,0,6],[7,8,9],[0,11,12], [13,14,15]]
n = np.array(a)


def zero_line_column(m):
    
    m_copy = m.copy()
    size = m_copy.shape   
    zero_index = []
    
    for index in np.ndindex(size):
        row, col = index
        if m_copy[row, col] == 0:
            zero_index.append(index)
            
    for index in zero_index:
        row, col = index
        for i in range(0, size[0]):
            m_copy[i, col] = 0
        for j in range(0, size[1]):
            m_copy[row, j] = 0
 
    return m_copy       


print zero_line_column(n)
print n
