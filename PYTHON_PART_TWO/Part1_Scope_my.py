#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Zasięg zmiennych

# Używanie własnych funkcji w Pythonie powoduje, że znaczenie ma zasięg naszych zmiennych.
# W momencie tworzena zmiennej w pamięci przypisywane jest dla niej miejse.
# Adersem w pamięci do tej zmiennej jest jej nazwa. Oczywiście zmienna w Pythonie przehowuje jakąś wartość.
# Nie można zdeklarować zmiennej bez wartości. Jeżeli chcemy mieć zdeklarowaną zmienną na poczatku kodu
# musimy jej przypisać 0 (zero), bądź "" (pusty string) itd, w zależności od tego jaki to rodzaj zmiennej.
# Tak samo jest z kolekcją elementów. Musimy zdeklarować np.: pustą listę itd.

# Nazwa zmiennej oprócz adresu do przechowywania ma także swój zasięg, tzn. widoczność
# tej zmiennej w innej cześci kodu.

# Zacznijmy od takiego przykładu:

x = 25 # zdeklarownie zmiennej z wartością 25

def scopeDef1():
    x = 50 # nadpisanie tej zmiennej nową wartością
    return x

print(x) # wartość zmiennej X bez wywoływania funkcji pozostanie bez zmian, nie bedzi nadpisana nową wartością.
print(scopeDef1()) # wywołanie funkcji spowoduje zmanę wartości zmiennej X na nową wartość ponieważ w kodzie funkcji zmieniamy jej wartość.

# Powyższy przykład prezentuje ideę zakresu zmiennych.
