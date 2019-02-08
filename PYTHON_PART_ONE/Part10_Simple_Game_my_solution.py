#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################
###    PART 10: Simple Game    ###
###        ŁAMACZKODÓW         ###
## --Pudlo--Blisko--Trafiles--  ##
##################################

# Gra działająca w oparicu o wiersz poleceń.

# Komputer losuje 3 liczby z przedziału 1 - 10.
# Zadaniem użytkownika jest zgadnąć te liczby.

# Zgadywanie odbywa się poprzez wpisywanie, ciągiem, propozycji liczb użytkownika, np.: 377. Gdzie 3 to pierwsza liczba itd.
# Natepnie w wierszu poleceń komputer przekazuje wskazówki dotyczące typowań użytkownika.

# Są następujące możliwe wskazówki:
# - Tragiles - jeżeli użytkownik zgadł liczbę w swoim dokładnym położeniu
# - Blisko - jeżeli liczb którą podał użytkownik jest wylosowana przez komputer, ale nie w tym położeniu w którym wskazał użytkownik
# - Pudlo - jeżeli liczba wskazana przez uzytkownika nie znajduje się w wylosowanych przez komputer w żadnym położenie.

# Na przykład:
# Komputer wylosował: 482 (oczywiście użytkownik tego nie wie)
# Użytkownik typuje: 281
# Komunikat jest następujący: 1 liczba: Blisko 2 liczba: Trafiles 3 liczba: Pudlo
# Oznacza to, że pierwsza liczba jest w innym położeniu niż zaproponował użytkownik, ale jest jedną z liczb które wylosował komputer.
# Drugą liczbę użytkownik odgadł, natomiast trzecia jest nietrafiona.

# Gra toczy się, aż do momentu użytkownik trafi wszytkie liczby.

# Miłej zabawy

import random

computerNumbers = list(range(1,10))
random.shuffle(computerNumbers)
computerNumbers = computerNumbers[:3]
odpowiedzi = []
# print(computerNumbers)

print("Przez komputer zostaly wylosowane 3 liczby")

def checkUserNumber(num):
	odpowiedzi = []
	for index, var in enumerate(num):
		if int(var) == computerNumbers[index]:
			odpowiedzi.append("Trafiles")
		elif int(var) in computerNumbers:
			odpowiedzi.append("Blisko")
		else:
			odpowiedzi.append("Pudlo")
	return odpowiedzi

while odpowiedzi.count("Trafiles") < 3:
	number = str(input("Zgadnij liczby wylosowane przez komputer w odpowiedniej kolejnosci: "))
	odpowiedzi = checkUserNumber(number)
	print("Twoje odpowiedzi mialy nastepujaca skutecznosc: 1 liczba: {x} 2 liczba: {y} 3 liczba: {z}".format(x=odpowiedzi[0], y=odpowiedzi[1], z=odpowiedzi[2]))

print("Brawo zgadles liczby komputera\nA byly to: {x}, {y}, {z}".format(x=computerNumbers[0], y=computerNumbers[1], z=computerNumbers[2]))
