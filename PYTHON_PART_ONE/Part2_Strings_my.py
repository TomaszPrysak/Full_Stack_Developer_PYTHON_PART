#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_string1 = "testujemy"
print(my_string1[2:]) # wyswletlamy znaki o indeksie od 2 do konca
print(my_string1[:3]) # wyswletlamy znaki o indeksie od 0 do 2 (indeks 3 jest granica ktora nie jest brana pod uwage)
print(my_string1[:]) # wyswietlanie calosci, rowne jest zwyklemu poleceniu print(string)
print(my_string1[-1]) # wyswietlenie ostatniego indeksu
print(my_string1[:-1]) # wyswietlenie wszystkiego oprocz osatatniego indeksu
print(my_string1[::2]) # wyswietlanie co drugiego znaku posorb wszystkich znakow, 2 oznacza skok miedzy znakami
print(my_string1[::-1]) # sposob iterowania od konca
# sposob umieszczania stringow w stringu
my_string2 = "Tutaj wstawimy {x}, a tutaj {y}".format(x="nic",y="cos")
print(my_string2)
