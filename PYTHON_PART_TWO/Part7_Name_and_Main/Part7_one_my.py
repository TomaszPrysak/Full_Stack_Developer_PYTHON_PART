#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Część pierwsza:
import Part7_two_my

# Część pierwsza:
print("Uruchomiony został plik Part7_one_my.py, zmienna __name__ ma wartość = {x}".format(x = __name__))

# Część trzecia kropka jeden:
def funkcja_pierwsza():
    print("Funkcja #1 z pliku Part7_one_my.py")
def funkcja_druga():
    print("Funkcja #2 z pliku Part7_one_my.py")

# Część druga:
if __name__ == "__main__":
    print("Plik Part7_one_my.py wykonywany gdy uruchamiany jako plik główny")
    # Część trzecia kropka dwa
    funkcja_pierwsza()
    Part7_two_my.funkcja_trzecia()
else:
    print("Plik Part7_one_my.py wykonywany gdy importowany jako moduł")
