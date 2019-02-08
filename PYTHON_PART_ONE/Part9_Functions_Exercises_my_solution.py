#!/usr/bin/env python
# -*- coding: utf-8 -*-

#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Stwórz funkcję, która będzie zwracać True albo False w zleżności od tego czy
# w liście przekazywanej jako argument funkcji będzie znajdować się sekwencja liczb 1,2,3.
# Sekwencja ta musi znajdować się gdziekolwiek w liści, ale muszą one

# Przykłady:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(lst):
	for i in range(len(lst)-2):
		if lst[i] == 1 and lst[i+1] == 2 and lst[i+2] == 3:
			return True
	return False

list1 = [1, 1, 2, 3, 1]
print(arrayCheck(list1))

#####################
## -- PROBLEM 2 -- ##
#####################

# Stwórz funkcję która będzie zwracać ciąg znaków składający się z co drugiego znaku
# z ciagu znaków przekazywanego do funkcji jako argument.

# Przykłady:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(txt):
	result = ""
	for i in range(len(txt)):
		if i % 2 == 0:
			result += txt[i]
	return result

string = "Hi"
print(stringBits(string))

#####################
## -- PROBLEM 3 -- ##
#####################

# Stwórz funkcję która będzie zwracać True jeżeli jeden z ciągów znaków będzie znajdować się w drugim.
# I na odwórt. Pierwotne zadanie brzmiało, żeby funkcja ta zwracała True jeżeli jeden z ciągów znaków
# bedzie znajdował się na samym końcu drugiego i na odwrót. Zrobiłem dwa przykłady.

# Przykłady:

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

# Funkcja do sprawdania czy jeden ze stringów znajduje się w drugim i na odwrót
def end_other1(a, b):
	a = a.lower()
	b = b.lower()
	if a in b:
		return True
	elif b in a:
		return True
	else:
		return False

# Funkcja do sprawdzania czy jeden ze stringów znajduje się na końcu drugiego i na odwrót
def end_other2(a, b):
	a = a.lower()
	b = b.lower()
	# return b.endswith(a) or a.endswith(b) sposób na rozwiązanie zadania z wykorzystaniem specjalnej metody endswith()
	#                                       zwraca ona TRUE jeżeli na końcu ciągu znaków na ktorym została wywołana
	#                                       znajduje się wyszczególniona wartość, czyli inny string.
	return a[-len(b):] == b or b[-len(a):] == a

firstString = "Hiabc"
secondString = "abc"
print(end_other1(firstString, secondString))
print(end_other2(firstString, secondString))

#####################
## -- PROBLEM 4 -- ##
#####################

# Stwórz funkcję która będzie zwracać ciąg znaków w którym każdy znak jest podwojony w stosunku
# do oryginalnego ciągu znaków.

# Przykłady:

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
	result = ""
	for i in str:
		result += i*2
	return result

string2 = "Hi-There"
print(doubleChar(string2))

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Mając 3 wartości będące liczbami całkowitymi, należy stworzyć funkcję która zwóci ich sumę.
# Jednakże, jeśli jedna z tych wartości jest z przedziału 13 - 19 to wówczas przyjmujemy, że jej wartość wynosi 0.

# Jednak należy stworzyć osobną funkcję do sprawdzania czy liczba jest z przedziału 13 - 19 .
# Dodatkowo, jeżeli jest z tego przedziału i jest to 15 lub 16 to niech jej wartość pozostanie taka sama.
# Niech nie przyjmuje wówczas wartości 0.

# Przykład:

# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(lst):
	a = lst[0]
	b = lst[1]
	c = lst[2]
	return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
	if n in [13,14,17,18,19]:
		return 0
	return n

list3 = [2, 13, 1]
print(no_teen_sum(list3))

#####################
## -- PROBLEM 6 -- ##
#####################

# Stwórz funkcję zwracającą ilość parzystych liczb w liście jako argumencie funkcji
#
# Przykłady:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(lst):
	counter = 0
	for i in lst:
		if i % 2 == 0:
			counter += 1
	return counter

list3 = [2, 2, 0]
print(count_evens(list3))
