#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/////////////////
#/////////////////
# Programowanie obiektowe

# W tym rozdziale koncentrujemy się na Programowaniu Obiektowtym w Pythonie.

# Istnieje bardzo dużo kursów, samouczków obejmujących lekcje programowania obiektowego.
# Na końcu tego pliku będzie podlinkowanych kilka z nich.
# Z uwagi na mnogość wspomnianych kursów skupimy się na nastepujących najwazniejszych kwestiach programowania obiektowego w Pythonie:

# 1. Obiekty
# 2. Słowo kluczowe "class"
# 3. Atrybuty klas
# 4. Metody klas
# 5. Dziedziczenie
# 6. Metody specjalne klas

# Zaczynając naukę programowania obiektowego na początku przypomnijmy sobie podstawy obiektów w Pythonie
# Przykład 1:
listaObiekt = [1,2,2,3,3,3,3,3]
print(listaObiekt.count(3))
# W Pythonie wszystko co wykonujemy, tworzymy, np. zmienną, to jest ona obiektem.
# W zależności od tego jaka to jest zminna to taki przyjmuje ona rodzaj obiektu.
# Mamy zmienną całkowitą i zmiennoprzecinkową. I jednym z tych obiektów będzie ewentualna zmienna.
# I tak samo to działa w każdym innym przypadku.
# W powyższym przykładzie tworzymy obiekt o nazwie "listaObiekt". Jest to obiekt klasy
# lista, kolekcja elementów. Python wie, że tworzymy listę ponieważ obiekt klasy lista
# tworzony jest z użyciem nawiasów kwadratowych "[]". Definicja klasy lista
# tak została przygotowana, że wymagane jest użycie tych nawiasów aby go stworzyć.
# Następnie w przykładzie mamy wykorzystanie metody ".count()" za pomocą której
# zliczamy wystąpnienia cyfry 3. Tak została przygotowana klasa lista,
# że zawiera metodę zliczającą wystopnienia konkretnego jej elementu.
# Po prostu ta metoda została zawarta w definicji klasy wraz z jej nazwą.
# Na tym właśnie polega programowanie obiektowe.
# Tworzymy w miarę uniwersalną definicję klasy by móc tworzyć podobne obiekty
# wykorzystując jedną defiunicję.

#/////////////////
#/////////////////
# Obiekty

# Jak już było wspomniane w Pythonie wszystko jest obiektem.
# Poniżej wykorzystując polecenie type() sprawdzimy obiektami jakiej klasy są poszczególe obiekty.

print(type(1))
print(type("test"))
print(type([]))
print(type(()))
print(type({}))

# Skoro wszystko jest obiektem to my też możemy stworzyć klasę do której będą należały
# obiekty które później będziemy tworzyć.
# Wynika to z tego, że każdy obiekt jest jakieś klasy. I tak de facto towrzymy definicję jakieś klasy
# to wywołując tą klasę tworzymy obiekt tej klasy.

#/////////////////
#/////////////////
# Class

# W Pythonie obiekty definiujemy poprzez klasy, które można uznać za sposób łączenia
# i dzielenia obiektów w ramach grup.
# Tworząc własny obiekt musimy najpierw zdefiniować klasę do której będzie on należał.
# Definicję nowej klasy zaczynamy od słówka "class" a nastepnie podajemy nazwę klasy.
# Klasa jest takim szablonem który definiuje charakter naszego obiektu.
# Klasa pozwala nam stworzyć instancję, która jest obiektem danej klasy.
# W naszym pierwszym przykładzie obiekt "listaObiekt" jest instancją klasy lista.

# Tworznie nowego obiektu:
class Przyklad(): # definicja klasy o nazwie "Przyklad". Od tego momentu możemy już tworzyć obiekty typu Zawierze.
				  # Zgodnie z konwencją nazwy klas zaczynają się wielką literą.
	pass # ciało klasy Przyklad.

przyklad1 = Przyklad() # utworznie obiektu przyklad1, który jest instancją klasy Przyklad.
					   # Podobnie jak w przypadku funkcji, po nazwie klasy umieszczamy nawiasy otwarte.
print(type(przyklad1)) # sprawdzenie typu obiektu

# Obiekt przyklad1 jest teraz odwołaniem się do nowej instancji klasy Przyklad.
# Innymi słowy tworzy instancję klasy Przyklad.
# Aktualnie nasza klasa nie zawiera niczego w definicji.
# Dlatego taka klasa a tym samym obiekt takiej klasy będzie bezużyteczny.
# Aby klasa była bardziej użyteczna możemy zdefiniować jej następujące cechy:
# a) atrybuty, właściwości (inaczej mówiąc parametry, argumenty obiektu ustalane w trakcie tworzenia obiektu,
# 	 tak jak argumenty przekazywane do zwykłej funkcji)
# b) metody (to inaczej mówiąc funkcje zawarte w klasie, operacje wykonywane z atrybutami, właściwościami obiektu)

#/////////////////
#/////////////////
# Atrybuty, właściwości

# Czasami podczas tworzenia obiektu chcemy ustawić pewne wartości (zwane atrybutami, właściwościami)
# już na początku, które będziemy używać w przyszłości do operacji na nich. inicjalizując obiekt,
# przygotowujemy go do użycia. Jeżeli chcemy aby obiekty podczas tworzenia, czyli w trakcie ich
# inicjalizowania, zawierały okreslone przez użytkownika atrybuty, właściwości danego obiektu to
# musimy stworzyć funkcję:
# def __init__(self, atrybut1, atrybut2...)
# Jest to specjalna funkcja i musi mieć taką właśnie nazwę. I zawsze być pierwszą funkcją w klasie.
# Funkcja, metoda __init__ pozwala ustawić właściwości obiektu w momencie jego tworzenia.
# I będą one dotyczyły tylko tego jednego konkretnego obiektu.
# Jest ona wywoływana automatycznie w momencie tworzenia obiektu.
# Pierwszym atrybutem w tej metodzie zawsze musi być atrybut self. Jest to odwołanie się do instancji obiektu.
# W celu zdefiniowania w metodzie init jakieś właściwości, zmiennej obiektowej stosujemy poniższą składnie:
# self.object_variable1= atrybut1
# self.object_variable2 = atrybut2
# Powyższą składnię możemy odczytac nastepująco: wartość parametru atrybut1 zapisz
# do późniejszego użytku w zmiennej obiektowej "self.object_variable1".
# Parametr self w każdej zmiennej obiektowej umożliwia dostęp do tej zmiennej w ramach całej klasy obiektu. Jednocześnie pozwala
# funkcji w klasie wywołać inną funkcję.
# Po stworzeniu obiektów z atrybutami mamy do nich dostęp za pomocą operatora kropkowego i nazwy zmiennej obiektowej.
# Odwołanie się do zmiennej obiektowej następuje bez nawiasu otwartego ponieważ to jest atrybut i nie przyjmuje żadnych argumentów.
# Obiekty tej samej klasy zawierają indywidualne wartości atrybutów. Każdy obiekt tej samej klasy może mieć różne wartości atrybutów.
# W Pytonie w programowaniu obiektowym istnieją też atrybuty stale przypisane do każdej instancji obiektu.
# Nazywa się je zmiennymi klasowymi. Ich wartość będzie taka sama dla każdej instancji klasy czyli dla każdego obiektu danej klasy.
# Deklaruje się je zawsze na początku definicji klasy przed funkcją init. Normalnie tak jabyśmy deklarowali zmienną:
# class_variable1 = wartosc1
# Mamy dwie możliwości zmiany wartości zmiennej klasowej:
# - wywołując ja z nazwy obiektu. Wówczas jak zmienimy jej wartość to obiekt ten zachowa nową wartość. I wartość ta będzie indywidualna tylko dla tego obiektu. Nawet jeżlei zmienimy wartość zmiennej globalnej poprzez wywołanie jej z nazwy klasy.
# - jeżeli wywołamy ją z nazwy klasy. Wówczas jak zmienimy jej wartość to każdy obecny oraz przyszły obiekt będzie mieć nową wartość. Chyba, że indywidualnie dla obiektu zmienimy jej wartość. Wówczas ten jeden obiekt będzie miał inną wartość

# Przykład 2:
# Stworzymy klasę Pies której, zmienną klasową będzi gatunek a atrybutami będze jego imię oraz głos, .

class Pies():
	gatunek = "pies domowy" # deklaracja zmiennej klasowej.
	def __init__(self, imie, glos):
		self.imie_psa = imie # przekazanie parametru imie do zmiennej obiektowej self.imie_psa, deklaracja zmiennej obiektowej
		self.glos_psa = glos # przekazanie parametru glos do zmiennej obiektowej self.glos_psa, deklaracja zmiennej obiektowej

tina = Pies("Tina", "Hauhau") # stworznie instancji o nazwie tina obiektu Pies
rambo = Pies("Rambo", "Wrrrr") # stworznie instancji o nazwie rambo obiektu Pies

print(tina.imie_psa) # odwołanie do zmiennej obiektowej imie_psa obiektu tina, nie używamy self jeżeli chcemy się odwołać do zmiennj obiektowej używając operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(rambo.glos_psa) # odwołanie do zmiennej obiektowej glos_psa obiektu rambo, nie używamy self jeżeli chcemy się odwołać do zmiennj obiektowej używając operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
tina.imie_psa = "Kapiszon" # zmiana wartości zmiennej obiektowej imie_psa obiektu tina
print(tina.imie_psa) # odwołanie do zmiennej obiektowej imie_psa obiektu tina po zmianie jej wartości


print(Pies.gatunek) # odwołanie do zmiennej klasowej gatunek poprzez wywołanie jej z nazwy klasy, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(tina.gatunek) # odwołanie do zmiennej klasowej gatunek poprzez wywołanie jej z obiektu tina, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
tina.gatunek = "kundel" # zmiana wartości zmiennej klasowej gatunek obiektu tina, nowa wartość zmiennej klasowej będzie dotyczyć tylko obiektu tina
print(tina.gatunek) # odwołanie do zmiennej klasowej gatunek obiektu tina po zmianie jej wartości indywidualnie tylko dla obiektu tina
print(Pies.gatunek) # odwołanie do zmiennej klasowej gatunek wywołanej z nazwy klasy Pies, będzie ta sama co przy definicji klasy na początku, ponieważ indywidualnie zmienilismy jej wartość tylko dla obiektu tina.
Pies.gatunek = "domowiec" # zmiana wartości zmiennej klasowej gatunek całej klasy Pies, wartość zmiennej klasowej będzie dotyczyć każdego obiektu tej klasy, nowego jak i obecnego, ALE oprócz obiektu tina ponieważ dla tego obiektu zmieniliśmy tą zmienną indywidualnie
print(rambo.gatunek) # odwołanie do zmiennej klasowej gatunek obiektu rambo po zmienie jej wartości dla całej klasy, będzie inna w stosunku do tego co definiowalimsy dla klasy, i zmieniła się ponieważ zmienialismy tą zmienną dla całej klasy
print(tina.gatunek) # odwołanie do zmiennej klasowej gatunek obiektu tina po zmianie jej wartości dla całej klasy, ALE dla tego obiektu nie została ona zmieniona bo wcześniej zmieniliśmy ja indywidualnie dla tego obiektu
