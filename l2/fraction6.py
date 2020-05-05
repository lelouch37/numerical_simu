# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:59:38 2020

@author: Owner
"""


class fraction:
    def __init__(self, a, b):
        self.__numerator = a
        self.__denominator = b
        self.reduction()
        
    def disp(self):
        print(str(self.__numerator) + "/" + str(self.__denominator))
        
    def __add__(self, b):
        c = fraction(self.__numerator*b.__denominator+self.__denominator
                        *b.__numerator, self.__denominator*b.__denominator)
        return c
    
    def __repr__(self):
        return str(self.__numerator) + "/" + str(self.__denominator)
    
    def reduction(self):
        tmp = gcd(self.__numerator, self.__denominator)
        self.__numerator //= tmp
        self.__denominator //= tmp
    
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)