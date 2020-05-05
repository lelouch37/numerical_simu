# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:45:43 2020

@author: Owner
"""


class fraction:
    def __init__(self, a, b):
        self.__numerator = a
        self.__denominator = b
        
    def disp(self):
        print(str(self.__numerator) + "/" + str(self.__denominator))
        
    def __add__(self, b):
        return fraction(self.__numerator*b.__denominator+self.__denominator
                        *b.__numerator, self.__denominator*b.__denominator)
    
    def __repr__(self):
        return str(self.__numerator) + "/" + str(self.__denominator)