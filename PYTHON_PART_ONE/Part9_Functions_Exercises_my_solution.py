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

# For example:

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

# For example:

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

# Examples:

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other1(a, b):
	a = a.lower()
	b = b.lower()
	if a in b:
		return True
	elif b in a:
		return True
	else:
		return False

def end_other2(a, b):
	a = a.lower()
	b = b.lower()
	return a[-len(b):] == b or b[-len(a):] == a

firstString = "Hiabc"
secondString = "abc"
print(end_other1(firstString, secondString))
print(end_other2(firstString, secondString))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
	pass



#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
	pass
def fix_teen(n):
	pass

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
	pass
