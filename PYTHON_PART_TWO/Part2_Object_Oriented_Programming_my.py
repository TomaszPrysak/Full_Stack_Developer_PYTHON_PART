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
class Przyklad(): # definicja klasy o nazwie "Przyklad". Od tego momentu możemy już tworzyć obiekty typu Przykład.
				  # Zgodnie z konwencją nazwy klas zaczynają się wielką literą.
	pass # ciało klasy Przyklad.

przyklad1 = Przyklad() # utworznie obiektu przyklad1, który jest instancją klasy Przyklad.
					   # Tak naprawdę nowy obiekt klasy Przyklad przypisalismy do zmiennej przyklad1. Dlatego posługujemy się nazwą zmiennej jako nazwą nowego obiektu klasy Przyklad.
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
# Parametr self w każdej zmiennej obiektowej umożliwia dostęp do tej zmiennej w ramach całej klasy i klas nadrzędnych, z których ta klasa dziedziczy.
# UWAGA!!! Jeżeli zdefiniujemy naszą metodę init z kilkoma argumentami to podczas tworzenia nowej instancji naszej klasy (tzn. nowego obiektu tej klasy) musimy podać wartości wszystkich argumentów.
#		   Jeżeli tego nie zrobimy to wystąpi błąd. Aby zabezpieczyć się przed możliwym brakiem wartości argumentów podanych przez użytkownika podczas tworzenia obiektu musimy w definicji metody init przypisać argumentom domyślne wartości.
# Jak będziemy chcieli użyć tej zmiennej w jakieś metodzie wewnątrz ciała klasy to również uzywamy self przed nazwą zmiennej.
# Dotyczy to dokładnie tego samego jak chcemy wywołać jakąś zmienną lub metodę na jakimś obiekcie, już poza klasą. To na jego nazwie po kropce wpisujemy nazwę tej zmiennej lub metody.
# W przypadku tworzenia klasy każdą zmienną i funkcję w definicji klasy rozpoczynamy od słówka self i po kropce piszemy nazwę zmiennej bądź funkcji.
# Słówko self oznacza, że odnosimy się do zmiennej lub metody tylko wewnątrz danej klasy.
# Jednocześnie pozwala metodzie w klasie wywołać inną metodę.
# Po stworzeniu obiektów z atrybutami mamy do nich dostęp za pomocą operatora kropkowego i nazwy zmiennej obiektowej.
# Odwołanie się do zmiennej obiektowej następuje bez nawiasu otwartego ponieważ to jest atrybut i nie przyjmuje żadnych argumentów.
# Obiekty tej samej klasy zawierają indywidualne wartości atrybutów. Każdy obiekt tej samej klasy może mieć różne wartości atrybutów.
# W Pytonie w programowaniu obiektowym istnieją też atrybuty stałe przypisane do każdej instancji obiektu.
# Nazywa się je zmiennymi klasowymi. Ich wartość będzie taka sama dla każdej instancji klasy czyli dla każdego obiektu danej klasy.
# Deklaruje się je zawsze na początku definicji klasy przed funkcją init. Normalnie tak jabyśmy deklarowali zmienną:
# class_variable1 = wartosc1
# Mamy dwie możliwości zmiany wartości zmiennej klasowej:
# - wywołując ja z nazwy obiektu. Wówczas jak zmienimy jej wartość to obiekt ten zachowa nową wartość. I wartość ta będzie indywidualna tylko dla tego obiektu. Nawet jeżlei zmienimy wartość zmiennej globalnej poprzez wywołanie jej z nazwy klasy.
# - jeżeli wywołamy ją z nazwy klasy. Wówczas jak zmienimy jej wartość to każdy obecny oraz przyszły obiekt będzie mieć nową wartość. Chyba, że indywidualnie dla obiektu zmienimy jej wartość. Wówczas ten jeden obiekt będzie miał inną wartość
# Bardzo ważne, jeżeli chcemy użyć zmiennej klasowej wewnątrz ciała klasy, na przykład w jakiejś metodzie wówczas musimy odnieść się do niej ze słówkiem self, tak jak to ma miejsce w zmiennej obiektowej. Jest też możliwość odniesienia się do tej zmiennej poprzez nazwę klasy i po kropce nazwę zmiennej.

# Przykład 2:
# Stworzymy klasę Pies której, zmienną klasową będzi gatunek a atrybutami będze jego imię oraz głos.
# Klasa ta będzie stworzona w sposób Pythonowski, tzn nie będzie hermetyzować zmiennych obiektowych.
# Będzie możliwy dostęp do zmiennych poprzez wywołanie ich w notacji kropkowej poza klasą.

class Pies():
	gatunek = "pies domowy" # deklaracja zmiennej klasowej, będzie taka sama dla każdej instancji tej klasy, czyli dla każdego obiektu tej klasy (chyba, że indywidualnie później nadpiszemy tą zmienną)
	def __init__(self, imie, glos): # funkcja wywoływana podczas inicjalizacji obiektu ustawiająca zmiennej obiektowe
		self.imie = imie # przekazanie parametru imie do zmiennej obiektowej self.imie, deklaracja zmiennej obiektowej
		self.glos = glos # przekazanie parametru glos do zmiennej obiektowej self.glos, deklaracja zmiennej obiektowej

tina = Pies("Tina", "Hauhau") # stworznie instancji o nazwie "tina" klasy Pies
rambo = Pies("Rambo", "Wrrrr") # stworznie instancji o nazwie "rambo" klasy Pies

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
print(rambo.gatunek) # odwołanie do zmiennej klasowej gatunek obiektu "rambo" po zmienie jej wartości dla całej klasy, będzie inna w stosunku do tego co definiowalimsy dla klasy, i zmieniła się ponieważ zmienialismy tą zmienną dla całej klasy
print(tina.gatunek) # odwołanie do zmiennej klasowej gatunek obiektu "tina" po zmianie jej wartości dla całej klasy, ALE dla tego obiektu nie została ona zmieniona bo wcześniej zmieniliśmy ja indywidualnie dla tego obiektu

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
												   # odwołanie się do zmiennych obiektowych self.radius nastepuje z użyciem self, ponieważ odwołujemy się do zmiennej aktualnej instacji obiektu na którym ją wywołujemy,
												   # natomiast odwołanie do zmiennej klasowej nastepuję poprzez nazwę klasy, natacji kropkowej wraz z nazwą zmiennej, można też użyć self przed nazwą zmiennej klasowej zamiast nazwy klasy, ale dzięki temu, że użyjemy nazwy klasy rozróżniamy zmienne klasowe i obiektowe.

kolo1 = Kolo(2) # stworznie instancji o nazwie kolo1 klasy Kolo
print(kolo1.radius) # odwołanie do zmiennej obiektowej radius obiektu kolo1, jeżeli chcemy się odwołać do zmiennj obiektowej używamy operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(kolo1.area()) # wywołanie metody bezargumentowej area na obiekcie kolo1, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
kolo2 = Kolo(5) # stworznie instancji o nazwie kolo2 obiektu Kolo
print(kolo2.radius) # odwołanie do zmiennej obiektowej radius obiektu kolo2, jeżeli chcemy się odwołać do zmiennj obiektowej używamy operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(kolo2.area()) # wywołanie metody bezargumentowej area na obiekcie kolo2, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów

# W powyższym przykładzie, zdefiniowaliśmy klasę z metodą bezargumentową.
# Kolejny przykład będzie zawierał metody z argumentami, które musimy podać w momencie ich wywoływania.
# Przykład ten zostanie powiązany z omówieniem programowania opartego o hermetyzację (enkapsulację), wówczas metody są niezbędne.
# Należy zaznaczyć, że programowanie hermetyczne nie jest typowym programowaniem Pythonowskim. Ponieważ z założenia Python nie ukrywa danych, nie implementuje żadnych metod hermetyzacji.
# Definiując klasy a w nich zmienne obiektowe oraz zmienne klasowe, z założenia mamy dostęp do zmiennych poprzez notację kropkową.
# W każdej chwili możemy wywołać taką zmienną i zmienic jej wartość. Nie potrzebujemy zatem definiować w klasie metod zwracającyh wartość danej zmiennej obiektowej (oraz zmiennej klasowej) czy metod do zmiany ich wartości. Po prostu wszystko wywołujemy je poprzez notacje kropkową i nazwę zmiennej.
# Programowanie hermetyczne w Pythonie należy niejako wymusić poprzez stosowanie prywatnych atrybutów, właściwości oraz metod typu "getters" oraz "setters". Tak jak to robimy w programowaniu obiektowym np. w Javie.
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
		return Pies_hermetyzajca.__gatunek # metoda zwraca wartość prywatnej zmiennej klasowej Pies_hermetyzajca.__gatunek, do prywantej zmiennej klasowej dostajemy się poprzez nazwę klasy i po kropce nazwy zmiennej, nie kończy się nawiasami ponieważ to atrybut a nie metoda, atrybuty nie przyjmują argumentów
	def get_imie(self): # definicja metody get_imie bez argumentów. Metoda opiera się na prywatnej zmiennej obiektowej (prywatnym argumencie) self.__imie
		return self.__imie # metoda zwraca wartość prywatnej zmiennej obiektowej self.__imie, do prywatnej zmiennej obiektowej dostajemy się słówko self i po kropce nazwy zmiennej, nie kończy się nawiasami ponieważ to atrybut a nie metoda, atrybuty nie przyjmują argumentów
	def set_imie(self, imie): # definicja metody set_imie przyjmującej jeden argument. Metoda opiera się na prywantej zmiennej obiektowej (prywatnym argumencie) self.__imie. Wartość argumentu przekazujemy do metody w momencie wywoływania tej metody z instancji obiektu
		self.__imie = imie # argument metody imie przekazujemy do prywatnej zmiennej obiektowej self.__imie, innymi słowy mówiąc nadpisujemy prywatną zmienną obiektową nową wartością którą przekazaliśmy do metody w postaci argumentu tej metody imie
	def get_glos(self): # definicja metody get_glos bez argumentów. Metoda opiera się na prywatnej zmiennej obiektowej (prywatnym argumencie) self.__glos
		return self.__glos # metoda zwraca wartość prywatnej zmiennej obiektowej self.__glos, do prywatnej zmiennej obiektowej dostajemy się słówko self i po kropce nazwy zmiennej, nie kończy się nawiasami ponieważ to atrybut a nie metoda, atrybuty nie przyjmują argumentów
	def set_glos(self, glos):  # definicja metody set_glos przyjmującej jeden argument. Metoda opiera się na prywantej zmiennej obiektowej (prywatnym argumencie) self.__glos. Wartość argumentu przekazujemy do metody w momencie wywoływania tej metody z instancji obiektu.
		self.__glos = glos # argument metody glos przekazujemy do prywatnej zmiennej obiektowej self.__glos, innymi słowy mówiąc nadpisujemy prywatną zmienną obiektową nową wartością którą przekazaliśmy do metody w postaci argumentu tej metody glos

puszek = Pies_hermetyzajca() # stworznie instancji o nazwie puszek klasy Pies_hermetyzajca
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
# Taka sama sytuacja się tyczy gdy opiszemy metodę w klasie, w momencie jej wywoływania na jednej z instancji obiektu również środowisko IDE wyświetli nam informacje z komentarza który zawarliśmy w definicji klasy.

# Przykład 5:
# Klasa zdefiniowana z metodami z których jedna metoda wywołuje inną metodę.
# Dodatkowo zastosowano komentarze wielolinijkowe w celu wyświetlania ich w śrdodowisku IDE

class Prostokat():
	def __init__(self, dl=1, szer=1): # funkcja wywoływana podczas inicjalizacji obiektu ustawiająca zmiennej obiektowe, jeżeli podczas inicjalizacji obiektu nie zostaną podane argumenty wówczas ich wartości będą domyślne dl=1, szer=1
		"""
		Klasa tworząca obiekt typu prostokąt.
		Przyjmuje dwa argumenty:
		arg1 = długość naszego prostokąta (domyslnie = 1)
		arg2 = szerokość naszego prostokąta (domyślnie = 1)
		jednostką jest mm
		"""
		self.dl = dl # przekazanie parametru dl do zmiennej obiektowej self.dl, deklaracja zmiennej obiektowej
		self.szer = szer # przekazanie parametru szer do zmiennej obiektowej self.szer, deklaracja zmiennej obiektowej
	def pole_podstawy(self): # definicja metody pole_podstawy bez argumentów. Metoda opiera się na zmiennych obiektowych. Z ich iloczynu zwraca pole powierzchni aktualnej instancji obiektu, czyli pole prostokąta
		"""
		Metoda obliczająca pole powrzechni naszego prostokąta na podstawie danych przyjętch podczas tworzenia obiektu.
		jednostką jest mm
		"""
		return self.dl * self.szer # iloczyn zmiennych obiektowych self.dl oraz self.szer
								   # odwołanie się do zmiennych obiektowych nastepuje z użyciem self, ponieważ odwołujemy się do zmiennej aktualnej instacji obiektu na którym ją wywołujemy,

	def obwod(self): # definicja metody obwod bez argumentów. Metoda opiera się na zmiennych obiektowych. Z sumy ich podwojonej wartości zwraca obwód aktualnej instancji obiektu, czyli obwód prostokąta
		"""
		Metoda obliczająca obwód naszego prostokąta na podstawie danych przyjętcyh podczas tworzenia obiektu.
		jednostką jest mm
		"""
		return (2 * self.dl) + (2 * self.szer) # suma iloczynu zmiennych obiektowych self.dl oraz self.szer
											   # odwołanie się do zmiennych obiektowych nastepuje z użyciem self, ponieważ odwołujemy się do zmiennej aktualnej instacji obiektu na którym ją wywołujemy,

	def objetosc_prostopadloscianu_z_podstawy(self, wys=1): # definicja metody objetosc_prostopadloscianu_z_podstawy przyjmującej jeden argument. Metoda zwraca objętość prostopadłościaniu opartego o wymiary naszego prostokąta.
															# Tworząc instancję obiektu Prostokat() podawaliśmy jedynie dwa argumenty będące długością i szerokością. Dlatego zatem metoda przyjmuje jeden argument, tzn. wysokość potrzebną do obliczenia objętości. Jeżeli nie podamy argumentu zmienna wys przjmie wartość domyslną 1.
															# Objętość prostopadłościanu oblicza się poprzez iloczyn pola podstawy i wysokości.
															# Ponieważ mamy osobną metodę już zdefiniowanej w tej samej klasie do obliczania pola podstawy w związku z tym nie będziemy jeszcze raz zapisywać obliczeń pola podstawy tylko wywołamy metodę self.pole_podstawy() zdefiniowanną w tej samej klasie, która zwróci nam wynik pola podstawy.
															# I wynik ten pomnozymy przez wartość argumentu przekazanego do metody w trakcie jej wywołania.
															# Słówko self tutaj, tak jak w przypadku odwoływania się do zmiennych obiektowych, oznacza, że odwołujemy się do metody aktualnej instacji obiektu na którym ją wywołujemy,
		"""
		Metoda obliczająca objętość prostopadłościanu utworzonego na podstawie naszego prostokąta.
		Przyjmuje jeden argument:
		arg = wysokość prostopadłościanu (domyślnie = 1)
		"""
		return self.pole_podstawy() * wys # iloczyn wartości zmiennej lokalnej wys będącej tak naprawdę argumentem metody oraz wartości otrzymanej z wywołania metody self.pole_podstawy()
										  # metoda self.pole_podstawy() była wcześniej zdefiniowana w klasie i zwraca iloczn zmiennych obiektowych self.dl oraz self.szer

prost1 = Prostokat(5, 6) # stworznie instancji o nazwie prost1 klasy Prostokat
print(prost1.dl) # odwołanie do zmiennej obiektowej dl obiektu prost1, jeżeli chcemy się odwołać do zmiennj obiektowej używamy operatora kropkowego, nie używamy nawiasów otwartych ponieważ to atrybut i nie przyjmuje żadnych argumentów
print(prost1.pole_podstawy()) # wywołanie metody bezargumentowej pole_podstawy na obiekcie prost1, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
print(prost1.obwod()) # wywołanie metody bezargumentowej obwod na obiekcie prost1, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
print(prost1.objetosc_prostopadloscianu_z_podstawy(7)) # wywołanie metdy argumentowej typu objetosc_prostopadloscianu_z_podstawy, w argumencie metody przekazujemy wartość jaką chcemy użyć w obliczeniach zdefiniowanych w metodzi
print(prost1.objetosc_prostopadloscianu_z_podstawy(5)) # wywołanie metdy argumentowej typu objetosc_prostopadloscianu_z_podstawy, w argumencie metody przekazujemy wartość jaką chcemy użyć w obliczeniach zdefiniowanych w metodzi

#/////////////////
#/////////////////
# Dziedziczenie

# W Pythonie obiekty definiujemy poprzez klasy, które pozwalają nam na podział obiektów na grupy.
# Przykładowy diagram przedstawiający klasy łączace instancje tych klas w grupy:

#          RZECZOWNIKI
#         /           \
#        /             \
# NIEŻYWOTNE           ŻYWOTNE
#     |                   |
#   ROWER             ZWIERZĘTA
#     |                   |
#  GÓRSKIE              SSAKI
#                         |
#                        PSY

# Czytając powyższy diagram można go interpretować następująco:
# Główną klasą jest klasa RZECZOWNIKI. O jeden poziom niżej mamy klasy:
# NIEŻYWOTNE oraz ŻYWOTNE.
# Ta pierwsza klasa ma pod sobą kolejno klasy ROWER a następnie GÓRSKIE.
# Ta druga ma kolejno klasy ZWIERZĘTNA, SSAKI i na końcu PSY.

# Jeżeli jedna klasa jest częścią durigej, to mówimy wtedy, że jest jej dzieckiem (child),
# a tę która ma w swojej części drugą klasę mówimy, że jest jej rodzicem (parent).
# Na naszym diagramie klasa znajdująca się bezpośrednio nad inną klasą jest jej rodzicem, a klasa bezpośrednio poniżej jest jej dzieckiem.
# Na przykład klasy Żywotne i Nieżywotne są dziećmi klasy Rzeczowniki, a to oznacza, że klasa Rzeczowniki jest ich rodzicem.
# Analogicznie klasa Ssaki jest rodzicem klasy Psy, która z kolei jest jej dzieckiem.
# Oczywiście relacje między kolasami nie sięgają tylko do jednego pokolenia w tył.
# Klasa Rzeczowniki jest rodzicem klasy Żywtone oraz przodkiem wszystkich innych klas znajdujących się pod nią (oczywiście już powiedzieliśmy, że jest ona rodzicem klasy Żywotne).
# Idąc dalej klasa Pies jest potomkiem klasy Rzeczowniki, ale również potomkiem klasy Żywtne i Zwierzęta.
# Jest też potomkiem klasy Ssaki, ale wówczas nazywamy ją dzieckiem klasy Ssaki.

# Aby poinformować Pythona, że dana klasa to dziecko innej klasy, nazwę klasy bazowej (nadrzędnej, rodzica) podajemy w nawiasach zaraz po nazwie naszej nowej klasy wg poniższej składni:
# class Parent():
#	code of class
# class Child(Parent):
#	code of class
# Nazwa klasy Parent w nawiasie przy nazwie klasy Child świadczy o tym, że klasa Child dziedziczy od klasy Parent.

# Powyższe wprowadzenie było potrzebne aby zrozumieć temat dziedziczenia.
# Dziedziczenie to sposób defniniowania nowych klas jako uzupełnienie, rozwinięcie klas już zdefiniowanych.
# Nowo utworzone klasy nazywane są pochodnymi (potomkami), dziedziczącymi, natomiast klasy od których pochodzą, dziedziczą nazywane są klasami bazowymi.
# Najważniejszym atutem dziedziczenia jest ponowne użycie kodu i zmniejszenie złożoności programu.
# Dzieje się tak dlatego, że klasy pochodne (potomkowie, dzieci) posiadają dostęp do metod i atrybutów (czyli zmiennych obiektowych oraz zmiennych klasowych) klas bazowych (rodziców, przodków). Czyli nie ma potrzeby ich ponownego implementowania.
# Stąd mówimy, że metody i atrybuty (zmienne) są dziedziczone.
# Takie podejście do programowania powoduje, że klasy pochodne (potomkowie, dzieci) rozszerzają, zmieniają funkcjonalność klas bazowych (rodziców, przodków).
# Rozszerzają, zmieniają ponieważ kod klasy będącej dzieckiem klasy bazowej będzie tak napisany aby miał wpływ na to co zawiera kod klasy bazowej.
# Będzie on zawierał odpowiednie metody i atrybuty przetwarzające informacje z klasy bazowej. Oczywiście będzie również zawierać unikatowe metody i atrybuty dla swojej klasy.

# W sytuacji gdy klasa dziedzicząca posiada więcej niż jedną klasę bazową (rodzicielską, przodka) oznacza, że obiekt tej klasy odziedziczy atrybuty po wszystkich rodzicach.
# W przypadku gdy wywołamy metodę czy atrybut (zmienną obiektową bądź klasową), ktory występuje tylko w jednym z rodziców, to sytuacja jest prosta — przeszukiwany jest najpierw pierwszy rodzic, potem drugi, itd., dopóki nie natrafimy na metodę bądź atrybut o żądanej nazwie.
# W sytuacji gdy wywołamy metodę czy atrybut (zmienną obiektową bądź klasową), dostępny u więcej niż jednego rodzica (to znaczy, że dana metoda czy atrybut w kilku klasach nadrzędnych ma taką samą nazwę), to decyduje kolejność dziedziczenia. Odziedziczone będzie to co znajduje się w najbliższym rodzicu (przodku).
# Mówimy tutaj o sytuacjach:
# 1. kiedy wywoływamy metodę bądź atrybut na istniejącej już instancji klasy, czyli za pomocą notacji kropkowej po nazwie obiektu podamy nazwę metody bądź atrybutu zdefiniowanego w klasie instancji tego obiektu bądź w klasie jej rodzica, potomka.
# 	 tina = Pies()
# 	 tina.klasa - wywołanie atrybutu klasa na obiekcie tina,
#	 Taki zapis spowoduje, że zostanie wywołany pierwszy napotkany atrybut (o tej nazwie) w hierarchi dziedziczenia, zaczynając od aktualnej klasy. Jeżeli atrybut o takiej nazwie znajduje się w kilku klasach nadrzędnych to wywołany zostanie pierwszy idąc w górę drzewka dziedziczenia.
# 	 Patrząc na przykład naszego drzewka, jeżeli stworzymy obiekt tina i będziemy chciali wywołać na nim atrybut klasa i atrybut ten będzie znajdować się zarówno w klasie Ssaki jak i Zwierzeta to wywołany zostanie atrybut z klasy Ssaki, bo jest ona pierwszym przodkiem klasy Psy.
# 2. kiedy wywołujemy w ciele klasy metodę zdefiniowaną w klasie nadrzednej, wówczas mamy dwa sposoby na jej wywołanie:
# a) ze słówkiem self przed nazwą metody bądź argumentu:
# 	 self.oblicz_dl_zycia()
# 	 ze słówkiem self i po kropce nazwę metody, dokładnie tak jakbyśmy wywoływali metodę zdefiniowaną w ciele tej samej klasy.
# 	 Taki zapis spowoduje, że zostanie wywołana pierwsza napotkana metoda (o tej nazwie) w hierarchi dziedziczenia, zaczynając od aktualnej klasy. Jeżeli metoda o takiej nazwie znajduje się w kilku klasach nadrzędnych to wywołana zostanie pierwsza idąc w górę drzewka dziedziczenia.
# 	 Patrząc na przykład naszego drzewka, jeżeli w ciele klasy Psy będziemy chcieli wywołać metodę oblicz_dl_zycia i metoda ta będzie znajdować się zarówno w klasie Ssaki jak i Zwierzeta to wywołana zostanie metoda z klasy Ssaki, bo jest ona pierwszym przodkiem klasy Psy.
# b) poprzez nazwę klasy i notację kropkową:
# 	 Ssaki.oblicz_dl_zycia(self)
#	 po nazwie konkretnej klasy i po kropce nazwę metody wraz ze słówkiem self w nawiasie, tak jakbyśmy przekazywali parametr do metody klasy.
# 	 Taki zapis umieszczony w klasie będącej dzieckiem klasy Ssaki spowoduje wywołanie metody oblicz_dl_zycia z klasy Ssaki.
# 	 A więc taki zapis powoduje, że nie musimy się martwić, że w kliku klasach dziedziczących jest metoda o nazwie oblicz_dl_zycia, ponieważ my podając przed nazwą metody nazwę klasy okreslamy z której klasy dziedziczącej wywłujemy tą metodę.
# 	 Uwaga !!! bardzo ważne aby w takim zapisie w nawiasie po nazwie metody wpisać słówko self, w przypadku kiedy metoda jest bezargumentowa bądź przyjmuje jakieś argumenty to musimy wpisać słówko self plus ewentualne argumenty.

# Przykład 6:
# Klasy zdefiniowane z dziedziczeniem z klas nadrzędznych.
# Dodatkowo pokazane zostaną dwa sposoby wywoływania metod bądź atrybutów z klas nadrzędnych (rodziców, przodków)

class Rzczeczowniki(): # klasa bazwowa, rodzic, wszystkich klas potomnych
	def kim_jestem(self): # metoda zwracająca stringa jak poniżej
		return "Samodzielna skladniowo i semantycznie odmienna czesc mowy"

class Zywotne(Rzczeczowniki): # klasa dziecko dziedzicząca z klasy rodzica Rzczeczowniki, sama jest rodzicem klas Zwierzeta, Saski, Psy
	klasa = "Zywotne" # zmienna klasowa, należy zauważyć, że w klasie Zwierzeta też wystepuje zmienna klasowa o takiej nazwie
	def dojrzewanie(self): # metoda zwracająca stringa jak poniżej
		return "Rosne"

class Zwierzeta(Zywotne): # klasa dziecko dziedzicząca z klas rodziców Zywotne oraz Rzczeczowniki, sama jest rodzicem klas Ssaki, Psy
	klasa = "Zwierzeta" # zmienna klasowa, należy zauważyć, że w klasie Zywotne też wystepuje zmienna klasowa o takiej nazwie
	def oddychanie(self): # metoda zwracająca stringa jak poniżej
		return "Wdech...Wydech..."
	def ruch_do_przodu(self): # metoda zwracająca stringa jak poniżej
		return "Ide do przodu"
	def ruch_do_tylu(self): # metoda zwracająca stringa jak poniżej
		return "Cofam sie"
	def ruch_w_lewo(self): # metoda zwracająca stringa jak poniżej
		return "Ide w lewo"
	def ruch_w_prawo(self): # metoda zwracająca stringa jak poniżej
		return "Ide w prawo"
	def test(self): # metoda zwracająca stringa jak poniżej
		return "Jestem testem ze Zwierzat"

class Ssaki(Zwierzeta): # klasa dziecko dziedzicząca z klas rodziców Zwierzeta, Zywotne oraz Rzczeczowniki, sama jest rodzicem klasy Psy
	def narodziny(self): # metoda zwracająca stringa jak poniżej
		return "Narodziny z matki"
	def karmienie_mlekiem(self): # metoda zwracająca stringa jak poniżej
		return "Karmienie mlekiem"
	def jedzenie_mleka(self): # metoda zwracająca stringa jak poniżej
		return "Ssanie mleka"
	def test(self): # metoda zwracająca stringa jak poniżej
		return "Jestem testem z Ssakow"
	def nazwa_klasy(self): # metoda która zwraca wartość zmiennej klasowej klasa,
						   # zmienna ta jest wywoływana z ciała klasy Ssaki, jednak w tej klasie nie znajduje się taka zmienna,
						   # a więc jest to zmienna dziedziczona po klasach rodzicach, w których ona występuje, tj. Zwierzęta i Zywotne,
		return self.klasa # wywołanie zmiennej klasowej dziedziczonej po rodzicach poprzez konstrukcje self.klasa powoduje, że zwróci wartość zmiennej klasowej tej która znajduje się w pierwszym rodzicu idąc w górę po drzewku dziedziczenia.

class Psy(Ssaki): # klasa dziecko dziedzicząca z klas rodziców Ssaki, Zwierzeta, Zywotne oraz Rzczeczowniki
	def __init__(self, name="Reksio"): # funkcja wywoływana podczas inicjalizacji obiektu ustawiająca zmienną obiektową, jeżeli podczas inicjalizacji obiektu nie zostanie podany argument wówczas ich wartość będzie domyślna name="Reksio"
		self.name = name # przekazanie parametru name do zmiennej obiektowej self.namel, deklaracja zmiennej obiektowej
	def szczekanie(self): # metoda zwracająca stringa jak poniżej
		return "Hau hau"
	def lizanie(self): # metoda zwracająca stringa jak poniżej
		return "Liz liz"
	def bieganie_do_przodu(self): # metoda wywołująca metodę dziedziczoną po przodku, a następnie zwracająca potrojoną wartość tego co zwróci metoda dziedziczona. Wywołoanie metody dziedziczonej nastąpuje poprzez słówko self i po kropce nazwa metody a więc zostanie wywołana metoda o tej nazwie u przodka u którego wystepuje, poszukiwanie jej zacznie się od najbliższego przodka i bedzie się zagłębiać aż do znalezienia tej metody u jakiekoś przodka.
		return (self.ruch_do_przodu() + " ") * 3
	def bieganie_slalomu(self): # metoda wywołująca kilka metod dziedziczonych po przodkach, a nastepnie zwracająca konkatenację wartości zwracanych przez te metody dziedziczone. Wywoływanie tych metod następuje poprzez podanie nazwy klasy z której są dziedziczone i po kropce nazwa metody. Dzięki temu w poszukiwaniu wywoływanej metody nie będą przeszukiwane wszystkie klasy będące przpdkami tylko od razu z konkretnej klasy będą dziedziczone metody.
		return (Zwierzeta.ruch_do_przodu(self) + " " + Zwierzeta.ruch_w_lewo(self) + " " + Zwierzeta.ruch_do_przodu(self) + " " + Zwierzeta.ruch_w_prawo(self) + " " + Zwierzeta.ruch_do_przodu(self)) * 2
	def zycie(self): # metoda wywołująca kilka metod dziedziczonych po przodkach, a nastepnie zwracająca konkatenację wartości zwracanych przez te metody dziedziczone. W tym wypadku wywołanie metod jest zarówno poprzez słówko self i po kropce nazwa metody jak i poprzez podanie nazwy klasy z której chcemy metody dziedziczyć i po kropce nazwa metody. Oba sosoby wywołania metod dziedziczonych zostały opisane w metodach "bieganie_do_przodu" i "bieganie_slalomu" tej aktualnej klasy.
		return self.narodziny() + " " + Ssaki.jedzenie_mleka(self) + " " + self.dojrzewanie() + " " + Zwierzeta.oddychanie(self) + " " + self.bieganie_do_przodu() + " " + self.lizanie()

tina = Psy("Tina") # stworznie instancji o nazwie tina klasy Psy
print(tina.name) # odwołanie do zmiennej obiektowej name obiektu tina
print(tina.bieganie_do_przodu()) # wywołanie metody bezargumentowej bieganie_do_przodu na obiekcie tina, metoda ta w swojej definicji w konstrukcji klasy Pies odwołuje się z kolei do metody self.ruch_do_przodu(), którą dziedziczy od swojejgo przodka najbliższego w hierarchi dziedziczenia
print(tina.bieganie_slalomu()) # wywołanie metody bezargumentowej bieganie_slalomu na obiekcie tina, metoda ta w swojej definicji w konstrukcji klasy Pies odwołuje się z kolei do metd które dziedziczy bezpośrednio od klasy Zwierzeta, a nie tak jak w powyzszym przypadku, że dziedziczy po najbliższym przodku. Sposób dziedziczenia wiadać po sposobie odwołania się do metody, tj. poprzez nazwę klasy
print(tina.zycie()) # wywołanie metody bezargumentowej zycie na obiekcie tina, metoda ta w swojej definicji w konstrukcji klasy Pies odwołuje się z kolei do metod które dziedziczy bezpośrednio od klasy Zwierzeta, Ssaki jak i od swojego przodka najbliższego w hierarchi dziedziczenia, czyli jest miksem różnych wywołań metod dziedziczących
print(tina.klasa) # wywołanie zmiennej klasowej klasa na obiekcie tina. Zmienna ta została zdefiniowana w klasie Zwierzęta. Widać tutaj tę charakterystykę i możliwości dziedziczenia w programowianiu obiektowym
print(tina.nazwa_klasy()) # wywołanie metody bezargumentowej nazwa_klasy na obiekcie tina, jednak co jest ciekawe metoda ta nie została zdefiniowana w klasie Psy, której instancją jest obiekt tina, a została zdefiniowana w klasie Ssaki, dodatkowo metoda ta wywołuje zmienną klasową, która została zdefiniowana w klasie Zwierzęta. Widać tutaj tę charakterystykę i możliwości dziedziczenia w programowianiu obiektowym
print(tina.test()) # wywołanie metody bezargumentowej test na obiekcie tina, jednak co jest ciekawe metoda ta nie została zdefiniowana w klasie Psy, której instancją jest obiekt tina, a została zdefiniowana w klasie Zwierzeta. Widać tutaj te charakterystykę i możliwości dziedziczenia w programowianiu obiektowym

# Dziedziczenie konstruktora klasy.

# Jak już było wspominane, dziedziczenie pomaga w oszczędności pisania kodu i elastyczności programowania.
# Bardzo ważne w kontekście dziedziczenia jest dziedziecznie konstruktora klasy.
# Ta możliwość dodaje właśnie tej elastyczności w programowaniu obiektowym.
# Możemy stoworzyć podobną klasę do już istniejącej, ta nowa klasa będzie wykorzystywać konstruktor klasy już istniejącej.
# Oczywiście jeżeli nie jest wymagane zdefiniowanie własnego konstruktora przez klasę która dziedziczy po rodzicu. Jeżeli byłaby taka konieczność to po prostu definiujemy konstruktor.

# W przykładzie poniżej stworzyliśmy klasę Rectangle która posiada dwa argumenty w konstruktorze klasy odpowiadające długości i szerokości prostokąta, które musimy podać tworząc nową instancję (obiekt) klasy Rectangle. Klasę tą wyposażyliśmy w metody obliczające obwód i pole prostokąta.
# Tworząc obiekt klasy Rectangle tworzymy obiekty o bokach o różnych wymiarach. Taka jest idea, aby taki obiekt był prostokątem. Nie będziemy tworzyć kwadratów jako obiektów klasy Rectangle.
# Chcemy odróżniać obiety typu kwadrat i prostokąt już na etapie tworzenia obiektu.
# W tym celu towrzymy klasę, dziecko, Square która dziedziczy z klasy rodzica Rectangle. Klasa Square posiada jeden argument w konstruktorze odpowiadający wymiarowi jego boku. A wiemy, że kwadrat to prostokąt o bokach jednakowej długości.
# I ten argument w konstrukotrze klasy Square jest przekazywnay do konstrukotra klasy Rectangle poprzez dziedziczenie w postaci następującej konstrukcji:
# ParentClass.__init__(self, arg1, arg2...) - UWAGA !!! takiej konstrukcji staramy się unikać. Pózniej będzie wytłumaczona funkcja super() która powinna być stosowana w takich wypadkach.
# w naszym wypadku: Rectangle.__init__(self, length, length).
# Oczywiście konstruktor klasy Rectangle wymaga dwóch argumentów, dlatego dwa razy użyliśmy tego samego argumentu z konstrukotra klasy Square, który jest podstawiany zarówno jako długość i szerokość w klasie Rectangle.
# Dzięki temu wykorzystując argumenty i metody klasy Rectangle stworzyliśmy szybko osobną klasę obiektów.

# Przykład 7
# Zaprezentowanie dziedziczenia konstruktora klasy.

class Rectangle(): # klasa bazwowa, rodzic, wszystkich klas potomnych
	def __init__(self, length=1, width=1): # funkcja wywoływana podczas inicjalizacji obiektu ustawiająca zmienne obiektowe, jeżeli podczas inicjalizacji obiektu nie zostanie podany argument wówczas ich wartość będzie domyślna
		self.length = length # przekazanie parametru length do zmiennej obiektowej self.length, deklaracja zmiennej obiektowej
		self.width = width # przekazanie parametru width do zmiennej obiektowej self.width, deklaracja zmiennej obiektowej
	def area(self): # definicja metody area bez argumentów. Metoda opiera się na zmiennych obiektowych. Z ich iloczynu zwraca pole powierzchni aktualnej instancji obiektu, czyli pole prostokąta
		return self.length * self.width # iloczyn zmiennych obiektowych self.length oraz self.width
										# odwołanie się do zmiennych obiektowych nastepuje z użyciem self, ponieważ odwołujemy się do zmiennej aktualnej instacji obiektu na którym ją wywołujemy,
	def perimeter(self): # definicja metody perimeter bez argumentów. Metoda opiera się na zmiennych obiektowych. Z sumy ich podwojonej wartości zwraca obwód aktualnej instancji obiektu, czyli obwód prostokąta
		return (2 * self.length) + (2 * self.width) # suma iloczynu zmiennych obiektowych self.dl oraz self.szer
													# odwołanie się do zmiennych obiektowych nastepuje z użyciem self, ponieważ odwołujemy się do zmiennej aktualnej instacji obiektu na którym ją wywołujemy,

class Square(Rectangle): # klasa dziecko dziedzicząca z klasy rodzica Rectangle
	def __init__(self, length=1): # cała magia dzieje się tutaj. A raczej wewnątz konstruktora. Ta funkcja jest wywoływana podczas inicjalizacji obiektu i ustawia jednną zmienną obiektową
		Rectangle.__init__(self, length, length) # CAŁA MAGIA TUTAJ !! W konstruktorze obecnej klasy uruchamiamy konstruktor z klasy z której dziedziczymy
											     # Argument wymagany przy inicjalizacji nowego obiektu klasy Square jest przekazywany do wywoływanego konstruktora klasy Rectangle
												 # Argument ten przekazywany jest podwójnie ponieważ tego wymaga konstruktor klasy Rectangle, a w związku z tym, że kwadrat to prostokąt o równych bokach to możemy argument przekazać w miejsca odpowiadające wymiarom długości i szerokości prodtokonta.

prostotkat1 = Rectangle(8,5) # stworznie instancji o nazwie prostotkat1 klasy Rectangle
print(prostotkat1.area()) # wywołanie metody bezargumentowej area na obiekcie prostotkat1, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
print(prostotkat1.perimeter()) # wywołanie metody bezargumentowej perimeter na obiekcie prostotkat1, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
kwadrat1 = Square(3) # stworznie instancji o nazwie kwadrat1 klasy Square
print(kwadrat1.area()) # wywołanie metody bezargumentowej area na obiekcie kwadrat1, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
print(kwadrat1.perimeter()) # wywołanie metody bezargumentowej perimeter na obiekcie kwadrat1, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów

# Po powyższym przykładzie widzimy, że w klasach dziedziczonych po rodzicac można wywoływać ich konstruktory.
# My jednak go wywołaliśmy w sosób jednoznaczny poprzez podanie nazwy klasy z której dziedziczymy i go wywołaliśmy.
# Jest lepszy i bardziej elastyczny sposób.

# Funkcja super() i automatyczne dziedziczenie konstruktorów.

# Tutaj przechodzimy do funkcji super().
# Funkcja ta dotyczy sytuacji w których chcemy wywołać metodę nadrzędną, czyli taką odziedziczoną po rodzicu.
# Normalnie kiedy chcemy wywołać metodę z klasy będącej rodzicem lub przodkiem to odnośmy się do niej bezpośrednio poprzez nazwę klasy i nazwę metody bądź poprzez słówko self i nazwę metody.
# Do tych dwóch opcji dochodzi jeszcze opcja dziedziczenia, właśnie z funkcją super():
# super().__init__(arg1, arg2, ..) - arg oznaczają ilość argumentów występujących w konstruktorze klasy nadrzędnej który wywołujemy
# super().method(arg1, arg2, ..) - arg oznaczają ilość argumentów występujących w metodzie klasy nadrzędnej którą wywołujemy
# Taka konstrukcja powoduje, że gdy zmieniamy hierarchię dziedziczenia i stosujemy funkcję super() nie musimy zmieniać wszystkich odwołań do odziedziczonych metod. Jeśli odwoływaliśmy się do metod rodzica przez super(), to automatycznie zaczniemy się odwoływać do metod nowego rodzica.
# Dodatkowo funkcja super() zachowuje się w szczególny sposób w sytuacji wielokrotnego dziedziczenia (czyli w sytuacji, gdy dana klasa ma więcej niż jednego rodzica - o czym później). O ile każda z metod w hierarchii wywołuje metodę "nadrzędną" przez funkcję super(), to wszystkie metody w hierarchii zostaną wywołane w pewnym ściśle określonym porządku.

# Przy okazji omawiania funkcji super() pokazana będzie bardzo ciekawa właściwość programowania obiektowego i dziedziczenia.
# Wyżej opisywana była możliwość dziedziczenia konstruktorów klas nadrzędnych. Teraz przedstawiona bedzie kolejna właściwość dotycząca dziedziczenia konstruktorów.
# Będzie to jeszcze większa MAGIA !! niż przy poprzednim dziedziczeniu konstruktorów i ich jawnym wywoływaniu.
# Poniżej stworzone zostały klasy: Rectangle_super() która jest rodzicem klasy Square_super() która z kolei jest rodzicem klasy Cube_super().
# Klasa Rectangle_super() posiada swój konstruktor, natomiast Square_super() też ma konstruktor w którym wywołuje konstruktor swojego rodzica, tj. Rectangle_super(). Jest to wymagane z powodu konieczności specyficznego przekazania argumentów do zmiennych obiektówych w konstrukotrze klasy Rectangle_super().
# Bardzo ciekawa jest klasa Cube_super(). Klasa ta nie ma swojego konstruktora a mimo to można stworzyć nową instancję klasy Cube_super() wraz z argumentem.
# Jak zatem tworzony jest nowy obiekt klasy Cube_super() wraz z argumentem pomino ze klasa ta nie ma swojego konstruktora ?
# Można to zrobić ponieważ klasa ta jest dzieckiem (dziedziczy) od klasie Square_super(). A więc skoro ona dziedziczy to dziedziczy wszystko.
# Skoro dziedziczy wszystko to dziedziczy też konstruktor. A więc nie trzeba jawnie pisać konstruktor w którym z kolei wywołany konstruktor klasy rodzica (nadrzędnej). Nie trzeba tego pisać, ponieważ w pełni wykorzystamy konstruktor klasy Square_super(). Gdybyśmy potrzebowali unikatowego konstruktora to musielibyśmy go zdefiniować. Tak jak miało to miejsce w klasie Square_super().
# Jest to super możliwość. Należy zwrócić uwagę, że tak jak dziedziczenie metod czy atrubutów, tak samo dziedziczenie automatyczne konstruktorów następuje tak,
# że program wędruje w górę naszego drzewka hierarchi i szuka konstruktora którego może użyć w celu stworzenia nowej instancji obiektu.
# Oczywiści należy pamiętać, żeby ten konstruktor który dziedziczymy spełniał potrzeby klasy która go dziedziczy (na dodatek jeżeli klasa dziedziczy wszystko po rodzicu to domyslnie wymaga podawania argumentu podczas inicjializacji nowego obiektu tej klasy. Jeżeli byśmy nie podali argumentu podczast tworzenia nowego obiektu to wystąpiłby błąd).
# Klasa Square_super() dziedziczy konstruktor po rodzicu poprzez wywołanie go za pomocą funkcji super(). Jest to wygodniejsze ponieważ dziedziczymy konstruktor po naszym najbliżcym przodku, czyli rodzicu i nie podajemy dzięki temu nazwy klasy.
# Klasa ta dziedziczy konstruktor jawnie aby podczas inicjalizacji nowego obiektu klasy Square_super() podstawić dwa razy ten sam argument do konstruktora klasy Rectangle_super().
# Jeżli nie byłoby tej "zmiany" w konstruktorze to tworząc nowy obiekt klasy Cube_super() i podając mu tylko jeden argument wystąpiłby błąd, ponieważ konstruktor klasy Rectangle_super() wyamga dwóch argumentów.

# Wyjaśnienie kwestii dziedziczenia konstruktorów czy to jawnie czy to za pomocą funkcji super() aż po automatyczne dziedziczenie udowadnia dlaczego programowanie obiektowe rozwija istniejące już klasy. I jest bardzo użytecznym i elastyczym programowaniem.
# Zamiast zagłębiać się w kod i dodawać do klasy jakieś metody to my po prostu tworzymy dodatkową klase, dziedziczącą po rodzicu, która bdzie mieć jedną dodatkową metodą i tak zwiększymy możliwości klasy rodzica. Bardzo prosto.
# Oczywiście to jeden z przykładów. Bo możliwości kombinowania w programowaniu obiektowym wraz z dziedziczeniem, które jest jego nieodłącznym elementem, są duże.

# Przykład 8
# Zaprezentowanie dziedziczenia przez funkcję super() oraz automatycznego dziedziczenia konstruktorów.

class Rectangle_super(): # klasa bazwowa, rodzic, wszystkich klas potomnych
	def __init__(self, length=1, width=1):  # funkcja wywoływana podczas inicjalizacji obiektu ustawiająca zmienne obiektowe, jeżeli podczas inicjalizacji obiektu nie zostanie podany argument wówczas ich wartość będzie domyślna
		self.length = length  # przekazanie parametru length do zmiennej obiektowej self.length, deklaracja zmiennej obiektowej
		self.width = width  # przekazanie parametru width do zmiennej obiektowej self.width, deklaracja zmiennej obiektowej
	def area(self): # definicja metody area bez argumentów. Metoda opiera się na zmiennych obiektowych. Z ich iloczynu zwraca pole powierzchni aktualnej instancji obiektu, czyli pole prostokąta
		return self.length * self.width # iloczyn zmiennych obiektowych self.length oraz self.width
										# odwołanie się do zmiennych obiektowych nastepuje z użyciem self, ponieważ odwołujemy się do zmiennej aktualnej instacji obiektu na którym ją wywołujemy,
	def perimeter(self): # definicja metody perimeter bez argumentów. Metoda opiera się na zmiennych obiektowych. Z sumy ich podwojonej wartości zwraca obwód aktualnej instancji obiektu, czyli obwód prostokąta
		return (2 * self.length) + (2 * self.width) # suma iloczynu zmiennych obiektowych self.dl oraz self.szer
													# odwołanie się do zmiennych obiektowych nastepuje z użyciem self, ponieważ odwołujemy się do zmiennej aktualnej instacji obiektu na którym ją wywołujemy,

class Square_super(Rectangle_super): # klasa dziecko dziedzicząca z klasy rodzica Rectangle_super()
	def __init__(self, length=1):  # cała pierwsza magia dzieje się tutaj. A raczej wewnątz konstruktora. Ta funkcja jest wywoływana podczas inicjalizacji obiektu i ustawia jednną zmienną obiektową
								   # Pomimo, że definiujemy osobny konstruktor dla naszej kalsy to tylko po to aby wywołać konstruktor z klasy nadrzędnej (rodzica) aby inaczej przekazać mu argumenty.
								   # Jeżeli nie byłaby wymagana żadna zmiana w konstruktorze to niemusielibyśmy definiować własny konstruktor dla tej klasy. Wystarczyłoby to, że dziedziczymy po klasie nadrzędnej a zatem dziedziczymy i konstruktor.
								   # Taka sytuacja będzie pokazana przy opisywaniu klasy Cube_super
		super().__init__(length, length) # W konstruktorze obecnej klasy uruchamiamy konstruktor z klasy z której dziedziczymy, jednak uruchamiamy go poprzez funkcję super(). W ten sposób jesteśmy elastyczni, ponieważ odwołujemy sie zawsze do klasy nadrzędnej (rodzica) niezależnie czym ta klasa jest. Jeżeli zmieniłaby się klasa będąca rodzicem to wówczas bedziemy dziedziczyć od tego nowego rodzica.
										 # Argument wymagany przy inicjalizacji nowego obiektu klasy Square_super() jest przekazywany do wywoływanego konstruktora klasy nadrzędnej (w tym wypadku klasy Rectangle_super())
										 # Argument ten przekazywany jest podwójnie, ponieważ tego wymaga konstruktor klasy Rectangle_super(), a w związku z tym, że kwadrat to prostokąt o równych bokach to możemy argument przekazać w miejsca odpowiadające wymiarom długości i szerokości prodtokonta.

class Cube_super(Square_super): # klasa dziecko dziedzicząca z klasy rodzica Square_super()
								# cała druga magia dzieje się tutaj. Klasa ta nie posiada konstruktora.
								# Nie jest to wymagane ponieważ klasa dziedziczy po klasie Square_super(). W dziedziczeniu jest tak, że dziedziczy wszystko, łącznie z konstruktorem.
								# A więc jeżeli obiekty tej klasy nie wymagają specjalnego konstruktora to nie musimy go definiować, wystarczy, że klasa ta odziedziczy go po klasie nadrzędnej (rodzicu).
								# Wówczas przy tworzeniu nowej instancji tej klasy (nowego obiektu) uruchamiany jest konstruktor klasy nadrzędnej (rodzica).
	def surface_area(self): # definicja metody surface_area bez argumentów wywołująca metodę dziedziczoną area()
		face_area = super().area() # pewna magia się tutaj dzieje. Do zmiennej (zwykłej) przypisywana jest wartość zwracana przez odziedziczoną bezargumentową metodę area().
								   # Cała klasa jest bardzo elasycznie stworzona. Tak samo ta metoda. Wiemy, że klasa odziedziczyła konstruktor po klasie Square_super(), a ta z kolei po Rectangle_super(). A wiec zmienne obiektowe to, tak jak w klasie Square_super() oraz Rectangle_super(), self.length oraz self.width. Tyle, że w przypadku Square_super() oraz Cube_super() dla obu zmiennych obiektowych wartości są takie same.
								   # Przechodząc do opisu co dzieje się w tej metodzie. Otóż, wywoływana jest metoda dziedziczona area(). Wywoływna jest za pomocą funkcji super(). Chcociaż funkcja super() dziedziczy po klasie nadrzędnej, a w klasie nadrzędnej nie ma metody area() to szukanie tej metody nastepuje w klasie po ktorej dziedziczy klasa Square_super(). Bardzo podobnie jak w przypadku wywoływania metod dziedziczonych z użyciem słówka self.
								   # Po prostu następiuje szukanie metody w górę drzewka dziedziczenia, aż zostanie znaleziona. A jak już metoda zostanie znaleziona to wynik tej metody jest przypisywany do zmiennej lokalnej face_area.
		return face_area * 6 # zwrócenie pomnożonej przez 6 wartości przypisanej do zmiennej lokalnej face_area. Metoda ta zwraca całkowite pole powierzchni ścian sześcianu.
	def volume(self):  # definicja metody volume bez argumentów wywołująca metodę dziedziczoną area
					   # w przypadku tej metody zasada i logika jest podobna jak przy metodzie surface_area.
		face_area = super().area() # wywołanie dziedziczonej funkcji area() i przypisanie zwracanej przez nią wartości do zmiennej face_area.
		return face_area * self.length # zwrócenie pomnożonego pola podstawy przez jedną ze zmiennych obiektowych aby otrzymać objętość sześcianu.
									   # Nie ma znaczenia która zmienna obiektowa zostanie użyta, ponieważ do obu została przypisana ta sama wartość podczas tworzenia obiektu Cube_super.
									   # A jak wiemy obiekt ten dziedziczy konstruktor po klasie Square_super który z kolei wywoluje w swoim konstrukotrze konstruktor klasy Rectangle_super ale przekazując mu pod argumenty opisujące długość i szerokość prostokąta tą samą wartosć.

# Klasa Square_super oraz Cube_super zostały zdefiniowane w sposób elastyczny z wykorzystaniem dziedziczenia konstruktorów jawnego (jeżeli jest potrzeba specyficznego dostosowania konstruktora który dziedziczymy) oraz automatyczneog (jeżeli konstruktor który dziedziczymy jest wystarczający).
# Dodatkowo dziedziczenie klas też został zastosowany w sposób elastyczny.

prostokat11 = Rectangle_super(3,5) # stworznie instancji o nazwie prostokat11 klasy Rectangle_super()
print(prostokat11.area())  # wywołanie metody bezargumentowej area na obiekcie prostotkat11, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
print(prostokat11.perimeter()) # wywołanie metody bezargumentowej perimeter na obiekcie prostotkat11, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
kwadrat11 = Square_super(4) # stworznie instancji o nazwie kwadrat11 klasy Square_super
print(kwadrat11.area()) # wywołanie metody bezargumentowej area na obiekcie kwadrat11, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
print(kwadrat11.perimeter()) # wywołanie metody bezargumentowej perimeter na obiekcie kwadrat11, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
szescian11 = Cube_super(3) # stworznie instancji o nazwie szescian11 klasy Cube_super
print(szescian11.surface_area()) # wywołanie metody bezargumentowej surface_area na obiekcie szescian11, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów
print(szescian11.volume()) # wywołanie metody bezargumentowej volume na obiekcie szescian11, używamy nawiasów ponieważ to jest metoda i mimo, że nie przyjmuje żadnych argumentów to konwencja wywoływania metod (funkcji też) nakazuje stosowanie nawiasów

# Wielodziczenie.

# Jest to narzędzie pozwalające na tworzenie skomplikowanych hierarchii dziedziczenia i daje spore możliwości programistyczne, z drugiej jednak strony, zbytnie skomplikowanie struktury klas dziedziczących prowadzi do trudnego opanowania i modyfikowania kodu.
# Wielodziedziczenia należy zatem unikać, jeśli nie jest niezbędne. Poniżej podam tylko podstawowe informacje na temat dziedziczenia wielobazowego

# Wielodziedziczeniem nazywamy sytuację, kiedy jedna klasa pochodna dziedziczy z conajmniej dwóch klas nadrzędnych.

# Najbardziej znanym problemem związanym z wykorzystaniem wielodziedziczenia jest problem diamentu. Przypadek ten polega na tym, że w ramach wielodziedziczenia jedna klasa istnieje kilkukrotnie w jednym drzewie dziedziczenia.

#        SAMOCHÓD
#        /      \
#       /        \
# MOTOCYKL     HELIKOPTER
#     \           /
#      \         /
#        ROWER

# W tym przypadku klasa SAMOCHÓD występuje dwukrotnie w naszym drzewie: po raz pierwszy ze strony klasy MOTOCYKL, po raz drugi od strony klasy HELIKOPTER.
# Aby poinformować Pythona, że dana klasa to dziecko dwóch innych klasy, nazwy bazowych (nadrzędnych) podajemy po sobie po przecinku w nawiasach zaraz po nazwie naszej nowej klasy wg poniższej składni.
# class Parent1():
#	code of class
# class Parent2():
#	code of class
# class Child(Parent1, Parent2):
#	code of class

# Aby pokaząć jak neleży dziedziczyć po kilku klasach bazowych przedstawione to będzie na przykładzie powyższej hierarchi (diamentu). Jednak nie będę się szczegółowo rozpisywać na temat tego przykładu.
# Tak jak zostało już powiedziane. Wielodziedziczenia należy unikać.

class Samochod():
	pass
class Motocykl(Samochod):
	pass
class Helikopter(Samochod):
	pass
class Rower(Motocykl, Helikopter): # zapis dziedziczenia po dwóch klasach bazowych
	pass

# Metody specjalne

# Dotychczas w przykładach naszych klas tworzyliśmy zawsze metdy które później były wywoływane (po stworzeniu instancji obiektu) poprzez konstrukcję: className.method(arg1, arg2, ...).
# Ja bym nazwał takie metody, metodami normalnymi, metodami użytkownika. To my tworzymy ich definicję od początku do końca. A zadania tych metod mogą być bardzo rózne. To zależy tylko od nas co te metody będą robić. I dlatego są wywoływane w taki sposób (className.method(arg1, arg2, ...)) ponieważ są unikatowe dla danej klasy (wraz z jej przodkami i dziećmi).
# Są jednak również metody, które są metodami specjalnymi. Nie wywołujemy ich poprzez nazwę klasy i po kropce nazwę metody, czy inaczej mówiąc, nie wywołujemy je bezpośrednio. Wywołuje je za nas Python w okreslonych okoliczniściach lub gdy użyjemy określonej składni. A to jak dana metoda będzie wywoływana zależy od każdej metody specjalnej z osobna.
# Ze specjalnym ich wywoływaniem wiąże się również specjalne ich definiowanie. Definiuje się podobnie jak konatruktor, z dwoma podkreślnikami na początku i na końcu metody specjalnej, tj:
# def __specMethod__(self, arg2, arg2, ...) - jeżeli metoda wymaga argumentów to się je podaje
# Metody specjalne mają z góry określone zadania (każda jest inna, oczywiście). Są częścią Pythona. Nie możemy zmieniać sposób działania takich metod. I dlatego sposób ich definiowania w klasie oraz sposób ich wywoływania w naszym kodzie jest z góry określony.
# Metody te pozwalają nam korzystać z funkcji specyficznych dla języka Python na obiektach tworzonych przez naszą klasę.
# Metod tych jest dużo. Opisanych zostanie kilka z nich i na nich zostanie przedstawiona zasada ich definiowania i wywoływania. Ponieważ to metody zawarte w Pythonie to informacje na ich temat znajdziemy w dokumentacji technicznej.

# Poniżej lika metod specjalnych:

# __str__(self) - metoda ta jest przydatna do tekstowej reprezentacji obiektu, jest ona wywoływana w momencie gdy użyjemy metody str() na obiekcie klasy zawierającej w ciele metodę specjalną __str__().
#                 Metoda str() służy do konwertowania argumentu na "stringa". A więc metoda specjalna __str__() umieszczona w ciele klasy będzie zwracała to co chcemy aby świadczyło o konwertowaniu naszego obiektu na "stringa" przy użyciu metody str().

#				  Metoda ta też jest wywoływana w momencie kiedy chcemy użyć metody print() z argumentem będącym obiektem klasy zawierającej w ciele metodę specjalną __str__().
#				  Metoda print() służy do zwracania na ekran argumentu. A więc metoda specjalna __str__() umieszczona w ciele klasy będzie zwracała to co chcemy aby było wyświetlone na ekranie po użyciu print() na obiekcie naszej klasy.

# Przykład 9
# Zaprezentowanie metody specjalnej __str__().

class Telewizor():
	def __init__(self, name="noname"):
		self.name = name
	def __str__(self): # definicja metody specjalnej, która nie przyjmuje argumentów.
					   # Jest wywoływana w momencie kiedy w kodzie wywołamy metodę str() bądź print() na naszym obiekcie.
		return "Telewizor marki: {x}".format(x=self.name) # zwracany string, który jest wynikiem przekonwertowania naszego obiektu na stringa bądź informacją tekstową zwróconą na ekran

philips = Telewizor("Philips") # stworzenie instancji o nazwie philips klasy Telewizor()
print(philips) # wywołanie metody print() na obiekcie philips (taki zapis, że piszemy samą nazwę klasy bez nazwy zmiennej obiektowej czy nazwy metody) spowoduje, że wywołamy metodę specjalną __str__() zawartą w ciele klasy, i zwrócony zostanie string który zapisalśmy w tej metodzie
x = str(philips) # wywołanie metody str() na obiekcie philips (taki zapis, że piszemy samą nazwę klasy bez nazwy zmiennej obiektowej czy nazwy metody) spowoduje, że wywołamy metodę specjalną __str__() zawartą w ciele klasy,i zwrócony zostanie string który zapisaliśmy w tej metodzie. Tutaj dodatkowo to co zostanie zwrócone przez metodę __str__() zostanie przypisane do zmiennej x
print(x) # wyświetlenie zawartości zmienne x, czyli to co zostało zwrócone przez metodę __str__() naszego obiektu

# __len__(self) - metoda ta jest wywoływana w momencie gdy użyjemy metody len() na obiekcie klasy zawierającej w ciele metodę specjalną __len__().
#     			  Metoda len() słuzy do zwracania ilości elementów obiektu na którym tą metodę wywolujemy. A więc metoda specjalna __len__() umieszczona w ciele klasy będzie zwracała to co chcemy aby świadczyło o ilości elementów obiektu przy użyciu na nim metody len()
#                 Należy zwrócić uwgę, że wartością zwracaną przez tą metodę musi być wartość integer.

# Przykład 10
# Zaprezentowanie metody specjalnej __len__().

class Ksiazka():
	def __init__(self, tytul="brak", autor="nieznany", liczbaStron=0):
		self.tytul = tytul
		self.autor = autor
		self.liczbaStron = liczbaStron
	def __len__(self): # definicja metody specjalnej, która nie przyjmuje argumentów.
	 				   # Jest wywoływana w momencie kiedy w kodzie wywołamy metodę len() na naszym obiekcie.
		return self.liczbaStron # zwracana wartość integer, która informuje nas o ilość elementów w naszym obiekcie
	def __str__(self):
		return "Autorem(ką) książki "''"{x}"''" jest {y}. Książka liczy {z} stron".format(x=self.tytul, y=self.autor, z=self.liczbaStron)

naszaSzkapa = Ksiazka("Nasza szkapa", "nie wiem", 3)  # stworzenie instancji o nazwie naszaSzkapa klasy Ksiazka()
print(naszaSzkapa)
print(len(naszaSzkapa)) # wywołanie metody len() na obiekcie naszaSzkapa (taki zapis, że piszemy samą nazwę klasy bez nazwy zmiennej obiektowej czy nazwy metody) spowoduje, że wywołamy metodę specjalną __len__() zawartą w ciele klasy, i zwrócona zostanie wartości integer którą zapisaliśmy w tej metodzie
y = len(naszaSzkapa) # wywołanie metody len() na obiekcie naszaSzkapa (taki zapis, że piszemy samą nazwę klasy bez nazwy zmiennej obiektowej czy nazwy metody) spowoduje, że wywołamy metodę specjalną __len__() zawartą w ciele klasy, i zwrócona zostanie wartości integer którą zapisaliśmy w tej metodzie. Tutaj dodatkowo to co zostanie zwrócone przez metodę __len__() zostanie przypisane do zmiennej y
print(y) # wyświetlenie zawartości zmienne y, czyli to co zostało zwrócone przez metodę __len__() naszego obiektu

# __add__(self) - jest jedną ze specjalnych metod matematycznych służącą do bezpośredniej interakcji między dwoma obiektami tej samej klasy.
#				  W tym przypadku jak nazwa wskazuje jest to metoda która jest wykonywana w momencie kiedy będziemy chcieli dodać dwa obiekty do siebie. Po prostu gdy zastosujemy zapis: objectName1 + objectName2. Wystarczy, że podamy tylko nazwy dodawanych obiektów. Bez konieczności wywoływania metody __add__(). To zresztą dotyczy wszystkich metod specjalnych.
#				  Ponieważ dodajemy dwa obiekty to w definicji funkcji podajemy to co chcemy dodwać.
#  				  Specjalne metody matematyczne w definicji wymagają podania argumentu który jest specyficzny: other. Oznacza to nic innego jak to, że argument z other pochodzi z drugiego obiektu tej samej klasy. Po prostu metody matematyczne (zazwyczaj) zachodzą między dwoma obiektami więc musimy jakoś poiformować, że argument do dodawania będzie pochodził z drugiego obiektu. I to robimy właśnie za pomocą słówka other.
#                 Właściwy zapis definicji metody w klasie zatem będzie następujący: __add__(self, other), a w definicji funkcji będzie występować ohter.variable
#           	  Metoda ta zwróci sume argumentów jakie zdefiniujemy w ciele tej metody. Oczywiście muszą to być liczby.
#				  Łatwo się domyslić, że możemy stosować więcej matematycznych metod specjalnych. Są to na przykład: odejmowanie (__sub__(), "-"), mnożenie (__mul__(), "*"), dzielenie(__truediv__(), "/"), potęgowanie(__pow__(), "**"). Takich metod jest wiecej i można je znaleźć w dokumentacji technicznej Pythona.

class Dzialka_budowlana():
	def __init__(self, dlugosc, szerokosc):
		self.dlugosc = dlugosc
		self.szerokosc = szerokosc
	def powierzchnia(self):
		self.powierzchnia = self.dlugosc * self.szerokosc
		return self.powierzchnia
	def __add__(self, other): # definicja matematycznej metody specjalnej, która przyjmuje other jako argumemt pochodzący z innego obiektu tej samej klasy do wykonania operacji matematycznej
		return self.powierzchnia + other.powierzchnia # zawracana jest suma tych samy zmiennych obiektowych (powierzchnia), jendak jedna będzie pochodzić z pierwszego obiektu (self.powierzchnia) a drugia z drugiego obiektu (other.powierzchnia). Taki zapis pozwala na dodawanie dwóch obiektów tej samej klasy. Oczywiście nie musimy dodawać dwóch tych samych zmiennych obiektówych.
													  # To co będzie dodawane z pierwszego obiektu będzie zapisane jako self, a to co będzie dodawane z drugiego obiektu będzie jako other.

dzialkaA30 = Dzialka_budowlana(10, 80)
print(dzialkaA30.powierzchnia())
dzialkaA31 = Dzialka_budowlana(7, 80)
print(dzialkaA31.powierzchnia())
print(dzialkaA30 + dzialkaA31) # wywołania operacji dodawania dwóch obiektów tej samej klasy, dzialkaA30 oraz dzialkaA31. Zapis dodawania dwóch obiektów do siebie z użyciem znaku dodawania oraz samych nazw obiektów spowoduje, że wywołana zostanie metoda specjalna __add__() zawarta w ciele klasy, a następnie zostanie zwrócony wynik dodawania.
							   # Taki sposób zapisu dodawnania jest prostszy i intuicyjny. Jest jeszcze jeden sposób wywoływania specjalnych metod matematycznych. Poniżej będzie to opisane.
print(dzialkaA30.__add__(dzialkaA31)) # wywołania operacji dodawania dwóch obiektów tej samej klasy, dzialkaA30 oraz dzialkaA31. Wywołanie następije porzez jawne wywołanie metody __add__() na obiekcie pierwszym, z drugim obiektem jako argumentem. Czyli w tym wypadku to ten drugi obiekt będący argumentem metody jest definicji metody jako other.
									  # Każda metoda matematyczna możliwość takiego wywołania.

###

# Linki do zewnętrznych materiałów:
# https://www.datacamp.com/community/tutorials/super-multiple-inheritance-diamond-problem
# https://www.datacamp.com/community/tutorials/property-getters-setters
