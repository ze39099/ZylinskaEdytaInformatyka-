# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:30:55 2021

@author: Edyta
"""
def srednia(a,b):
    if a>0 and b>a:
        suma_niepodzielnych=0
        suma=0;
        for i in range(a,b+1):
            if i%2:
                suma_niepodzielnych+=1
                suma=suma+i
        print("Śrenia arytmetyczna liczb nieparzystych z przedziału:",a,b,"wynosi:",suma/suma_niepodzielnych)
    else:
        print("Podano nieprwidłowy przedział!")
            
    
   
    
   
    
a=input("Podaj początek przedziału:")
b=input("Podaj koniec przedziału:")

srednia(int(a),int(b))
    

    
        
        