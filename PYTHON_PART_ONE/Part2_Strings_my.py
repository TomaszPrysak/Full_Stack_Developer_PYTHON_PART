#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_string1 = "testujemy"
print(my_string1[2:]) # wyśwletlamy znaki o indeksie od 2 do konca
print(my_string1[:3]) # wyśwletlamy znaki o indeksie od 0 do 2 (indeks 3 jest granicś która nie jest brana pod uwagę)
print(my_string1[:]) # wyświetlanie całosci listy, równe jest zwykłemu poleceniu print(string)
print(my_string1[-1]) # wyświetlenie ostatniego indeksu
print(my_string1[:-1]) # wyświetlenie wszystkiego oprocz osatatniego indeksu
print(my_string1[::2]) # wyświetlanie co drugiego znaku pośród wszystkich znaków, 2 oznacza skok miedzy znakami
print(my_string1[::-1]) # sposob iterowania od konca
print(my_string1[-2:]) # wyświetlenie dwóch ostatnich znaków z ciągu w prawidłowej kolejności

# sposob umieszczania stringow w stringu
my_string2 = "Tutaj wstawimy {x}, a tutaj {y}".format(x="nic",y="cos")
print(my_string2)
