#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 11:45:18 2019
@author: kingoking
"""
#importing value of pi from the math library
from math import pi
radius = eval(input("Enter radius of base of cylinder: "))
length = eval(input("Enter the length of cylinder: "))
area = pi * radius**2 #calculating area of base
volume = area * length #calculating volume of cylinder
print("Area of base of cylinder: ", area)
print("Volume of cylinder: ", volume)
