# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:23:28 2022

@author: javie
"""

import random

global out
global password
global list

answer = input('How many characters? (at least 2)')
password = ''

def number2element(number):
    global out
    global list
    
    list = 'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+'0123456789'
    out = list[number]
    return out

def generator(characters):
    
    global out
    global password

    password = ''
    element = []
    elementP = []
     
    for i in range(int(characters)):
        element.append(random.randint(0,61))
        elementP.append(element[i])
        number2element(elementP[i])
        password = password + out
        
   
generator(answer)
print("Is " + str(password) + " good enough?")
