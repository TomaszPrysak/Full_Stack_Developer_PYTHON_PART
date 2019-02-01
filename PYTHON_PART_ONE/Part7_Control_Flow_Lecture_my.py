#!/usr/bin/env python
# -*- coding: utf-8 -*-

# W Pythonie podczas porównywania zmiennych najpierw sprawdzany jest typ porównywanych zmiennych.
# Jeżeli różnią się typem (integer, string, float) to całe wyrażenie jest fałszem.
# Python, w przeciwieństwie do JavaScript, w przypadku porównywania: ==,
# nie próbuje rzutować porównywanych zmiennych do wspólnego typu i dopiero porównywać
# ich wartośco wartości.

print(1 == "1")
print(1 == 1)
print("tak" == "nie")

# Pętla FOR

# Podczas iterowania przez elementy (pary klucz:wartość) słownika za pomocą petli FOR do zmiennej
# zaposanej w konstrukcji pętli przypisywane są klucze elementów słownika.
# Należy pamiętać, że słowniki są zbiorem elementów nieuporządkowanych, dlatego podczas
# iterowania przez słownik nigdy elementy nie będą zwracane w jakiejś kolejności.
# Jeżeli tak będzie to jest to tylko przypadek. W kolejnym przypadku już tak nie będzie.

dict = {"romek":1,"atomek":2}
for key in dict:
    print(key)
    print(dict[key])

# W Pythonie, w trakcie iterowania pętlą FOR przez elementy kolekcji, której poszczególne elementy są również kolekcjami,
# mamy możliwość rozpoakowywania elementów tej wewnętrznej kolekcji do pojedynczych zmiennych zapisanych
# w konstrukcji pętli.

lista = [[1,2],[3,4],[5,6]]
for listaItem1, listaItem2 in lista:
    print(listaItem1)
    print(listaItem2)

lista2 = [("a","b"),("c","d")]
for lista2Item1, lista2Item2 in lista2:
    print(lista2Item1)
    print(lista2Item2)
