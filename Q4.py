#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:02:57 2019

@author: kingoking
"""
div = 100
s = 0
num = int(input("Enter a multidigit number(0 - 999): "))
while num!=0:
    val = num // div
    s = s + val
    num = num % div
    div = div // 10    
print("The sum of individual digits is: ", s)