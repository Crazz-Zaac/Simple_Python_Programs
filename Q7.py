#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:29:29 2019

@author: kingoking
"""
import math
def pentagon():
    r = eval(input("Enter length of the center of a pentagon to a vertex: "))
    s = 2*r*math.sin(math.pi/5)
    A = ((3*math.sqrt(3)) / 2) * s**2
    print("Area of the pentagon is: ",A)
pentagon()