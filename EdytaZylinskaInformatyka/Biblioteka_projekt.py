# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:39:05 2021

@author: ania
"""
import pandas as pd

def Komunikat(tekst):
    input(tekst+"\n\nWCIŚNIJ ENTER ŻEBY KONTYNUOWAĆ")

def WczytajDane():
    data = pd.read_excel('MagazynKsiazek.xlsx',"Sheet1", index_col=0)
    data = pd.DataFrame(data)
    return data

def PokazPozycje(data):
    ilosc_pozycji=len(data)
    if(ilosc_pozycji<1):
        Komunikat("Brak ksiązek w magazynie!")
    else:
        print(data)
        print("")
     
def DodajPozycje(data):
    print("Podaj dane:")
    tytul=input("Tytuł: ")
    autor=input("Autor: ")
    wydawnictwo=input("Wydawnictwo: ")
    ilosc_stron=input("Ilość stron: ")
    rok_wydania=input("Rok wydania: ")
    new_row={'Tytuł':tytul,'Autor':autor,'Wydawnictwo': wydawnictwo,'Ilość stron':ilosc_stron,'Rok wydania':rok_wydania}
    data=data.append(new_row,ignore_index=True)
    try:   
        data.to_excel("MagazynKsiazek.xlsx")
        Komunikat("Pomyslnie dodano ksiązkę")
    except:
        Komunikat("ZAMKNIJ DOKUMENT A NASTĘPNIE POWTÓRZ ZADANIE!")


def UsunPozycje(data):
    PokazPozycje(data)
    wybor=input("Podaj id ksiązki którą chcesz usunąć: ")
    wybor1=input("Czy na pewno chcesz usunąć książkę o ID="+wybor+" Wpisz t lub n: ")
    if(wybor1=="t"):
        data=data.drop([int(wybor)])
        data=data.reset_index(drop=True)
        try:       
            data.to_excel("MagazynKsiazek.xlsx")
            Komunikat("Pomyslnie usunięto ksiązkę!")
        except:
            Komunikat("ZAMKNIJ DOKUMENT A NASTĘPNIE POWTÓRZ ZADANIE!")
            
    else:
        Komunikat("Nie usunięto ksiązki!")

def EdytujPozycje(data):
    PokazPozycje(data)
    wybor=input("Podaj id ksiązki którą chcesz zedytować: ")
    print("Podaj nowe dane:")
    tytul=input("Tytuł: ")
    autor=input("Autor: ")
    wydawnictwo=input("Wydawnictwo: ")
    ilosc_stron=input("Ilość stron: ")
    rok_wydania=input("Rok wydania: ")
    data.loc[int(wybor),'Tytuł']=tytul
    data.loc[int(wybor),'Autor']=autor
    data.loc[int(wybor),'Wydawnictwo']=wydawnictwo
    data.loc[int(wybor),'Ilość stron']=ilosc_stron
    data.loc[int(wybor),'Rok wydania']=rok_wydania
    wybor1=input("Czy na pewno chcesz zedytować wybraną pozycję? Wpisz t lub n: ")
    if(wybor1=="t"):
        try:
            data.to_excel("MagazynKsiazek.xlsx")
            Komunikat("Pomyslnie zedytowano pozycję!")
        except:
            Komunikat("ZAMKNIJ DOKUMENT A NASTĘPNIE POWTÓRZ ZADANIE!")
    else:
        Komunikat("Anulowano edytowanie pozycji!")

def Menu():
    print("1. Dodaj pozycję\n2. Usuń pozycję\n3. Pokaż wszystkie pozycje\n4. Edytuj pozycję\n5. Wyjdź z programu")


while 1:
    Menu()
    wybor=input("Wybierz: ")
    if(wybor == "1"):
        dane=WczytajDane()
        DodajPozycje(dane)
    elif(wybor=="2"):
        dane=WczytajDane()
        UsunPozycje(dane)
    elif(wybor == "3"):
        dane=WczytajDane()
        PokazPozycje(dane)
    elif(wybor=="4"):
        dane=WczytajDane()
        EdytujPozycje(dane)
    elif(wybor=="5"):
        input("Wcisnij \"enter\" żeby kontynuować")
        break
    else:
        print("Zły wybór!")
