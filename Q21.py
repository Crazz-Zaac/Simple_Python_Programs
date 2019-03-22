#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:54:05 2019
@author: kingoking
"""
class Gap_tst:
    dct = {}
    dataset = [4, 1, 3, 5, 1, 7, 2, 8, 2, 0, 7, 
               9, 1, 3, 5, 2, 7, 9, 4, 1, 6, 3,
               3, 9, 6, 3, 4, 8, 2, 3, 1, 9, 4, 
               4, 6, 8, 4, 1, 3, 8, 9, 5, 5, 7, 
               3, 9, 5, 9, 8, 5, 3, 2, 2, 3, 7, 
               4, 7, 0, 3, 6, 3, 5, 9, 9, 5, 5, 
               5, 0, 4, 6, 8, 0, 4, 7, 0, 3, 3, 
               0, 5, 5, 7, 9, 5, 1, 6, 6, 3, 8, 
               8, 8, 9, 2, 9, 1, 8, 5, 4, 4, 5, 
               0, 2, 3, 9, 7, 1, 2, 0, 3, 6, 3]
    def __init__(self, alpha):
        self.alpha = alpha
    
    def calc(self):
        for x in range(10):
            pos = self.dataset.index(x) #position of first x = 0
            for y in range(self.dataset.count(x)):
                count = 0
                v = pos+1
                self.dct[x] = str(v) + " "
                n = v
                while True:
                    if self.dataset[n] != x :
                        count +=1
                        n +=1
                    else:
                        pos = 
                        break
            print(pos)
Gap = Gap_tst(0.05)
Gap.calc()  
