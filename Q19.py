#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:00:33 2019
@author: kingoking
"""
class Chi:
    f_table = {}   
    Oi_Ei = []
    dataset = [0.34, 0.90, 0.25, 0.89, 0.87, 0.44, 0.12, 0.21, 
               0.46, 0.67, 0.83, 0.34, 0.79, 0.64, 0.70, 0.81, 
               0.94, 0.74, 0.22, 0.74, 0.96, 0.99, 0.77, 0.56, 
               0.41, 0.51, 0.73, 0.02, 0.47, 0.30, 0.17, 0.82, 
               0.56, 0.47, 0.31, 0.78, 0.05, 0.79, 0.71, 0.23, 
               0.19, 0.82, 0.93, 0.65, 0.37, 0.42, 0.99, 0.17, 
               0.99, 0.46, 0.05, 0.66, 0.10, 0.42, 0.18, 0.49,
               0.42, 0.51, 0.54, 0.01, 0.81, 0.28, 0.69, 0.34,
               0.75, 0.49, 0.72, 0.43, 0.42, 0.97, 0.30, 0.94,
               0.96, 0.58, 0.73, 0.05, 0.06, 0.39, 0.84, 0.24, 
               0.51, 0.64, 0.40, 0.19, 0.79, 0.62, 0.18, 0.26,
               0.97, 0.88, 0.64, 0.47, 0.97, 0.11, 0.29, 0.78]
    def __init__ (self, alpha, dst):
        self.dst = dst
        if alpha == 0.05: #observed value
            self.X_alpha = 9
        else:
            self.X_alpha = eval(input("Chi observation value: "))
        
    def calc(self):
        self.dataset.sort()
        Ei = len(self.dataset)
        for data in self.dataset:
            if data not in self.f_table:
                key = data + dst
                #if data <= data and 
                value = self.dataset.count(key)
                self.f_table[key] = value
#list comprehension for storing 
        
        self.Oi_Ei = [((self.f_table[val] - Ei)**2)/Ei for val in self.f_table]
        print(self.Oi_Ei)

Chi_square = Chi(0.05, 0.04)
Chi_square.calc()
        