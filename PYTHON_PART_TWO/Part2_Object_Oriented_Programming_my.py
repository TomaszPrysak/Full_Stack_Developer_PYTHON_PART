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

# W większości podczas tworzenia obiektu chcemy ustawić pewne wartości (zwane atrybutami, właściwościami)
# już na początku, które będziemy używać w przyszłości do operacji na nich.
# Inicjalizując obiekt przygotowujemy go do użycia. Jeżeli chcemy aby obiekty podczas tworzenia, czyli w trakcie ich
# inicjalizowania, zawierały okreslone przez użytkownika atrybuty, właściwości to
# musimy stworzyć funkcję:
# def __init__(self, atrybut1, atrybut2...)
# Jest to specjalna funkcja i musi mieć taką właśnie nazwę. I zawsze być pierwszą funkcją w klasie.
# Funkcja, metoda __init__ pozwala ustawić właściwości obiektu w momencie jego tworzenia.
# I będą one dotyczyły tylko tego jednego konkretnego obiektu, tej konkretnej instancji klasy.
# Jest ona wywoływana automatycznie w momencie tworzenia obiektu.
# Pierwszym atrybutem w tej metodzie zawsze musi być atrybut self. Jest to odwołanie się do tej aktualnej instancji obiektu. Czyli obiekt owdołuje się sam do siebie.
# W celu zdefiniowania w metodzie init jakieś właściwości, zmiennej obiektowej stosujemy poniższą składnie:
# self.object_variable1= atrybut1
# self.object_variable2 = atrybut2
# Powyższą składnię możemy odczytac nastepująco: wartość parametru atrybut1 zapisz do późniejszego użytku w zmiennej obiektowej "self.object_variable1".
# Parametr self w każdej zmiennej obiektowej umożliwia dostęp do tej zmiennej w ramach całej klasy.
# UWAGA!!! Jeżeli zdefiniujemy naszą metodę init z kilkoma argumentami to podczas tworzenia nowej instancji naszej klasy (tzn. nowego obiektu tej klasy) musimy podać wartości wszystkich argumentów.
#		   Jeżeli tego nie zrobimy to wystąpi błąd. Aby zabezpieczyć się przed możliwym brakiem wartości argumentów podanych przez użytkownika podczas tworzenia obiektu musimy w definicji metody init przypisać argumentom domyślne wartości.
# Jak będziemy chcieli użyć tej zmiennej w jakieś metodzie wewnątrz ciała klasy to również uzywamy self przed nazwą zmiennej.
# Dotyczy to dokładnie tego samego jak chcemy wywołać jakąś zmienną lub metodę na jakimś obiekcie, już poza klasą. To na jego nazwie po kropce wpisujemy nazwę tej zmiennej lub metody.
# W przypadku tworzenia klasy każdą zmienną i funkcję w definicji klasy rozpoczynamy od słówka self i po kropce piszemy nazwę zmiennej bądź funkcji.
# W przypadku definicji klasy słówko self oznacza, że odnosimy się do zmiennej lub funkcji tylko wewnątrz definicji klasy.
# Jednocześnie pozwala funkcji w klasie wywołać inną funkcję.
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
# Bardzo ważne, jeżeli chcemy użyć zmiennej klasowej wewnątrz ciała klasy, na przykład w jakiejś metodzie wówczas musimy odnieść się do niej ze słówkiem self, tak jak to ma miejsce w zmiennej obiektowej. Jeste też możliwość odniesienia się do tej zmiennej poprzez nazwę klasy i po kropce nazwę zmiennej.

# Przykład 2:
# Stworzymy klasę Pies której, zmienną klasową będzi gatunek a atrybutami będze jego imię oraz głos.
# Klasa ta będzie stworzona w sposób Pythonowski, tzn nie będzie hermetyzować zmiennych obiektowych.
# Będzie możliwy dostęp do zmiennych poprzez wywołanie ich w notacji kropkowej poza klasą.

class Pies():
	gatunek = "pies domowy" # deklaracja zmiennej klasowej, będzie taka sama dla każdej instancji tej klasy, czyli dla każdego obiektu tej klasy (chyba, że indywidualnie później nadpiszemy tą zmienną)
	def __init__(self, imie, glos): # funkcja wywoływana podczas inicjalizacji obiektu ustawiająca zmiennej obiektowe
		self.imie = imie # przekazanie parametru imie do zmiennej obiektowej self.imie, deklaracja zmiennej obiektowej
		self.glos = glos # przekazanie parametru glos do zmiennej obiektowej self.glos, deklaracja zmiennej obiektowej

tina = Pies("Tina", "Hauhau") # stworznie instancji o nazwie tina obiektu Pies
rambo = Pies("Rambo", "Wrrrr") # stworznie instancji o nazwie rambo obiektu Pies

print(tina.imie) # odwołanie do zmiennej obiektowej imie obiektu tina, jeżeli chcemy się odwołać do zmiennj obiektowej używamy operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(rambo.glos) # odwołanie do zmiennej obiektowej glos obiektu rambo, jeżeli chcemy się odwołać do zmiennj obiektowej używamy operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
tina.imie = "Kapiszon" # zmiana wartości zmiennej obiektowej imie obiektu tina
print(tina.imie) # odwołanie do zmiennej obiektowej imie obiektu tina po zmianie jej wartości

print(Pies.gatunek) # odwołanie do zmiennej klasowej gatunek poprzez wywołanie jej z nazwy klasy, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(tina.gatunek) # odwołanie do zmiennej klasowej gatunek poprzez wywołanie jej z obiektu tina, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
tina.gatunek = "kundel" # zmiana wartości zmiennej klasowej gatunek obiektu tina, nowa wartość zmiennej klasowej będzie dotyczyć tylko obiektu tina
print(tina.gatunek) # odwołanie do zmiennej klasowej gatunek obiektu tina po zmianie jej wartości indywidualnie tylko dla obiektu tina
print(Pies.gatunek) # odwołanie do zmiennej klasowej gatunek wywołanej z nazwy klasy Pies, będzie ta sama co przy definicji klasy na początku, ponieważ indywidualnie zmienilismy jej wartość tylko dla obiektu tina.
Pies.gatunek = "domowiec" # zmiana wartości zmiennej klasowej gatunek całej klasy Pies, wartość zmiennej klasowej będzie dotyczyć każdego obiektu tej klasy, nowego jak i obecnego, ALE oprócz obiektu tina ponieważ dla tego obiektu zmieniliśmy tą zmienną indywidualnie
print(rambo.gatunek) # odwołanie do zmiennej klasowej gatunek obiektu rambo po zmienie jej wartości dla całej klasy, będzie inna w stosunku do tego co definiowalimsy dla klasy, i zmieniła się ponieważ zmienialismy tą zmienną dla całej klasy
print(tina.gatunek) # odwołanie do zmiennej klasowej gatunek obiektu tina po zmianie jej wartości dla całej klasy, ALE dla tego obiektu nie została ona zmieniona bo wcześniej zmieniliśmy ja indywidualnie dla tego obiektu

#/////////////////
#/////////////////
# Metody

# W poprzednim rozdziale omówione było definiowanie atrybutów, właściwości w klasie.
# W tym rozdziale będą omawiane funkcje zdefiniowane wewnątrz ciała klasy. Takie funkcje nazywamy metodami.
# Metody opisuję cechy klasy, które są wspólne dla każdej instancji klasy. Metody definiują możliwości obiektów należących do tej samej klasy lub do klasy nadrzędnej.
# Metody pozwalają na wykonywanie operacji z atrybutami obiektów. Wartości atrybutów będą różne dla różnych obiektów, jednak operacje będą takie same dla każdego obiektu (instancji klasy)
# Ponieważ atrybuty obiektów są przypisywane zawsze na początku tworzenia obiektu w specjalnej metodzie init, dlatego pozostałe metody muszą być zdefiniowane po tej specjalnej metodzie init.
# Tak jak zwykła funkcja tak samo metoda zdefiniowana w ciele klasy może zawierać argumenty jak i nie musi, przykład zdefiniowania metody:
# def __init__(self, a1, a2):
# 	self.a1 = a1
#	self.a2 = a2
# def example_method1(self):
#	return self.a1 * self.a2
# def example_method2(self, a):
# 	return self.a1 / a
# Tak jak w przypadku metody specjalnej init zawsze pierwszym argumentem metody musi być self. Jest to odwołanie się do tej aktualnej instancji obiektu. Czyli obiekt owdołuje się sam do siebie.
# Przy czym jeżeli po self nie podamy w definicji metody innych argumentów to metoda jest bezargumentowa. self jest konieczne z uwagi na sposób tworzenia metod w klsach.
# Jednocześnie parametr slef pozwala na to, aby jedna metoda w klasie mogła wywoływać inną metodę z tej klasy lub z klasy nadrzędnej, czyli z klasy z której dziedziczy.
# W powyższym przykładzie zdefiniowano dwie metody w klasie funckji, jedna bez argumentów która zwraca iloczyn dwóch atrybutów obiektu, czyli dwóch zmiennych obiektowych self.a1 i self.a2.
# Natomiast druga metoda przyjmuje jeden argument który należy podać w nawiasie podczas wywoływania tej metody na obiekcie i zwraca ona iloraz jednego atrybutu self.a1 i argumentu przekazywanego do metody.
# Metody działają tylko w obszarze obiektu i tylko z jego atrybutami mogą dokonywać działań. Poza obiektem nie mogą być wywołane.
# Wywoływanie metod zdefiniowanych w klasie odbywa się, tak jak wywoływanie zmiennych obiektowych lub klasowych czyli poprzez nazwę obiektu i notację kropkową.
# Różnica polega na tym, że wywołując jakąś zmienną obiektową czy klasową po kropce i nazwie tej zmiennej NIE stosujemy nawiasów otwartych.
# W przypadku wywoływania metod na obiektach musimy otworzyć i zamknąć nawias otwary. A czasami jeżeli metoda ta przyjmuje jakieś argumenty to w nawiasie podać wartość którą chcmey jej przekazać.
# Musimy stosować nawias nawet bez podawania argumetu w nim ponieważ tak działa wywolywanie funkcji w Pythonie. Funkcja może, ale nie musi posiadać argumenty, dlatego Python wymusza stosowanie nawiasów.
# Jednocześnie dzięki temu jesteśmy w stanie odróżnić wywołanie na obiekcie zmiennej od wywołania na obiekcie metody. Wywołanie zmiennej nie będzie zakończone nawiasami a metody tak.

# Przykład 3:
# Stworzymy klasę Kolo której zmienną klasową będzi wartość PI a atrybutem promień.
# Klasa będzie zawierać metodę do zwracania powierzchni koła na podstawie jego promienia.

class Kolo():
	pi = 3.14
	def __init__(self, radius = 1):
		self.radius = radius
	def area(self): # definicja metody area bez argumentów. Metoda opiera się na zmiennej klasowej oraz obiektowej. Z ich iloczyny zwraca pole powierzchni aktualnej instancji obiektu, czyli pole kola
		return Kolo.pi * self.radius * self.radius # iloczyn zmiennej klasowej pi oraz zmiennej obiektowej self.radius
												   # odwołanie się do zmiennych obiektowych self.radius nastepuje z uzyciem sels, ponieważ odwołujemy się do zmiennej aktualnej instacji obiektu na którym ją wywołujemy,
												   # natomiast odwołanie do zmiennej klasowej nastepuję poprzez nazwę klasy natacji kropkowej z nazwą zmiennej, można też self przed nazwą zmiennej klasowej zamiast nazwy klasy, ale dzięki temu rozróżniamy zmienne klasowe i obiektowe.

kolo1 = Kolo(2) # stworznie instancji o nazwie kolo1 obiektu Kolo
print(kolo1.radius) # odwołanie do zmiennej obiektowej radius obiektu kolo1, jeżeli chcemy się odwołać do zmiennj obiektowej używamy operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(kolo1.area()) # wywołanie metody bezargumentowej area na obiekcie kolo1, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
kolo2 = Kolo(5) # stworznie instancji o nazwie kolo2 obiektu Kolo
print(kolo2.radius) # odwołanie do zmiennej obiektowej radius obiektu kolo2, jeżeli chcemy się odwołać do zmiennj obiektowej używamy operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(kolo2.area()) # wywołanie metody bezargumentowej area na obiekcie kolo2, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów

# W powyższym przykładzie, zdefiniowaliśmy klasę z metodą bezargumentową.
# Kolejny przykład będzie zawierał metody z argumentami, które musimy podać w momencie ich wywoływania.
# Przykład ten zostanie powiązany z omówieniem programowania opartego o hermetyzację (enkapsulację), wówczas metody są niezbęde.
# Należy zaznaczyć, że programowanie hermetyczne nie jest typowym programowaniem Pythonowskim. Ponieważ z założenia Python nie ukrywa danych, nie implementuje żadnych metod hermetyzacji.
# Definiując klasy a w nich zmienne obiektowe oraz zmienne klasowe, z założenia mamy dostęp do zmiennych poprzez notację kropkową.
# W każdej chwili możemy wywołać taką zmienną i zmienic jej wartość. Nie potrzebujemy zatem definiować w klasie metod zwracającyh wartość danej zmiennej obiektowej (oraz zmiennej klasowej) czy metod do zmiancyh ich wartości. Po prostu wszystko wywołujemy je poprzez notacje kropkową i nazwę zmiennej.
# Programowanie hermetyczne w Pythonie należy niejako wymusić poprzez stosowanie prywatnych atrybutów, właściwości oraz metod typu "getters" oraz "setters". Tak jak to robimy w programowaniu obiektowym w Javie.
# Prywatne atrybuty:
# W nazwie takiego atrybutu (zmiennej) na początku powinny się znaleźć dwa podkreślniki "__", np.:
# "__variable"
# Taka zmienna może być zdefiniowana na początku klasy lub w metodzie init.
# Dwa podkreślniki spowodują, że zmienna NIE będzie dostępna w notacji kropkowej, np.:
# "ClassName.__variable" czy "ClassName.__variable = newValue"
# Powyższe odwołania nie będą już możliwe.
# W momencie jak stosujemy prywatne atrybuty to musimy w definicji klasy zdefiniować metdy zwracające wartości oraz metody zmieniające/ustawiające wartości prywatnych atrybutów (zmiennych).
# Najczęściej takie metody nazywamy:
# - "getters", np.: "get_variable" metody zwracające wartości prywatnych atrybutów (zmiennych)
# - "setters", np.: "set_variable" metody zmieniające/ustawiające wartości prywatnych atrybutów (zmiennych)
# W przypadku metod typu "setters" aby zmienić wartość zmiennej obiektowej lub klasowej musimy metodę tę stworzyć z argumentem, który będzieny przekazywać do metody. A we wnętrzy tej metody będziemy zmieniać wartość zmiennej obiektowej bądź klasowej.

# Przykład 4:
# Bliźniacza klasa do klasy Pies, jednak przedstawiająca sposób definicji klasy z hermetyzacją zmiennych obiektowych oraz metod z argumentami.

class Pies_hermetyzajca():
	__gatunek = "pies domowy" # deklaracja zmiennej klasowej jako zmiennej prywatnej (prywatnego atrybutu), wówczas do zwrócenia jej wartości potrzebna będzie specjalna metoda typu "getter"
	def __init__(self, imie="Brak", glos="Brak"): # funkcja wywoływana podczas inicjalizacji obiektu ustawiająca zmiennej obiektowe, jeżeli podczas inicjalizacji obiektu nie zostaną podane argumenty wówczas ich wartości będą domyślne imie="Brak", glos="Brak"
		self.__imie = imie # przekazanie parametru imie do prywatnej zmiennej obiektowej self.__imie, deklaracja prywatnej zmiennej obiektowej (prywatnego atrybutu), wówczas do zwrócenia jej wartości oraz do ustawienia nowej warości będą potrzebne metody typu "getter" oraz "setter"
		self.__glos = glos # przekazanie parametru glos do prywatnej zmiennej obiektowej self.__glos, deklaracja prywatnej zmiennej obiektowej (prywatnego atrybutu), wówczas do zwrócenia jej wartości oraz do ustawienia nowej warości będą potrzebne metody typu "getter" oraz "setter"
	def get_gatunek(self): # definicja metody get_gatunek bez argumentów. Metoda opiera się na prywatnej zmiennej klasowej (prywatnym argumencie) Pies_hermetyzajca.__gatunek
		return Pies_hermetyzajca.__gatunek # Metoda zwraca wartość prywatnej zmiennej klasowej Pies_hermetyzajca.__gatunek, do prywantej zmiennej klasowej dostajemy się poprzez nazwę klasy i po kropce nazwy zmiennej, nie kończy się nawiasami ponieważ to atrybut a nie metoda, atrybuty nie przyjmują argumentów
	def get_imie(self): # definicja metody get_imie bez argumentów. Metoda opiera się na prywatnej zmiennej obiektowej (prywatnym argumencie) self.__imie
		return self.__imie # metoda zwraca wartość prywatnej zmiennej obiektowej self.__imie, do prywatnej zmiennej obiektowej dostajemy się słówko self i po kropce nazwy zmiennej, nie kończy się nawiasami ponieważ to atrybut a nie metoda, atrybuty nie przyjmują argumentów
	def set_imie(self, imie): # definicja metody set_imie przyjmująca jeden argument. Metoda opiera się na prywantej zmiennej obiektowej (prywatnym argumencie) self.__imie. Wartość argumentu przekazujemy do metody w momencie wywoływania tej metody z instancji obiektu
		self.__imie = imie # argument metody imie przekazujemy do prywatnej zmiennej obiektowej self.__imie, innymi słowy mówiąc nadpisujemy prywatną zmienną obiektową nową wartością którą przekazaliśmy do metody w postaci argumentu tej metody imie
	def get_glos(self): # definicja metody get_glos bez argumentów. Metoda opiera się na prywatnej zmiennej obiektowej (prywatnym argumencie) self.__glos
		return self.__glos # metoda zwraca wartość prywatnej zmiennej obiektowej self.__glos, do prywatnej zmiennej obiektowej dostajemy się słówko self i po kropce nazwy zmiennej, nie kończy się nawiasami ponieważ to atrybut a nie metoda, atrybuty nie przyjmują argumentów
	def set_glos(self, glos):  # definicja metody set_glos przyjmująca jeden argument. Metoda opiera się na prywantej zmiennej obiektowej (prywatnym argumencie) self.__glos. Wartość argumentu przekazujemy do metody w momencie wywoływania tej metody z instancji obiektu.
		self.__glos = glos # argument metody glos przekazujemy do prywatnej zmiennej obiektowej self.__glos, innymi słowy mówiąc nadpisujemy prywatną zmienną obiektową nową wartością którą przekazaliśmy do metody w postaci argumentu tej metody glos

puszek = Pies_hermetyzajca() # stworznie instancji o nazwie puszek obiektu Pies_hermetyzajca
# print(puszek.__imie) # odwołanie do zmiennej zmiennej obiektowej __imie. Jednak wystąpi błąd ponieważ jest to zmienna prywatna. Klasa została napisana o hermetyzajcę. Do zwrócenia wartości zmiennej potrzebna jest  metoda typu "getter"
print(puszek.get_imie()) # wywołanie metody bezargumentowej typu "getter" get_imie która zwraca wartość prywantej zmiennej obiektowej self.__imie, w tym wypadku zwróci wartość "Brak", ponieważ, obiekt został stworzony bez podania wartości wymaganych atrybutów, a więc zostąły im przypisane wartości domyślne
puszek.set_imie("Lucky Luke") # wywołanie metdy argumentowej typu "setter" set_imie, w argumencie metody przekazujemy wartość jaką chcemy przypisać prywantej zmiennej obiektowej self.__imie. W ten sposób zmieniamy wartość tej zmiennej, poprzez dodatkową metodę typu "setter". Musimy tak zrobić ponieważ klasa została napisana w sposób hermetyczny
print(puszek.get_imie()) # wywołanie metody bezargumentowej typu "getter" get_imie która zwraca wartość prywantej zmiennej obiektowej self.__imie, w tym wypadku zwróci wartość "Lucky Luke" ponieważ, wcześniej wywołaliśmy metodę set_imie("Lucky Luke") z argumentem przypisującym nową wartość do prywatnej zmiennej obiektowej self.__imie
print(puszek.get_glos()) # wywołanie metody bezargumentowej typu "getter" get_glos która zwraca wartość prywantej zmiennej obiektowej self.__glos, w tym wypadku zwróci wartość "Brak", ponieważ, obiekt został stworzony bez podania wartości wymaganych atrybutów, a więc zostąły im przypisane wartości domyślne
puszek.set_glos("Hau hau") # wywołanie metdy argumentowej typu "setter" set_glos, w argumencie metody przekazujemy wartość jaką chcemy przypisać prywantej zmiennej obiektowej self.__glos. W ten sposób zmieniamy wartość tej zmiennej, poprzez dodatkową metodę typu "setter". Musimy tak zrobić ponieważ klasa została napisana w sposób hermetyczny
print(puszek.get_glos()) # wywołanie metody bezargumentowej typu "getter" get_glos która zwraca wartość prywantej zmiennej obiektowej self.__glos, w tym wypadku zwróci wartość "Hau hau" ponieważ, wcześniej wywołaliśmy metodę set_glos("Hau hau") z argumentem przypisującym nową wartość do prywatnej zmiennej obiektowej self.__glos
print(puszek.get_gatunek()) # wywołanie metody bezargumentowej typu "getter" get_gatunek która zwraca wartość prywantej zmiennej klasowej self.__gatunek

# W powyższych przykładach 3 i 4 tworzyliśmy klasy z metodami bez argumentów oraz z argumentami.
# Teraz stworzymy klasę w której jedna metoda będzie wywoływać innę metodę.
# Gdy wywołujemy metodę względem obiektu, używamy notacji kropkowej, po nazwie obiektu i kropce piszemy nazwę metody zdefiniowanej w ciele klasy do której należy obiekt na którym chcemy wywołać metodę.
# Natomiast aby jedna metoda zdefiniowana w ciele klasy wywołała inną metodę należącą do tej samej klasy lub klasy nadrzędnej, używamy słówka self z notacją kropkową i po niej nazwę metody zdefiniowanej w tej klasie lub nadrzędnej.
# W definicji klasy mamy też możliwość, tak jak w przypadku funkcji, tworzenia kilkulinijkowych komentarzy które są wykorzystywane do opisywania klas przez środowisko IDE w którym pracujemy.
# W momencie kiedy chcemy utworzyć obiekt konkretnej klasy to środowisko IDE będzie nam podpowadać możliwe klasy do wyboru to po wybraniu klasy kursorami wyświetli nam się okienko z informacją zawartą w tym kilkulinijkowym komentarzu który zamieściliśmy definiując klasę.

# Przykład 5:
# Klasa zdefiniowana z metodami z których jedna metoda wywołuje inną metodę.

class Prostokat():
	def __init__(self, dl=1, szer=1):,
		"""
		Klasa tworząca obiekt typu prostokąt.
		Przyjmuje dwa argumenty:
		arg1 = długość naszego prostokąta (domyslnie = 1)
		arg2 = szerokość naszego prostokąta (domyślnie = 1)
		"""
		self.dl = dl
		self.szer = szer
	def pole_podstawy(self):
		"""
		Metoda obliczająca pole powrzechni naszego prostokąta na podstawie danych przyjętch podczas tworzenia obiektu.
		"""
		return self.dl * self.szer
	def obwod(self):
		"""
		
		"""
		return (2 * self.dl) + (2 * self.szer)
	def objetosc_prostopadloscianu_z_podstawy(self, wys=1):
		"""
		Metoda obliczająca objętość prostopadłościanu utworzonego na podstawie naszego prostokąta.
		Przyjmuje jeden argument:
		arg = wysokość prostopadłościanu (domyślnie = 1)
		"""
		return self.pole_podstawy() * wys

prost1 = Prostokat(5, 6)
print(prost1.dl)
print(prost1.pole_podstawy())
print(prost1.obwod())
print(prost1.objetosc_prostopadloscianu_z_podstawy(7))
print(prost1.objetosc_prostopadloscianu_z_podstawy(5))
