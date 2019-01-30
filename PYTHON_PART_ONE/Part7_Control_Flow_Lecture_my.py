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
