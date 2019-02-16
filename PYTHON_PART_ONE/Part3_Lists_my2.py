#!/usr/bin/env python
# -*- coding: utf-8 -*-

# List Comprehension
# wyrażenia jednolinijkowe do operacji z listami

lista = [[1,2,3],[4,5,6],[7,8,9]]

# List Comprehension bez if/else
firstColumn = [item[0] for item in lista] # jednolinijkowe wyrażenie, które iteruje przez wszystkie elementy listy
# i zwraca te elementy które opisaliśmy zapisaliśmy jako pierwsza składowa całego wyrażenia
# W tym przypadku z pobiera pierwszy element list będących elementami zbiorczej listy i umieszcza w nowej liście

print(firstColumn)

line = "pid=344221|vid2=99999|oiid=778987"

# List Comprehension tylko if
# [value for expression1 if expression2]
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
# UWAGA !!!
# Jeżeli powyższy warunek nie zostanie spełniony wówczasdany element nie trafia do nowej listy. Może się zatem zdażyć taka sytuacja
# że nowo powstała lista będzie pusta. Aby uniknąc tego, możemy zastosować List Comprehension z if oraz else.
# Przykład poniżej.

# List Comprehension z if oraz else
# [value1 if expression1 else value2 for expression2]
nowLista2 = [item.split("=")[1] if item.split("=")[0] == "oiid" else "nie jest oiidem" for item in line.split("|")] # jednolinijkowe wyrażenie
# bliźniacze do poprzedniego jednak z tą różnicą, że w momencie kiedy element nie spełni naszego warunku wówczas nie zostanie zwrócony element z lity tylko
# w nowej liści zostanie umieszczona wartość po else, tzn.: else "nie jest oiidem"

print(nowLista1)
print(nowLista2)
