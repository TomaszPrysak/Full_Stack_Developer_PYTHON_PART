#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = ["a","b","c","d"]
print(lista)

lista2 = ["x","y","z"]

lista2.append("o") # dodawanie nowego elementu na koniec listy
print(lista2)

lista.extend(lista2) # dodanie elementów jednej listy do elementów drugiej listy za pomocą metody extend, dodanie listy nastąpi na końcu pierwszej listy
lista3 = lista + lista2 # dodanie elementów jednej listy do drugiej poprzez konkatenację. Musimy użyć tutaj dodatkowej zmiennej, ponieważ oryginalne listy się nie zmieniają
print(lista)
print(lista3)
lista4 = lista3 * 2 # podwojenie listy o te same elementy dodane na samym końcu
print(lista4)

item1 = lista4.pop() # metoda pop służy do zwrócenia elementu o konkretnym indeksie (jeżeli nie podamy, żadnego indkesu w nawiasach to wyciągniemy ostatni element)
# jednocześnie nie dość, że zwracamy element listy to usuwamy go z listy
print(item1)
print(lista4)
item2 = lista4.pop(0) # zwrócenie i usunięcie z listy elementu o indeksie 0
print(item2)
print(lista4)
item3 = lista4.pop(5) # zwrócenie i usunięcie z listy elementu o indeksie 5
print(item3)
print(lista4)

lista3.reverse() # odwrócenie listy
print(lista3)

lista5 = [3,5,11,7,9,2]
lista5.sort() # sortowanie listy, w zależności od rodzaju danych, python przyjmuje różne posoby sortowania
print(lista5)
