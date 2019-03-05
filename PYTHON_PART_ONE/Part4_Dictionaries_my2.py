#!/urs/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict

# Dict Comprehension
# wyrażenia jednolinijkowe do operacji ze słownikami
# Tutaj jedyną różnicą jest rodzaj nawiasów stosowana w wyrazeniu jednolinijkowym, czylisą klamrowe {}
# No i zawsze na początku wyrażenia stoi cześć prezentująca jak będzie wyglądać para klucz/wartość.
# {klucz: wartośc for elementListy in lista for k, y, z in elementListy}
# Na przykład wyrażenie klucz: wartość może być przedstawione jako: k: (y, z)
# Wówczas klucz to zmienna k, a wartość to krotka utworzona ze zmiennych y i z

#dictBBC = {k: v for line in open('bbc_id.txt', 'r') for (v, k) in (line.strip('\n\r').split("\t"),)} --- jednolinijkowe tworzenie słownika z wartości przechowywanych w pliku,
# k: v - określa jak będzie wyglądać słownik, tzn. k jako klucz i v jako wartość
# for line in open('bbc_id.txt', 'r') - line jako zmienna będąca z zawartością pliku bbc_id.txt
# for (v, k) in (line.strip('\n\r').split("\t"),) - v i k oznaczają zmienne do których rozpakowujęmy kolumny za pomocą polecenia: line.strip('\n\r').split("\t"), ilość tych zmiennych do których rozpakowujemy musi być równa ilości powstałych kolumn po podziale

dictBBC = {k: v for line in open('Part4_Dictionaries_my2.1.txt', 'r') for (v, k) in (line.strip('\n\r').split("\t"),)}

print(dictBBC)
print(len(dictBBC))

dictBBC_2 = {k: v1 for line in open('Part4_Dictionaries_my2.2.txt', 'r') for (v2, v1, k) in (line.strip('\n\r').split("\t"),)}

print(dictBBC_2)
print(len(dictBBC_2))

resultDictSeriesName = {(36172241, "Zwierzęca klinika w sercu dżungli") : [3, 5, 8, 3, 5, 8, 3850, 6774, 10624, 1, 2, 3], \
                        (36171607, "Maluchy w świecie zwierząt") : [62, 17, 79, 62, 17, 79, 121315, 59828, 181143, 19, 8, 27]}

#res_list = [x[0] for x in resultDictSeriesName for v in resultDictSeriesName[x]] --- x to klucz, x[0] to pierwszy element w zbiorze elementów klucza
#res_list = [x[1] for x in resultDictSeriesName for v in resultDictSeriesName[x]] --- x to klucz, x[1] to drugi element w zbiorze elementów klucza
#res_list = [v for x in resultDictSeriesName for v in resultDictSeriesName[x]] --- v to wartości przypisane do klucza x, w  tym przypadku wartości przypisane do klucza będa iterowane, rozpakowywane osobno,
# a więc nie można sobie wybierać, którą wartość ze zbioru przypisnaego do klucza chcemy w finalnej liście
#res_list = [v[0] for k, v in resultDictSeriesName.items()] --- w tym przypadku zmiennej k rozpakowywany jest klucz, a zmiennej v wartości do niego przypisane,
# jednak w przeciwieństwie do przykładu powyżej, do v przypisana jest cała lista wartości przypisanych do klucza, a nie osobno itereowane, dzięki temu możemy wybierać którą wartość chcemy w finalnej liście
#res_list = [v for k, v in resultDictSeriesName.items()] --- to samo co powyżej tylko bez konkretnej wartości a z całą listą
#res_list = [k for k in resultDictSeriesName.keys()] --- w tym przypadku zmiennej k rozpakowujemy zbiór z klucza słownika, jeżeli klucz jest zbiorem,
# wówczas finalna lista będzie składała się z list zawierających wartości wchodzące w skład klucza
#res_list = [k[0] for k in resultDictSeriesName.keys()] --- to samo co wyżej tylko wskazujemy którą wartość ze zbioru będącego kluczem umieścimy w finalnej liści

print(resultDictSeriesName)
res_list = [v[1] for k, v in resultDictSeriesName.items()]
print(res_list)
print(len(res_list))

 ### Zdłączenie dwóch słowników
# resultDict = ({ k: resultDictCookie.get(k, 0) + resultDictNonCookie.get(k, 0) for k in set(resultDictCookie) | set(resultDictNonCookie) })

### Sortowanie słownika
#print(OrderedDict(sorted(resultDictSeriesName.items(), key=lambda x: x[0])))
# x[0] - to nasz klucz
#print(OrderedDict(sorted(resultDictSeriesName.items(), key=lambda x: x[1])))
# x[1] - to nasza wartość przypisana do klucza
#print(OrderedDict(sorted(resultDictSeriesName.items(), key=lambda x: x[0][0])))
# x[0][0] - jeżeli klucz to jakiś zbiór, wiec to będzie pierwsza wartość z tego zbioru
#print(OrderedDict(sorted(resultDictSeriesName.items(), key=lambda x: x[0][1])))
# x[0][1] - jeżeli klucz to jakiś zbiór, wiec to będzie druga wartość z tego zbioru
# i tak dalej
#print(OrderedDict(sorted(resultDictSeriesName.items(), key=lambda x: x[1][4])))
# x[1][4] - jeżeli wartość przypisana do klucza jest zbiorem to

OrderedDict(sorted(resultDictSeriesName.items(), key=lambda x: x[0][1]))
# musimy używać metody OrderedDict przy sortowaniu słownika żeby nie został on zamieniony przez metode "sorted" na listę
# ponieważ metoda "sorted" zwraca posortowaną liste
