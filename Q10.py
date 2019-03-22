#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 21:11:34 2019

@author: kingoking
"""
import random
scissor = 0
paper = 1
rock = 2
while True:
    comp = random.randint(0,2)
    val = eval(input("Enter 0, 1 or 2 (scissor, paper, rock): "))
    if comp == val:
        print("Draw")
    elif comp == 0 and val == 1 or comp == 1 and val == 2 or comp == 2 and val == 0:
        print("You loose")
    else:
        print("You win")
    choice = input("Do you want to play again(y/n)? ")
    if choice == 'y' or choice == 'Y':
        continue
    else:
        break
