#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:43:14 2019
@author: kingoking
"""
import random
def check():
    num = random.randint(10,99)
    ans = (num // 10) + (num % 10)
    guess = eval(input("Predict the sum: "))    
    print("Generated number: {}\nActual sum: {}\nYour guessed sum: {}\n".format(num, ans, guess))
    if guess == ans:
        print("You win!!")    
    else:
        print("You loose!!")

check()