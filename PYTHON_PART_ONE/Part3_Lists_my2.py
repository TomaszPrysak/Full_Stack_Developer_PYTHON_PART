#!/usr/bin/env python
# -*- coding: utf-8 -*-

# List Comprehension
# wyrażenia jednolinijkowe do operacji z listami
# Składnia wewnątrz wyrażenia bez rozpakowywania zmiennych:
# [elementListy for elementListy in lista]
# [elementListy for elementListy in lista if elementListy[2] == 3]
# [elementListy if elementListy[2] == 3 else "test" for elementListy in lista]
# Składnia wewnątrz wyrażenia z rozpakowywaniem zmiennych:
# [x for elementListy in lista for x, y  in elementListy]
# [x for elementListy in lista for x, y  in elementListy if y == 4]
# [x if y == 4 else "nie ma" for elementListy in lista for x, y  in elementListy]

# 1. List Comprehension bez if/else
# Składnia:
# [value for expresion]
# Wersja bez rozpakowywania zmiennych:
lista = [[1,2,3],[4,5,6],[7,8,9]]
firstColumn1 = [item[0] for item in lista] # jednolinijkowe wyrażenie, które iteruje przez wszystkie elementy listy
# i zwraca te elementy które opisaliśmy zapisaliśmy jako pierwsza składowa całego wyrażenia
# W tym przypadku z pobiera pierwszy element list będących elementami zbiorczej listy i umieszcza w nowej liście
print(firstColumn1)

# Wersja z rozpakowywaniem zmiennych:
firstColumn11 = [x for x,y,z in lista] # jednolinijkowe wyrażenie, które iteruje przez wszystkie elementy listy.
# Każdy element listy to trój elementowa lista. W związku z tym od razu rozpakowywujemy je do trzech zmiennych.
# Dzięki temu tylko poprzez wskazanie zmiennej umieszczamy ją w nowej liści.
print(firstColumn11)

# Wersja z rozpakowywaniem zmiennych
dictExample = {(36172241, "Zwierzęca klinika w sercu dżungli") : [3, 5, 8, 3, 5, 8, 3850, 6774, 10624, 1, 2, 3], \
                        (36171607, "Maluchy w świecie zwierząt") : [62, 17, 79, 62, 17, 79, 121315, 59828, 181143, 19, 8, 27]}
nowLista12 = [[v,k] for k,v in dictExample.items()] # jednolinijkowe wyrażenie, które iteruje przez wszystkie elementy listy
# powstałej w wyniku zastosowania metody items() wywołanej na słowniku. Jak wiem z ćwiczeń w pliku Part4_Dictionaries_my
# metoda items() zwraca listę krotek, gdzie ilość krotek zależy od ilości par klucz/wartość w słowniku na którym wywołaliśmy metodę items().
# Pierwszym elementem krotki jest klucz a drugim wartośc do niego przypisana. I tak dla każdej krotki.
# Następnie w tym przykładzie jednolonikowego wyrażenia iterujemy przez wszystkie elementy listy powstałej w wyniku działania metody items().
# Ponieważ każdy element listy to krotka dwuelementowa (pierwszy element to klucz, drugi to wartość do niego przypisana) to wykorzystując
# konstrukcję (k,v) rozpakowujemy (przypisujemy) sobie do k pierwszy element z krotki, a do v drugi element krotki. Tak jest z każdym przebiegiem przez elementy listy krotek.
# Następnie posiadając zmienne k i v możemy nimi kobinować. Ponieważ pierwsza pozycja w jednolinijkowym wyrażeniu określa to co będzie się znajdować nowo tworzonej liśc,
# to właśnie w tym miejscu używamy tych zmiennych i z nimi kobinujemy.
# W naszym przypadku stworzyliśmy listę, gdzie każdym elementem jest lista dwuelementowa (pierwszy element to wartość przypisana do v, drugim wartość przypisana do k)
print(nowLista12)
# Inne przykłady kombinowania ze zmiennymi do których rozpakowuemy elementy z list, słownikow:
# [v for (k,v) in dictExample.items()] - w tym wypadku wykorzystujemy tylko jedną zmienną do których rozpakowywaliśmy elementy ze słownika
# [v[:-1] for (k,v) in dictExample.items()] - w tym wypadku wykorzystujemy tylko jedną zmienna i wiedząc, że to lista to pobieramy z niej jej ostatni element

# 2. List Comprehension tylko if
# Składnia:
# [value for expression1 if expression2]
# Wersja bez rozpakowywania zmiennych:
line = "pid=344221|vid2=99999|oiid=778987"
nowLista2 = [item.split("=")[1] for item in line.split("|") if item.split("=")[0] == "oiid"] # jednolinijkowe wyrażenie, które iteruje przez wszystkie elementy listy
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
print(nowLista2)

# [value for expression1 for expression2 if expression3]
# Wersja z rozpakowywaniem zmiennych:
nowLista22 = [y for item in line.split("|") for x,y in (item.split("="),) if x == "oiid"] # to jednolinijkowe wyrażenie ma taki sam skutek jak wyrażenie powyżej.
# Jednakże w tym wypadku wykorzystujemy dodatkowe wyrażenie for/in w celu rozpakowania wartości z item.split("=") do pomocniczych x i y.
# Ponieważ wyrażenie item.split("=") tworzy nam dwuelementową listę, np.: [pid,344221], i tak jest z każda iteracją jednolinijkowego wyrażenia.
# To każdy element z tej dwuelementowej listy rozpakowujemy do zmiennych x i y. Dzięki temu póżniej możemy już posługiwac się tylko tymi zmiennymi.
# Podsumowanie:
# Wyrażenie line.split("|") tworzy nam listę elementów ze stringu. Dzięki temu możemy zastosować jednolinijkowe wyrażenie.
# Nastepnie na każdym element z powstałej listy stosujemy wyrażenie item.split("=") co pozwala nam stworzyć dwuelementowe listy z których każdy element rozpakowujemy do innej zmiennej, w tym wypadku x, y.
# A następnie posługujemy się tylko tymi zmiennymi
print(nowLista22)

# UWAGA !!!
# Jeżeli powyższy warunek nie zostanie spełniony wówczasdany element nie trafia do nowej listy. Może się zatem zdażyć taka sytuacja
# że nowo powstała lista będzie pusta. Aby uniknąc tego, możemy zastosować List Comprehension z if oraz else.
# Przykład poniżej.

# 3. List Comprehension z if oraz else
# Składnia:
# [value1 if expression1 else value2 for expression2]
# Wersja bez rozpakowywania zmiennych:
nowLista3 = [item.split("=")[1] if item.split("=")[0] == "oiid" else "nie jest oiidem" for item in line.split("|")] # jednolinijkowe wyrażenie
# bliźniacze do poprzedniego jednak z tą różnicą, że w momencie kiedy element nie spełni naszego warunku wówczas nie zostanie zwrócony element z listy tylko
# w nowej liście zostanie umieszczona wartość po else, tzn.: else "nie jest oiidem"
print(nowLista3)

# Wersja z rozpakowywaniem zmiennych:
nowLista33 = [y if x == "oiid" else "nie jest oiidem" for item in line.split("|") for x,y in (item.split("="),)] # jednolinijkowe z rozpakowywaniem zmiennych tak jak w podpunkcie drugim,
# dodano jedynie else.
print(nowLista33)
