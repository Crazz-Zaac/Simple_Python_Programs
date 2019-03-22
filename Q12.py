#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 23:01:58 2019

@author: kingoking
"""
def conv(num):
    res =' ' #empty string for storing the calculted value as string
    while num != 0: #until the remainder is 0
        q = num % 8 #calculating the quotient
        res = str(q) + res #concatinating after conversion
        num = num // 8 #updating the value of num with remainder after division
    print("Equivalent octal vale is: ",res)
    
data = eval(input("Enter a decimal number(0-9): "))
conv(data)