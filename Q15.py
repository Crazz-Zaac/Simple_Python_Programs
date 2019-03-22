#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:15:26 2019

@author: kingoking
"""

def find():
    f1 = open("/home/kingoking/Desktop/new.txt", 'r', encoding= 'utf-8')
    f2 = open("/home/kingoking/Desktop/find.txt", 'w+', encoding= 'utf-8')
#a list for comparing inorder to remove the numbers
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    txt = f1.read().lower()
    for data in txt:
    #checking if the the character read does not match with the numbers in list
        if data not in lst:
    #concatenating and writing the content to the file
            word = "" +data
            f2.writelines(word)
#closing the files
    f1.close()
    f2.close()
        
find()