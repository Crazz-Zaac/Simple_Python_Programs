#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 06:32:41 2019
@author: kingoking
"""
#importing re library to work with string expressions
import re
def fun():
    #reading file and creating another text file, file1 to store the result
    file = open("/home/kingoking/Desktop/text.txt", 'r', encoding= 'utf-8')
    file1 = open("/home/kingoking/Desktop/text2.txt", 'w+', encoding = 'utf-8')
    #reading the content and converting into lowercase
    txt = file.read().lower() 
    
    #making a list of the contents in file excluding two letter words 
    #such as in, of, at, be, etc. It also excludes 'a'. 
    chk_pattern = re.findall(r'\b[a-z]{3,15}\b', txt)
    for word in chk_pattern:
        #counting the words in the list of same type from the list
        num = chk_pattern.count(word) 
        #concatenating the string for writing in file1
        content = word + "\t\t\t" + str(num) + "\n"
        
        #writing the content to file1
        file1.write(content)
        print(content)
    #finally closing the file and file1 
    file.close()
    file1.close()

fun()
    
    