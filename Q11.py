#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:13:43 2019

@author: kingoking
"""

def check():
    x1, y1 = eval(input("Enter center (x, y) coordinate of first rectangle: "))
    w1, h1 = eval(input("Enter width and height of first rectangle: "))
    x2, y2 = eval(input("Enter center (x, y) coordinate of second rectangle: "))
    w2, h2 = eval(input("Enter width and height of second rectangle: "))
    
    if (x1==x2 and y1==y2 ) and (w1 > w2 and h1 > h2):
        print("The second rectangle is inside the first" )
    elif (x1==x2 and y1==y2 ) and (w1 == w2 and h1 == h2):
        print("The second rectangle over the first rectangle" )
    elif(x1):
        
    elif(x1!=x2 and y1!=y2 ) and (w1 != w2 and h1 != h2):
        print("The rectangles are completely apart from each other" )
    else:
        print("The second is overlapping the first rectangle" )

check()
    
    
    