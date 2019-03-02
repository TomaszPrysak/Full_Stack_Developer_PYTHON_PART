#!/usr/bin/env python
# -*- coding: utf-8 -*-

# List Comprehension
# wyrażenia jednolinijkowe do operacji z listami

# 1.1 List Comprehension bez if/else
# Składnia:
# [value for expresion]
lista = [[1,2,3],[4,5,6],[7,8,9]]
firstColumn = [item[0] for item in lista] # jednolinijkowe wyrażenie, które iteruje przez wszystkie elementy listy
# i zwraca te elementy które opisaliśmy zapisaliśmy jako pierwsza składowa całego wyrażenia
# W tym przypadku z pobiera pierwszy element list będących elementami zbiorczej listy i umieszcza w nowej liście
print(firstColumn)

# 1.2 List Comprehension bez if/else
# Składnia:
# [value for expresion]
dictExample = {(36172241, "Zwierzęca klinika w sercu dżungli") : [3, 5, 8, 3, 5, 8, 3850, 6774, 10624, 1, 2, 3], \
                        (36171607, "Maluchy w świecie zwierząt") : [62, 17, 79, 62, 17, 79, 121315, 59828, 181143, 19, 8, 27]}
nowLista3 = [[v,k] for (k,v) in dictExample.items()] # jednolinijkowe wyrażenie, które iteruje przez wszystkie elementy listy
# powstałej w wyniku zastosowania metody items() wywołanej na słowniku. Jak wiem z ćwiczeń w pliku Part4_Dictionaries_my
# metoda items() zwraca listę krotek, gdzie ilość krotek zależy od ilości par klucz/wartość w słowniku na którym wywołaliśmy metodę items().
# Pierwszym elementem krotki jest klucz a drugim wartośc do niego przypisana. I tak dla każdej krotki.
# Następnie w tym przykładzie jednolonikowego wyrażenia iterujemy przez wszystkie elementy listy powstałej w wyniku działania metody items().
# Ponieważ każdy element listy to krotka dwuelementowa (pierwszy element to klucz, drugi to wartość do niego przypisana) to wykorzystując
# konstrukcję (k,v) rozpakowujemy (przypisujemy) sobie do k pierwszy element z krotki, a do v drugi element krotki. Tak jest z każdym przebiegiem przez elementy listy krotek.
# Następnie posiadając zmienne k i v możemy nimi kobinować. Ponieważ pierwsza pozycja w jednolinijkowym wyrażeniu określa to co będzie się znajdować nowo tworzonej liśc,
# to właśnie w tym miejscu używamy tych zmiennych i z nimi kobinujemy.
# W naszym przypadku stworzyliśmy listę, gdzie każdym elementem jest lista dwuelementowa (pierwszy element to wartość przypisana do v, drugim wartość przypisana do k)
print(nowLista3)
# Inne przykłady kombinowania ze zmiennymi do których rozpakowuemy elementy z list, słownikow:
# [v for (k,v) in dictExample.items()] - w tym wypadku wykorzystujemy tylko jedną zmienną do których rozpakowywaliśmy elementy ze słownika
# [v[:-1] for (k,v) in dictExample.items()] - w tym wypadku wykorzystujemy tylko jedną zmienna i wiedząc, że to lista to pobieramy z niej jej ostatni element

# 2. List Comprehension tylko if
# Składnia:
# [value for expression1 if expression2]
line = "pid=344221|vid2=99999|oiid=778987"
nowLista1 = [item.split("=")[1] for item in line.split("|") if item.split("=")[0] == "oiid"] # jednolinijkowe wyrażenie, które iteruje przez wszystkie elementy listy
# która powstaje w momencie użycia metody split("|") na stringu zapisnym w zmiennej line. Powstaje lista:
# [pid=344221, vid2=99999, oiid=778987]
# Każdy z elementów tej listy jest przypisywany do zmiennej item.
# Następnie chcemy się dostać do każdego elementu z wirtualnej listy powyżej i jego pierwszego członu stojącego przed znakiem "="
# Dlatego każdy element dzielimy poprzez metodę split("="). Ponieważ zadaniem jest wybrać tylko te elementy które mają początek "oiid"
# w warunku if zapisujemy nastepujące wyrażenie: if item.split("=")[0] == "oiid".
# Znaczy to tyle, że z każdego elementu item który dzielimy znakiem "=" powstaje lista dwócj elementów, np.:
# [pid, 344221].
# Wówczas pierwszym element wywołujemy za pomocą [0].
# Jeżeli warunek opisnay wyżej zostanie spełniony wówczas wyrażenie zwraca drugi element z powstającej duwelementowej listy, ponieważ zależy nam na wartości.
# Element ten zostaje zpisywany do nowej liście w zmiennej nowLista1.
print(nowLista1)

# UWAGA !!!
# Jeżeli powyższy warunek nie zostanie spełniony wówczasdany element nie trafia do nowej listy. Może się zatem zdażyć taka sytuacja
# że nowo powstała lista będzie pusta. Aby uniknąc tego, możemy zastosować List Comprehension z if oraz else.
# Przykład poniżej.

# 3. List Comprehension z if oraz else
# Składnia:
# [value1 if expression1 else value2 for expression2]
nowLista2 = [item.split("=")[1] if item.split("=")[0] == "oiid" else "nie jest oiidem" for item in line.split("|")] # jednolinijkowe wyrażenie
# bliźniacze do poprzedniego jednak z tą różnicą, że w momencie kiedy element nie spełni naszego warunku wówczas nie zostanie zwrócony element z listy tylko
# w nowej liście zostanie umieszczona wartość po else, tzn.: else "nie jest oiidem"
print(nowLista2)
