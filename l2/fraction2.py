# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:32:37 2020

@author: Owner
"""


class fraction:
    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b
        
    def disp(self):
        print(str(self.numerator) + "/" + str(self.denominator))
        
    def __add__(self, b):
        return fraction(self.numerator*b.denominator+self.denominator
                        *b.numerator, self.denominator*b.denominator)