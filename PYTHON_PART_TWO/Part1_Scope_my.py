#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/////////////////
#/////////////////
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
print("#####")
x1 = 25 # zdeklarownie zmiennej globalnej z wartością 25

def scopeDef1():
	x1 = 50 # zdeklarowanie zmiennej lokalnej z wartością 50
			# mimo, że zmienna globalna x1 zdeklarowana poza funkcją oraz zmienna lokalna x1 zdeklarowana wewnątrz funkcji mają tą samą nazwę to są to dwie różne zmienne, w żaden sposób ze sobą nie związne.
			# Dlatego my nie nadpisujemy zmiennej globalnej w tej funkcji tylko tworzymy nową zmienną lokalną. Którą później zwracamy, a w konswkwencji wyświetlamy.
			## Błędne rozumowanie (nie kasuje):
			## Nadpisanie zmiennej globalnej nową wartością wartością: 50
			## zmiana jest tylko lokalna, wewnątrz funkcji, poza funkcją zmienna x1 będzie nadal miała starą wartość
			## można też to nazwać, że zmienna x1 w funkcji to inna zmienna niż x1 poza funkcją, mimo, że są tej samej nazwy.
	return x1

print(x1) # wyświetlenie wartości zmiennej globalnej x1
print(scopeDef1()) # wywołanie funkcji zwracającej wartość zmiennej lokalnej x1 zdefiniowanej wewnątrz funkcji.
				   ## Błędne rozumowanie (nie kasuje):
				   ## wywołanie funkcji spowoduje nadpisanie wartości zmiennej globalnej x1 na wartość z funkcji scopeDef1().
				   ## mimo, że zmienna x1 zdeklarowana została jako globalna na poczatku kodu to jej nadpisanie nową wartością wewnątrz funkcji jest traktowane lokalnie.
				   ## Zmiana tej wartości jest widziana tylko wewnątrz funkcji. No chyba, że byśmy przypisali wartość którą zwraca nasza funkcji spowrotem do zmiennej x1. Jednak odbywałoby się to już poza funkcją. Lub jeżeli na początku funkcji byśmy zastosowali zwrot "global x1"
print(x1) # wyświetlenie jeszcze raz zmiennej globalnej x1, jak widać jej wartość się nie zmieniła. Ponieważ zmienna x1 poza funkcją i zmienna x1 wewnątrz funkcji to dwie różne zmienne od siebie

# Powyższy przykład prezentuje ideę zakresu zmiennych.
# Idea zakres jest bardzo ważna dla odpowiedniego przypisywania i wywoływania zmiennych.

# TEORIA - BARDZO WAŻNE !!!
# Zmienna zdeklarowana wewnątrz funkcji nie jest w żaden sposób powiązana z innymi zmiennymi o tych samych nazwach
# zdeklarowanych i używanych poza tą funkcją. Nazwy zmiennych są lokalne dla funkcji. Nazywa się to właśnie zasięgiem zmiennej.
# Wszystkie zmienne mają zakres w bloku rozpoczynając od miejsca w którym są zdefiniowane ich nazwy.

# Pojęcie zakresu można opisać za pomocą trzech ogólnych zasad:

# 1. Przypisanie wartości do nazwy (zmiennej) domyślnie tworzy (nową zmienną) lub zmienia lokalnie wartość przypisaną do nazwy (już istniejącej zmiennej).
#    To znaczy, że nazwy (zmiennych) globalne i lokalne są ze sobą niezwiąznae. Nawet jeżeli nazwy (zmiennych) są takie same.

# 2. Wywołanie nazwy (zmiennej) powoduje przeszukanie i znalezienie wartości przypisanej do nazwy (zmiennej).
# 	 Zakres tego przeszukiwania ogranicza się do czterech zakresów:
# 	 - lokalnego,
# 	 - funkcji zagnieżdzonych, funkcji wewnątrz funkcji,
# 	 - globalnego,
# 	 - wbudowanego w różnych modułach, bibliotekach importowanych przez nas w kodzie.

# 3. Nazwy (zmiennych) zdeklarowane globalnie, nielokalnych, mapują (przyporządkowują)
# 	 przypisane im wartości na otaczające moduły i funkcje jeżeli w nich wystepują.

# Punkt drugi możemy zdefiniować poprzez regułę LEGB (LGBT :P):

#/////////////
#/////////////
# Reguła LEGB:

#/////////////
# L - local - lokalne - nazwy (zmiennych) zdefiniowane w dowolny sposób w ramach funkcji wielolinijkowej (def) lub jednolinijkowej (lambda)
#						i NIE zostały zdeklarowane jako GLOBAL.
#						Nawet jeżeli gdzieś w kodzie występuje nazwa (zmiennej) która jest taka sama jak wewnątrz funkcji to są to dwie różne zmienne.

# Przykład 1:
print("#####")
f = lambda x: x**2 # nazwa (zmiennej) x jest lokalna, używana tylko wewnątrz lambdy
print(f(2))

# Przykład 2:
print("#####")
def exampleLocal(localVariable):
	return localVariable**2 # nazwa (zmiennej) localVariable jest lokalna, ponieważ jest używana tylko wewnątrz funkcji exampleLocal()
print(exampleLocal(2))

# Przykład 3:
print("#####")
x = 50 # zdefiniowanie zmiennej globalnej, w głównym bloku kodu
def scopeDef2(x):
    print('Globalne x = {txt}'.format(txt=x)) # wyświetlenie wartość zmiennej x która została zdefiniowana globalnie, czyli w glównym bloku kodu.
    x = 2 # zdefiniowanie zmiennej lokalnej, wewnątrz funkcji
		  # przypisanie wartości 2 nie zmieni wartość zmiennej x zdefiniowanej globalnie
    print('Lokalne x = {txt}'.format(txt=x)) # wyświetlenie wartości zmiennej x która została zdefiniowana lokalnie
scopeDef2(x)
print('Globalne x, poza funkcja, nadal ma wartosc = {txt}'.format(txt=x)) # wywołanie zmiennej x poza funkcją spowoduje wyświetlenie wartość x zdefiniowanej w
															# głównym bloku kodu. Potwierdza to tym samym, że zmienne zdefiniowane globalnie nie mają wpływu na zmienne lokalne i na odwrót.


#/////////////
# E - enclosing function locals - obejmujące funkcje zagnieżdżone w funckji - nazwy (zmiennych) zdefiniowane wewnątrz funkcji (najbardziej zewnętrznej)
#																			  są widoczne dla funkcji zdefinowanej wewnątrz tej samej funkcji co nazwa (zmiennej),
#																			  dotyczy to funkcji zagnieżdżonych (funkcji wewnątrz funkcji)

# Przykład:
print("#####")
name = 'To jest globalna nazwa' # nazwa (zmiennej) name w tym miejscu jest zdefiniowana jako globalna
def exampleEncloxing1():
	name = 'Tomek' # nazwa (zmiennej) name jest zdefiniowana w tym miejscu jako lokalna dla funkcji exampleEncloxing1()
	def exampleEncloxing2():
		print('Czesc ' + name) # zmienna name jest dostępna dla funkcji exampleEncloxing2() ponieważ funkcja ta jest zdefiniowana wewnątrz funkcji exampleEncloxing1()
	exampleEncloxing2()
exampleEncloxing1()

#/////////////
# G - global - globalne - nazwy (zmiennych) zdefiniowane na najwyższym poziomie:
#						  na samym poczatku naszego pliku,
#						  na samym początku importowanego modułu,
#						  bądź zdeklarowane jako GLOBAL na początku funkcji wielolinijkowej.
#						  A jeżeli wewnątrz funkcji zdefiniowaliśmy nazwę (zmienne) bez GLOBAL wówczas jest to zmienna lokalna widoczna tylko i wyłącznie wewnątrz funkcji i mimo, że jak będzie mieć taką samą nazwę jak jakaś nazwa (zmiennej) globalnej to są to dwie różne nazwy (zmiennych).

# Przykład 1:
print("#####")
print(name) # nazwa (zmiennej) zdefiniowana w poprzednim przykładzie poza jakąkolwiek funkcją. Jest ona zdefiniowana jako globalna. I mimo, że w funkcji zdefiniowaliśmy zmienną lokalną o tej samej nazwie co globalna, czyli name, to są to dwie rózne zmienne.

# Wyrażenie GLOBAL
# Do tej pory zmienna zdefiniowana na najwyższym poziomie (poza funkcjami lub klasami), czyli w głównym bloku kodu
# i zmienna lokalna o takiej samej nazwie zdefiniowana wewnątrz funkcji to dwie różne zmienne.
# Zmiana wartości jednej nie ma wpływu na drugą.
# Jednak w takim wypadku (gdzie zmienna globalna i lokanla mają take same nazwy) możemy w je ze sobą "scalić".
# Czyli jeżeli chcemy używać wewnątrz funkcji zmiennej zdefiniowanej globalnie (w głównym bloku kodu, poza funkcją)
# to musimy w definicji funkcji, na samym jej początku, użyć wyrażenia "global nazwa_zmiennej". Polecenie to mówi Pythonowi,
# że nazwa zmiennej używana wewnątrz funkcji nie jest lokalna, ale globalna. Wówczas każda operacja na zmiennej wewnątrz funkcji
# będzie trwała i widoczna poza funkcją. Nie jest możliwe "scalenie" zmiennych globalnej i lokalnej bez wyrażenia "global".

# Przykład 2:
print("#####")
x2 = 50 # zdefiniowanie zmiennej globalnej, w głównym bloku kodu
def scopeDef3():
    global x2 # zdefiniowanie wewnątrz funkcji zmiennej x2 jako zmiennej odwołującej się do zmiennej globalnej, czyli zdefiniowanej poza funkcją
    print('Ta funkcja uzywa zmiennej x2 zdefiniowanej wewnetrznie jako globalnej')
    x2 = 2 # nadpisanie zmiennej x2 nową wartością,
		   # ponieważ x2 nie jest już zmienną lokalną przez użycie wyrażenia "global" na początku funkcji
		   # więc przypisanie wartości 2 do zmiennej x2 spowoduje, że poza funkcją zmienna x2 będzie miała nową wartość.
    print('Zmiana wewnatrz funkcji zmiennej x2 na wartosc = {x}'.format(x=x2)) # wyświetlenie aktualnej wartości zmiennej x2

print('Przed wywolaniem funkcji scopeDef3() zdefiniowana globalnie zmienna x2 = {x}'.format(x=x2)) # wyświetlenie aktualnej wartści zmiennej x2 jeszcze przed wywołaniem funkcji scopeDef3()
scopeDef3() # wywołanie funkcji z wyrażeniem GLOBAL dla zmiennej x2, czyli zmienna ta nie będzie już zmienną lokalną funkcji
print('Zmienna x2 poza funkcja ma nowa wartosc = {x}'.format(x=x2)) # wyświetlenie aktualnej wartści zmiennej x2 już po wywołaniu funkcji scopeDef3()
																	# w której to zmieniliśmy globalnie wartość zmiennej x2 dzięki temu, że na początku funkcji użyliśmy wyrażenia GLOBAL dla zmiennej x2.
																	# pozwoliło to traktować tą zmienną jako zmienną globalną wewnątrz funkcji.

# Wyrażenie "global" służy do deklarowania, że zmienna używana wewnątrz funkcji jest zmienną zdefiniowaną poza nią i powoduje to, że zmiana zmiennej wewnątrz funkcji będzie widoczna jeżeli tą zmienną użyjemy poza funkcją.
# Możemy deklarować dowolną ilość zmiennych globalnych wewnątrz funkcji.
# Wyrażenie "global" jednocześnie informuje osobę czytającą kod, że zmienna ta może być zmieniana wewnątrz funkcji i zmiany te będą widoczne na zewnątrz funkcji.

#/////////////
# B - Bulit-in - wbudowane - nazwy (zmiennych) wbudowane w Pythona i moduły, biblioteki zewnętrznie importowane,
#							 takie nazwy jak: open, range, dict, list, SyntaxError itd.
#							 Wówczas nie możemy stosować naszych nazw (zmiennych) będące takie same jak nazwy już wbudowane.

# Przykład:
print("#####")
print(len(name)) # słówko len oznacza nazwę wbudowanej metody Pythona do zwracania długości kolekcji elementów (lista, string, słownik)
#				   NIE MOŻNA stosować własnych nazw (zmiennych) nazwami modułów Pythona.
