#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:15:26 2019

@author: kingoking
"""
#Ceaser cipher
def fun():
    txt = input("Enter a plain text: ")
    dist = eval(input("Enter the distance value: "))
    new_txt="" #defining an empty string
    for letter in txt: #taking one letter at a time
        
        #taking the ascii value of a character and adding the distance value 
        val = ord(letter)+dist 
        
 #converting the ascii value into a character and concatenating to the empty string
        new_txt = new_txt + chr(val)
    print("The ciphered text is:\n",new_txt)
fun()