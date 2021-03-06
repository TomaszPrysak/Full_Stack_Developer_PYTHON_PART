#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Słowniki są to zbiór par klucz/wartość. Jednak pierwotne zdefiniowanie słownika z
# parami klucz/wartość nie określa jednocześnie takiej kolejności. Wszystko co umieszczamy w słowniku
# nie ma określonego położenia w nim. Jeżeli byśmy iterowali przez słownik to pary klucz/wartość
# będą w losowej kolejności. Słowniki są nieuporządkowanym zbiorem elementów. Do konkretnych wartości
# odowłujemy się za pomocą klucza

# Słowniki w Pythonie posiadają wbudowane metody do inkrementowania, dekrementowania, mnożenia oraz dzielenia
# wartości przypisanej do klucza. Odbuwa się to tak samo jako te same operacje jakiekolwiek zmiennej.
# Wykorzystujemy:
# +=
# -=
# *=
# /=

dict = {"key1":3, "key2":5}
print(dict["key1"])
dict["key1"] += 1
print(dict["key1"])
dict["key1"] *= 2
print(dict["key1"])
dict["key2"] -= 1
print(dict["key2"])
dict["key2"] /= 2
print(dict["key2"])

print(dict.keys()) # zwraca listę kluczy w słowniku, list ta będzie nieposortowana
print(dict.values()) # listę wartości przypisanych do kluczy, lista ta również nie będzie posortowana
print(dict.items()) # zwraca listę krotek, ilość par klucz/wartość oznacza taką samą ilość zwróconych krotek.
# każda krotka będzie złożona z klucza i przypisanej do niej wartości.
print(dict.get("key1","nieee mmmaaaaa")) # zwraca wartość klucza podanego w pierwszym arugmencie,
# jeżeli klucz podany w pierwszym argumencie nie istnieje, wówczas zwraca wartość NONE jezeli nie podaliśmy drugiego argumentu.
# Jeżeli podamy drugi argument wówczas on będzie zwrócony w momencie jak klucz z pierwszego argumentu nie będzie występować
# w słowniku na którym metoda get() została wywołana.
print(dict.get("key3",1)) # to samo co powyżej tylko juz z przykładem braku klucza w słowniku
print(dict.iteritems()) # zwraca obiekt będący iteratorem przez słownik
