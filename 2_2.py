#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:30:40 2018

@author: behruz
"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None  

def question5(ll, n):
    """
    Finds the element in a singly linked list(ll) 
    that's n elements from the end
    """
    stack = []
    current_node = ll
    
    if n == 0: return None
    
    while current_node.next != None:
      stack.append(current_node)
      current_node = current_node.next
    stack.append(current_node)
    
    if n > len(stack): return None
    
    return stack.pop(len(stack)-n).data
 
### Qustoin 5 Test Cases

print "---------- Question5 Test Cases: ----------\n"

d = Node(14)
c = Node(13)
c.next = d
b = Node(12)
b.next = c
a = Node(11)
a.next = b

print "a(11) --> b(12) --> c(13) --> d(14)"
print "question5(a, 0) = ", question5(a, 0)
print "question5(a, 1) = ", question5(a, 1)
print "question5(a, 2) = ", question5(a, 2)
print "question5(a, 3) = ", question5(a, 3)
print "question5(a, 4) = ", question5(a, 4)
print "question5(a, 5) = ", question5(a, 5)

     