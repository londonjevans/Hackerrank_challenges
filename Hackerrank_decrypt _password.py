#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:01:09 2020

@author: josevans
"""

# Hacker rank challenge: a password decrypter works as follows;
# given a password, it will replace each number in the password with a 0 and move the number to the front of the string.
# For any pair of characters where the first is lowercase and the second uppercase, it will swap the two and add a * after the second
# Build a decrypter to fix it.

s = '560Pl*0a'

exp_output = '6lP5a'



def decryptPassword(s):
    
    
    dec_list = [*s]
    new_list = []
    news = ''
        
    for i, item in enumerate(dec_list):
        if item == '0':
            new_list.append(i)
    
    new_list.reverse()
    
    for i in range(0, len(new_list)):
        dec_list[new_list[i]] = dec_list[i]
        
    dec_list = dec_list[len(new_list):]
    
    for index, i in enumerate(dec_list):
        try:
            if (dec_list[index].isupper() & dec_list[index+1].islower()):
                b = dec_list[index]
                a = dec_list[index+1]
                dec_list[index] = a
                dec_list[index+1] = b
            
                dec_list[index+2] = ''
        except:
            IndexError()
       
        
    for item in dec_list:
        news = news+item
    s = news
    return s
    
            

