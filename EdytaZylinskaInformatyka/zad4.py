# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:38:37 2021

@author: Edyta
"""

liczba = int(input("Ile liczb będzie podanych? "))

tablica = []

for i in range(liczba):
    kolejna = int(input("Podaj kolejną liczbę: "))
    tablica.append(kolejna)

print("Wczytano " + str(tablica))

tablica = sorted(tablica)

print("Posortowane: " + str(tablica))
