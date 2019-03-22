#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 08:07:33 2019
@author: kingoking
"""
#import nltk library for using the stopwords library
from nltk.corpus import stopwords
def stp():
     f1 = open("/home/kingoking/Desktop/hello.txt", 'r', encoding= 'utf-8')
     f2 = open("/home/kingoking/Desktop/stpword.txt", 'w+', encoding= 'utf-8')
     #storing the english stopwords in stpwrd as a list
     stpwrd = stopwords.words('english') 
     txt = f1.read() #reading content from the file
     content = txt.split()
     for word in content:
         #checking if the word in content matches with word in the list
         if word in stpwrd: 
        #if the matched we remove that word from the content list
             content.remove(word)
         else:
    #we concatenate the overall string and write it on the file
             val = " "+ word
             f2.writelines(val)
    #closing both the files
     f1.close()
     f2.close()

stp()