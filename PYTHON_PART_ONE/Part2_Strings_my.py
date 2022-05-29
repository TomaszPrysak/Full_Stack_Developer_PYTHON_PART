#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_string1 = "testujemy"
print(my_string1[2:]) # wyśwletlamy znaki o indeksie od 2 do konca
print(my_string1[:3]) # wyśwletlamy znaki o indeksie od 0 do 2 (indeks 3 jest granicą która nie jest brana pod uwagę)
print(my_string1[:]) # wyświetlanie całosci listy, równe jest zwykłemu poleceniu print(string)
print(my_string1[-1]) # wyświetlenie ostatniego indeksu
print(my_string1[:-1]) # wyświetlenie wszystkiego oprocz osatatniego indeksu
print(my_string1[::2]) # wyświetlanie co drugiego znaku pośród wszystkich znaków, 2 oznacza skok miedzy znakami
print(my_string1[::-1]) # sposob iterowania od konca
print(my_string1[-2:]) # wyświetlenie dwóch ostatnich znaków z ciągu w prawidłowej kolejności

# sposob umieszczania stringow w stringu wykorzystująć placeholdery:
my_string2 = "Tutaj wstawimy {x}, a tutaj {y}".format(x="nic",y="cos")
print(my_string2)

my_string3 = "Tutaj wstawimy {1}, a tutaj {0}".format("okejos","pico")
print(my_string3)

my_string4 = "Tutaj wstawimy {}, a tutaj {}".format("pikus","cycus")
print(my_string4)

# możemy dodać sposób formatowania placeholderów umieszczając w nawiasach {} specjalne oznaczenia formatowania
# sposoby stosowania formatowania placeholderów opisano na poniższej stronie internetowej:
# https://www.w3schools.com/python/ref_string_format.asp

my_string5 = "Twój wynik to {x:.0%}".format(x=0.25)
print(my_string5)

my_string6 = "Twój wynik to {0:.0%}".format(0.75)
print(my_string6)

my_string7 = "Twój wynik to {:.0%}".format(0.99)
print(my_string7)

zmienna1 = "gramoforn"
zmienna2 = "czajnik"
print(f"Testujemy {zmienna1} w zaciszu domowym. A w kuchni {zmienna2} gra operę narodową.")
