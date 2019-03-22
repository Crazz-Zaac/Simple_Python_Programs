#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 13:16:00 2019

@author: kingoking
"""

weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))
weight = 0.45359237 * weight
height = 0.0254 * height
BMI = weight/(height**2)
print("Your body mass index is: ",BMI)
