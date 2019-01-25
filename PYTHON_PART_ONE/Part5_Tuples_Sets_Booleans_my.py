#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Krotki

# Zbiory są kolekcją uporządkowanych elementów.
# Krotki są podobne do list jednak są kolekcją elementów których nie można zmieniać.
# Jeżeli raz zdefiniujemy krotkę to później nie możemy zmieniać jej elementów oraz dodawać nowych !
# Pomimo tego, że do elementów odwołujemy, tak jak w listach, za pomocą indeksów to jednak nie możemy ich zmieniać.
# Odwoływanie się za pomocą indeksów dokonuje się identycznie tak jak w listach,
# a więc możemy odwoływać się do konkretnego elementu, elementów z określonego przedziału,
# odowłoywać się do co drugiego elementu itd.

tuple = (1,2,"trzeci",4,"piaty")
print(tuple[3]) # zwrócenie elemntu o indeksie 3
print(tuple[:3]) # zwrócenie elementów od indeksu 0 do 2 (indkes 3 jest granicą która nie jest brana pod uwagę)
print(tuple[-1]) # zwrócenie ostatniego elementu
print(tuple[2:]) # zwrócenie elementów od indeksu 2 do ostatniego
print(tuple[::3]) # zwrócenie co trzeciego elementu z pośród wszystkich, zaczynając od początku
print(tuple[:-1]) # zwrócenie wszystkich oprócz ostatniego elementu
print(tuple[::-1]) # zwrócenie wszystkich elementów jednak od ostatniego do pierwszego

print(tuple.index("trzeci")) # zwrócenie indeksu pod którym znajduje się element umieszczony w argumencie metody .index(x), oczywiście element taki musi być w krotce
print(tuple.count("piaty")) # zwraca liczbę wystąpień elementu krotki, który podajemy w argumencie megody .count(x), oczywiście musi on istnieć

# Zbiory

# Są nieuporządkowaną kolekcją elementów, podobnie jak słowniki.
# Jednak do elementów tych nie możemy się w żaden posób odwołać.
# Zbiory zawierają jedynie elementy unikatowe. Jeżeli bysmy chcieli dodać do słownika
# element już w nim wystepujący to nie zostanie on umieszczony po raz kolejny po prostu zbiór się nie zwiększy.

zbior = set()
zbior.add(11)
zbior.add(22)
print(zbior)
zbior.add(11) # ponowne dodanie elementu już występującego w zbiorze spowoduje, że element ten nie doda się poraz kolejny
print(zbior) # zbiór nie zwiększył się.

lista = [1,2,3,4,2,3,4,6,7,8,1,1,1]
print(lista)
uniqeLista = set(lista) # rzutowanie powyższej listy w której występują elementy powtarzające się spowoduje, że lista ta zostanie ograniczona tylko do elementów unikatowyuch
print(uniqeLista)
lista = list(uniqeLista) # tym razem zrzutujemy zbiór znowu do listy i tym samym otrzymujemy listę pozbzwioną elementów powtarzających się.
print(lista)
