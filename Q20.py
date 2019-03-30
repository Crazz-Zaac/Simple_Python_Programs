#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:04:02 2019

@author: kingoking
"""
class Run:
    
    sgn = []
    dataset = [0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 
               0.62, 0.36, 0.27, 0.19, 0.72, 0.75, 0.08, 
               0.54, 0.02, 0.01, 0.36, 0.19, 0.28, 0.18,
               0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32,
               0.82, 0.53, 0.31, 0.42, 0.73, 0.04, 0.83, 
               0.45, 0.13, 0.57, 0.63, 0.29]
    def __init__(self, alpha):
        if alpha==0.5:
            self.Z=1.96
        else:
            self.Z = eval(input("Enter observed value: "))
    
    def calc(self):
        count=0
        for i in range(len(self.dataset)-1):
            chk=self.dataset[i+1]-self.dataset[i]
            if chk<0:
                self.sgn.append(0)
            elif chk>=0:
                self.sgn.append(1)
       
        for i in range(len(self.sgn)-1):
            if self.sgn[i]==self.sgn[i+1] or self.sgn[i]==1 and self.sgn[i+1]==0:
                flag=1
                print(flag)
            elif self.sgn[i]==0 and self.sgn[i+1]==1:
                flag=1
                print(flag)
            count += flag
#        print(count)
#            elif self.sgn[i+1] == 0 and self.sgn[i] == 1:
#                self.count += 1
#            elif self.sgn[i+1] == 1 and self.sgn[i] == 0:
#                self.count += 1
        print("\n")    
        print(self.sgn)
#        print(len(self.sgn))
        

Run_tst = Run(0.5)
Run_tst.calc()
                       
