#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:26:52 2020

@author: elliebear
"""

class Geometric_Calc:
    def __init__(self, base, a, b, c, height, length, width, side):
        self.base = base
        self.height = height
        self.length = length
        self.width = width
        self.side = side
        self.a = a
        self.b = b
        self.c = c
        
    def area_square(self):
        area_s = self.side ** 2
        return area_s
    
    def area_rectangle(self):
        area_r = self.length * self.width
        return area_r
    
    def area_triangle(self):
        area_t = self.height * self.base * 0.5
        return area_t
    def pythag_theorem (self):
        c =  (self.a**2) + (self.b**2)
        return c
    
numbers = Geometric_Calc(0, 2, 3, 4,0, 0, 0, 0)
print(numbers.pythag_theorem())