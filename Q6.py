#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:16:21 2019

@author: kingoking
"""
def fun():
    v0 = eval(input("Enter initial velocity(in m/s): "))
    v1 = eval(input("Enter final velocity(in m/s): "))
    t = eval(input("Enter time(in seconds): "))
    a = (v1-v0)/t
    print("The average acceleration is: ",a)
fun()