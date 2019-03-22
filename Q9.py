#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:27:45 2019

@author: kingoking
"""
def year():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October','November', 'December']
    year, mnth = eval(input("Enter year and month(in number): "))
    if year%4 == 0 and year%400==0: #checking leap year
        res = "leap year"
        days = 29   #special case for february in case of leap year
    else:
        res = "not leap year"
        days = 28
        
    if mnth == 9 or mnth == 4 or mnth == 6 or mnth == 11:
        mnth = mnth - 1  #inorder to access elements of list since its index starts from 0
        print("{} {} is a {} year, and had {} days".format(months[mnth], year, res, 30))
    elif mnth == 2:
        mnth = mnth - 1 #inorder to access elements of list since its index starts from 0
        print("{} {} is a {} year, and had {} days".format(months[mnth], year, res, days))
    else:
        mnth = mnth - 1 #inorder to access elements of list since its index starts from 0
        print("{} {} is a {} year, and had {} days".format(months[mnth], year, res, 31))

year()
        
        
    
        
    