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

# IF / ELSE
# Czasami musimy zastosować wyrażenie warunkowe zawierające tylko if oraz else, nie zawierające elif.
# Wówczas w celu zapisu jak najmniejszej ilości kodu możemy wykorzystać wyrażenie trójargumentowe.
# Składnia:
# wynik_gdy_prawda if warunek else wynik_gdy_fałsz
# Na przykład:
aa = 5
bb = 4
print("Ala ma kota" if aa > bb else "kot ma Ale")

# Pętla FOR

# Podczas iterowania przez elementy (pary klucz:wartość) słownika za pomocą petli FOR do zmiennej
# zaposanej w konstrukcji pętli przypisywane są klucze elementów słownika.
# Należy pamiętać, że słowniki są zbiorem elementów nieuporządkowanych, dlatego podczas
# iterowania przez słownik nigdy elementy nie będą zwracane w jakiejś kolejności.
# Jeżeli tak będzie to jest to tylko przypadek. W kolejnej iteracji będzie już inaczej.

dict = {"romek":1,"atomek":2}
# 1. Sposób
for key in dict:
    print(key)
    print(dict[key])
# 2. Sposób
for key, item in dict.iteritems():
	print(key)
	print(item)

# W Pythonie, w trakcie iterowania pętlą FOR przez elementy kolekcji, której poszczególne elementy są również kolekcjami,
# mamy możliwość rozpoakowywania elementów tej wewnętrznej kolekcji do pojedynczych zmiennych zapisanych w konstrukcji pętli.

lista = [[1,2],[3,4],[5,6]]
for listaItem1, listaItem2 in lista:
    print(listaItem1)
    print(listaItem2)

lista2 = [("a","b"),("c","d")]
for lista2Item1, lista2Item2 in lista2:
    print(lista2Item1)
    print(lista2Item2)

lista3 = [("a","b"),("c","d")]
for index, item in enumerate(lista3):
	print(index)
	print(item)

# Pętla WHILE

# Wykonywana jest ona dopóty, dopóki spełniony jest warunek postawiony w konstrukcji pętli

i = 1
while i < 5:
    print("i: {i}".format(i=i))
    i *= 2

# Słówko kluczowe "break"

# Umieszczenie słówka "break" w pętli spowoduje natychmiastowe przerwanie pętli i wyjście z niej bez
# wykonania kodu który znajduje się za tym słówkiem kluczowym.

lst = [1,2,3,4,5,6]

for item in lst:
	if item < 4:
		print("Jestem jeszcze w pętli")
	else:
		print("upppssss, przed nami break")
		break

# Słówko kluczowe "continue"

# Umieszcenie słówka "continue" w pętli spowoduje przeskoczenie do kolejnej iteracji pętli.

lst2 = ["1",2,"3",4,"5",6]

for item in lst2:
	if type(item) == type("test"): continue
	print(item)

# Funkcja range()

# range(arg1, arg2, arg3) # metoda ta słuzy do generowania list złożonych z liczb całkowitych
# arg1 - pierwsza liczba listy,
# arg2 - granica listy, liczba która nie wchodzi w skład lity, ostatnia liczba która wchodzi jest o jeden mniejsza od arg2
# arg3 - opcjonalny argument, oznacza krok pomiędzy nastepującymi sobie elementami listy stworzonej przez range()
#        jeżeli nic nie podamy, wówczas krokiem bedzie 1, a wiec kolejne liczby listy będa większe od poprzedniej o jeden,
#        jeżeli podamy 5 wówczas kolejne liczby będą się różniły o pięć, i tak dalej

# range() wykorzystujemy do generowania list służących jako "iteratory" do pętli FOR.
# Pozwoli to zaoszczędzić pamięć w momencie jezeli mamy do przeiterowania przez listę która zaweira
# dużą ilosć elementów różnego typu. Wówczas tworzymy sobie za pomocą range() listę do iterowania prez naszą właściwą listę.
# Wówczas range() konstryujemy od 0 do liczby będącej długością listy pierwotnej.

dziwnaLista = [1,"kapibara",44,"ułahili",2,"jupikajej",555]

for item in range(0, len(dziwnaLista)):
    print(dziwnaLista[item])

# nie musimy cały czas trzymać listy dziwnaLista w pamięci podczas iterowania.

# List Comprehension

# Omawialiśmy już ten sposób w rozdziale: Part3_Lists_my2
# Teraz tylko przerobimy przykład.

x = [1,2,3,4]

y = [itemX**2 for itemX in x]

print(y)
