#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:50:09 2019
@author: kingoking
"""
class Kolmogorov:
    dataset = [] #empty list for storing datas
    in_ri = [] #for storing calculated (i/N)-ri
    ri_i1N = [] #for storing calculated ri-(i-1)/N
    #D_alpha = 0.0
    def __init__(self, n, alpha):
        self.n = n
        #self.alpha = alpha
        if alpha == 0.01:
            self.D_alpha = 0.669
        elif alpha == 0.05:
            self.D_alpha = 0.565
    def calc(self):
        temp = [] #temporarily stores datas before sorting
        print("Enter the values for this test: ")
#using list comprehension
        temp = [eval(input()) for i in range(0, self.n)]
        temp.sort()
        self.dataset = temp
        for i in range(0, self.n):
            val1 = ((i+1)/self.n) - self.dataset[i]
            val2 = (self.dataset[i] - (i/self.n))
            self.in_ri.append(val1)
            self.ri_i1N.append(val2)
        print("\n")
        for i in range(0, self.n):
            print(self.in_ri[i])
        print("\n")
        for i in range(0, self.n):
             print(self.ri_i1N[i])
        D_plus = max(self.in_ri)
        D_minus = max(self.ri_i1N)
        D_calc = max(D_plus, D_minus)
        print("\n")
        print("Calculated value of D: ",D_calc)
        if D_calc < self.D_alpha:
            print("Data is uniformly distributed")
        else:
            print("Data are non uniformly distributed")
            
N = int(input("Enter the total number of datas: "))
alpha = eval(input("Enter the degree of freedom: "))
Kolmo = Kolmogorov(N, alpha)
Kolmo.calc()