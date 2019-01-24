#!/usr/bin/env python
# -*- coding: utf-8 -*-

# List Comprehension
# wyrażenia jednolinijkowe do operacji z listami

lista = [[1,2,3],[4,5,6],[7,8,9]]
firstColumn = [item[0] for item in lista] # jednolinijkowe wyrazenie, które iteruje przez wszystkie elementy listy
# i zwraca elementy według określonego przez nas warunku. Warunek ten stoi na samym początku wyrażenia.
# W tym przypadku z pobiera pierwszy element list będących elementami zbiorczej listy i umieszcza w nowej liście
print(firstColumn)
