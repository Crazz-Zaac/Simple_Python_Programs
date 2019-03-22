#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 23:19:22 2019

@author: kingoking
"""

def conv(num):
    res = 0
    i = 0
    while num != 0: #until the remainder is 0
        q = num % 10 
        res = res + q * (8**i) 
        num = num // 10
        i += 1
    print("Equivalent octal vale is: ",res)    
data = eval(input("Enter an Octal number(0-7): "))
conv(data) #calling function conv with parameter data