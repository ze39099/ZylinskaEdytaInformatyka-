# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:00:18 2021

@author: Edyta
"""

def funkcja(x):
    for i in range(-x,x+1):
        if i%2==0:
            print(i)

x=input("Podaj x: ")
funkcja(int(x))
            
         
            