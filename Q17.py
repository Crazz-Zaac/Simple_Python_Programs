#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 05:53:50 2019

@author: kingoking
"""
class Rng:
    val = []
    def __init__(self, a, b, r0, m): #constructor
#it is called as soon as the object of this 
        self.a = a
        self.b = b
        self.r0 = r0
        self.m = m
    
    def calc(self):
        
        while True:
            if self.a>1 and self.b>0: #mixed multiplicative RNG
                r1 = (self.a*self.r0 + self.b) % self.m
                Rng.val.append(r1)
                print(r1)
#checking duplicate value in the list so as to stop  the calculation
                if self.r0 in Rng.val and Rng.val.count(self.r0)>=2:
                    break
                self.r0 = r1     
            elif self.a == 1:#additive congurential RNG
                r1 = (self.a*self.r0 + self.b) % self.m
                Rng.val.append(r1)
                print(r1)
                if self.r0 in Rng.val and Rng.val.count(self.r0)>=2:
                    break
                self.r0 = r1                    
            elif self.b == 0:#multiplicative congurential RNG
                r1 = (self.a * self.r0) % self.m
                Rng.val.append(r1)
                print(r1)
                if self.r0 in Rng.val and Rng.val.count(self.r0)>=2:
                    break
                self.r0 = r1
#creating object of the class and passing values through it 
#these values are automatically initialized by __ini__ function
r1 = Rng(13, 1, 1, 19) 
r1.calc()