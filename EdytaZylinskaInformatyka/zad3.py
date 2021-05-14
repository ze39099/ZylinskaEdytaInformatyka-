# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:38:37 2021

@author: Edyta
"""

a = 5
b = 50

suma = 0
liczbaLiczbNieparzystych = 0

for zmienna in range(a, b + 1):
    if zmienna % 2==1:
        suma = suma + zmienna
        liczbaLiczbNieparzystych = liczbaLiczbNieparzystych + 1

srednia = suma / liczbaLiczbNieparzystych

print(srednia)
