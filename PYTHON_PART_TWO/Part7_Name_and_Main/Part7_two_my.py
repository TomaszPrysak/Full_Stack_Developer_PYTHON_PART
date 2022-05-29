#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Część pierwsza:
print("Uruchomiony został plik Part7_two_my.py, zmienna __name__ ma wartość = {x}".format(x = __name__))

# Część trzecia kropka jeden:
def funkcja_trzecia():
    print("Funkcja #3 z pliku Part7_two_my.py")
def funkcja_czwarta():
    print("Funkcja #4 z pliku Part7_two_my.py")

# Część druga:
if __name__ == "__main__":
    print("Plik Part7_two_my.py wykonywany gdy uruchamiany jako plik główny")
else:
    print("Plik Part7_two_my.py wykonywany gdy importowany jako moduł")
    # Część trzecia kropka trzy:
    funkcja_czwarta()
