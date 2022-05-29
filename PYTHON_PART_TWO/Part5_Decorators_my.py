#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/////////////////
#/////////////////
# Dekoratory

# Dekoratory to wzorce projektowe w Pythonie, które można traktować jako funkcje rozszerzające funkcjonalność już istniejących funkcji bez modyfikowania ich struktury.
# Można też powiedzieć, że dekoratory pozwalają użytkownikowi dodawać nowe funkcje do istniejącego już obiektu (funkcji) bez modyfikowania jego struktury.
# Dekoratory są zwykle wywoływane przed zdefiniowaniem funkcji (obiektu), którą chcemy zmodyfikować. Pomagają skrócić kod i uczynić go bardziej "Pythonowym".

# Dekoratory dynamicznie zmieniają funkcjonalność funkcji, metody lub klasy bez konieczności bezpośredniego korzystania z podklas lub zmiany kodu źródłowego dekorowanej funkcji.
# Korzystanie z dekoratorów w Pythonie zapewnia również, że kod jest "czysty" (nie powtarza się). Dekoratorzy mają kilka przypadków użycia, takich jak:
# - autoryzacja w ramach frameworków takich jak Flask i Django
# - logowanie
# - mierzenie czasu wykonania
# - synchronizacja

# Funkcje w Pythonie są obywatelami (obiektami) pierwszej klasy ("first-class citizen"). Oznacza to, że obsługują takie operacje, jak przekazywanie argumentu do funkcji,
# zwracanie wyniku działania funkcji, modyfikowanie i przypisywanie całej funkcji (nie tylko wartości przez nią zwracanej) do zmiennej.
# Funkcje jako obiekty pierwszej klasy to podstawowa koncepcja, którą należy zrozumieć, zanim zagłębimy się w tworzenie dekoratorów Python.
# Poniżej przybliżymy tą koncepcję, ale najpierw przypomnienie z zasięgu zmiennych.

#/////////////////
#/////////////////
# Zasięg zmiennych - przypomnienie

# Ponieważ dekoratory dotyczą funkcji to warto też sobie przypomnieć o zasięgu zmiennych.
# Zagadnienia te szerze zostały opisane w pliku: "Part1_Scope_my.py".
# Krótkie przypomnieniej:
# Tworząc funkcje w Pythonie tworzymy przestrzeń w ramach której używane zmienne są zmiennymi lokalnymi.
# A więc zmienne z wnętrza funkcji nie są powiązane ze zmiennymi o takiej samej nazwie znajdującymi się poza funkcją.
# Powyższe nie ma zastosowania jeżeli wewnątrz funkcji użyjemy wyrażenia "global" przed nazwą zmiennej która ma taką samą nazwę jak zmienna poza funkcją.
# Rozwinięciem tematu zasięgu zmiennych są metody locals() oraz globals().
# locals() - zwraca słownik z nazwami lokalnych zmiennych jako klucze i ich wartościami jako wartości przypisane do kluczy.
           # Metodę tę wywołujemy wewnątrz tej funkcji z której chcemy się dowiedzieć jakie są w niej lokalne zmienne.
           # Tylko zmienne lokalne, nie będą zawarte zmienne globalne.
# globals() - zwraca słownik z globalnymi zmiennymi jako klucze i ich wartościami jako wartości przyposane do kluczy.
            # Metodę tę wywołujemy poza funkcją w głównym bloku kodu.
            # I tylko zmienne globalne, nie będą zawarte zmienne lokalne znajdujące się wewnątrz funkcji.


# Przykład 1:

bhp = "Ręce myj przez 30 sekud. Zmienna globalna" # zmienna globalna, ponieważ znajduje się poza funkcją

def czym():
    pasta = "Najlepiej myć ręce pastą BHP" # zmienna lokalna, ponieważ znajduje się wewnątrz funkcji i nie ma przed nią wyrażenia "global"
    print("ZMIENNE LOKALNE:")
    print(locals()) # wyświetla słownik wszystkich zmiennych lokalnych znajdujących się w naszej funkcji, ale do momentu umieszczenia metody locals().
                    # Należy zauważyć, że w tym słowniku znajdują się (będą się znajdować) inne funkcje zdefiniowane wewnątrz naszej funckji lub inne obiekty.
                    # Skoro jest to słownik to możemy wykonywać na nim metody dotyczące słowników jak i odnosić się do konkretnych elementów słownika poprzez podanie ich nazwy klucza i otrzymanie wartości do niego przypisanej.
    print(locals().keys())  # wywołanie metody keys() na słowniku który jest zwracany przez metodę locals(). Wynikiem bedzie słownik zawierający klucze ze słownika zwracanego przez metodę locals().
    print(locals()["pasta"]) # zwrócenie wartości z pary klucz:wartość gdzie kluczem jest nazwa zmiennej "pasta" a wartością jest wartość tej zmiennej.

print("ZMIENNE GLOBALNE:")
print(globals()) # wyświetla słownik wszystkich zmiennych globalnych znajdujących się w naszym kodzie, ale do miejsca umieszczenia metody globals().
                 # Należy zauważyć, że w tym słowniku znajduje się wiele zmiennych predefiniowanych przez samego Pythona.
                 # Jest tam również nasza funkca czym(). Oznacza to, że funkcje tak jak i inne obiekty też znajdują się (będą się znajdować) w takim słowniku.
                 # Skoro jest to słownik to możemy wykonywać na nim metody dotyczące słowników jak i odnosić się do konkretnych elementów słownika poprzez podanie ich nazwy klucza i otrzymanie wartości do niego przypisanej.

print("ZMIENNE GLOBALNE - TYLKO KLUCZE:")
print(globals().keys()) # wywołanie metody keys() na słowniku który jest zwracany przez metodę globals(). Wynikiem bedzie słownik zawierający klucze ze słownika zwracanego przez metodę globals().
print(globals()["bhp"]) # zwrócenie wartości z pary klucz:wartość gdzie kluczem jest nazwa zmiennej "bhp" a wartością jest wartość tej zmiennej.

czym() # wywołanie funkcji aby pokazać sposób działą metody locals() zawartej w tej funkcji.

#/////////////////
#/////////////////
# Funkcja jako obiekt

# Po krótkim wstępie dotyczącym zasięgu zmiennych kontynuujmy budowanie logiki tego, czym jest dekorator.
# Pamiętajmy że w Pythonie wszystko jest obiektem. Oznacza to, że funkcje też są obiektami.
# Obiekty możemy przypisywać do zmiennych i przekazywać je do innych obiektów.
# Zajmijmy się dokładnie funkcjami ponieważ to ich dotyczą dekoratory.
# Python jest bardzo elastyczny co do funkcji, możemy:
# - przypisywać funkcje do zmiennych,
# - definiować funkcje zagnieżdżone czyli definiować funkcje wewnątrz innych funkcji,
# - przekazywać funkcje jako argument innych funkcji,
# - definiować funkcje które wywołane zwracają inne funkcje,
# - definiować funkcje zagnieżdżone, które mają dostęp do zmiennych funkcji zewnętrznych (tych w których są zagnieżdżone).

#/////////////////
# Przypisanie funkcji do zmiennej

# W przypisywaniu funkcji do zmiennej należy uważać na zapis takiego działania. Można przypisać do zmiennej nazwę funkcji zakończoną podwójnym nawiasem "()", np.:
# zmienna = funkcja().
# Taki zapis oznacza, że do zmiennej przypisujemy wynik działania funkcji, ponieważ podwójny nawias "()" oznacza wywołanie funkcji. Nie przypisujemy zatem samej funkcji.

# Jeżeli chcemy przypisać funkcję do zmiennej nie używamy podwójnego nawiasu "()", np.:
# zmiennaDruga = funkcjaDruga.
# Ten zapis powoduje, że możemy używać nazwy zmiennej jako nazwy funkcji do której ta zmienna została przypisana.
# Po prostu funkcja nie jest wykonywana tylko tak jakby otrzymuje kolejną nazwę (nazwę zmiennej do której została przypisana) oprócz tej oryginalnej zapisanej po operatorze "def".
# I wówczas wywołanie zmiennej z podwójnym nawiasem "()" oznaczać będzie to samo jakbyśmy wywołali funkcję z jej nazwy oryginalnej, która została przypisana do tej zmiennej.
# Jeżeli taka funkcja miała argumenty to przekazujemy je tak samo jak w przypadku używania oryginalnej nazwy funkcji, czyli w nawiasie

# Przykład 2:
# Zdefiniujemy funkcję z argumentem która będzie dodawać do przekazywanego argumentu cyfrę 1.
# Następnie funkcję tą przypiszemy do zmiennej, ale bez znaku podwójnego nawiasu.

def plus_one(number): # definicja funkcji oryginalnej, która zwraca sumę przekazywanego argumentu oraz cyfry 1.
    return print(number + 1)

add_one = plus_one # przypisanie funkcji bez znaku podwójnego nawiasu do zmiennej
add_one(5) # wywołanie zmiennej z argumentem, tak jakbyśmy wywoływali funkcję, możliwe to jest dzięki przypisaniu funkcji bez nawiasów do zmiennej. Powoduje to to, że nazwa zmiennej jest traktowana jako nazwa oryginalna funkcji.
           # A w związku z tym, że oryginalna funkcja wymagała argumentu to wywołując zmienną również musimy podać argument w nawiasie.

#/////////////////
# Definiowanie funkcji wewnątrz innej funkcji (funkcje zagnieżdżone)

# Funkcja zagnieżdżona różni się od funkcji niezagnieżdżonej tylko tym, że tą pierwszą możemy wywołać tylko i wyłącznie
# z wnętrza funkcji w której ona została zdefiniowana. Funkcja zagnieżdżona staje się tak naprawdę funkcją lokalną. Próba wywołania funkcji zagnieżdżonej
# z głównego bloku naszego kod (czyli poza funkcją w której została zdefiniowana) skończy się wystąpieniem błędu. Funkcja zagnieżdżona poza funkcją w które została zdefiniowana jest niewidoczna.
# Sama konstrukcja definiowania funkcji zagnieżdżonej jest taka sama jak funkcji niezagnieżdżonej. Używamy po prostu konstrukcji:
# def functionName(arg):
#     code here
# Konstrukcji tej po prostu stosujemy wewnątrz innej funkcji.
# Samo wywołanie funcji zagnieżdżonej też odbywa się jak funkcji niezagnieżdżonej. Używamy po prostu konstrukcji:
# functionName(arg)
# Konstrukcji tej po prostu używamy wewnątrz funkcji po definicji funkcji zagnieżdżonej.
# Poniższy przykład 4 pokazuje sposób definiowania oraz przekazywania argumentemu w funkcji zagnieżdżonej.

# Przykład 3:

def hello(name="Tomek"): # definicja funkcji zewnętrznej, wewnątrz której zdefiniowane zostały funkcje zagnieżdżone
    print("Jesteśmy w funkcji hello()")
    def greet(): # definicja funkcji zagnieżdżonej która zwraca stringa
        return "Teraz jesteśmy wewnątrz funkcji greet()"
    def welcome(): # definicja funkcji zagnieżdżonej, która zwraca stringa
        return "A tera jestemy w funkcji welcome()"
    print(greet()) # wywołanie funkcji zagnieżdżonej, zostanie ona wywołana w moemencie kiedy wywołana zostanie funkcja zewnętrza (czyli ta w której funkcja zagnieżdżona się znajduje)
    print(welcome()) # wywoływanie funkcji zagnieżdżonej, zostanie ona wywołana w moemencie kiedy wywołana zostanie funkcja zewnętrza (czyli ta w której funkcja zagnieżdżona się znajduje)
    print("I znowu witamy w funkcji hello()")

hello() # wywołanie funkcji wewnątrz której zdefiniowane zostały funkcje zagnieżdżone.
try:
    welcome() # próba wywołania funkcji zagnieżdżonej poza funkcją w które została zdefiniowana. Poskutkuje to błędem dlatego polecenie to zostało umieszczone w bloku try except
except:
    print("Nie możemy wywołać funkcji welcome() ponieważ jest ona zdefiniowana wewnątrz funkcji hello().\nTo oznacza, że funkcja welcome() jest lokalnym obiektem funkcji hello() i nie mamy do niego dos†ępu z poza funkcji hello()")

# Przykład 4:

def dodaj_jeden_do(x): # definicja funkcji zewnętrznej z argumentem, wewnątrz której zdefiniowana została funkcja zagnieżdżona. Funkcja ta zwraca inkrementację o jeden wartości która zostanie przekazana do tej funkcji.
                       # Inkrementacja nastepuje w funkcji zagnieżdżonej, dlatego jeszcze trzeba wykonać funkcję zagnieżdżoną z przekazaniem do niej argumentu tego samego który został przekazany do funkcji zewnętrznej.
    def dodaj_wewnetrznie_jeden_do(x): # definicja funkcji zagnieżdżonej z argumentem.
                                       # W tym przykładzie argument funkcji zagnieżdżonej jest tak samo nazwany jak w funkcji w której ta funkcja została zdefiniowana.
                                       # Nie ma tutaj konfliktu ponieważ nazwa argumentu jest zawsze lokalną nazwą argumentu w funkcji w której się znajduje.
                                       # Oczywiście możemy ten argument nazwać inaczej niż dla funkcji zewnętrznej (tej w której została zdefiniowana funkcja zagnieżdżona) jednak dla przykładu nazwa została ta sama.
                                       # Funkcja ta zwraca zinkrementowaną o jeden wartość przekazaną do tej funkcji.
        return x + 1
    wynik = dodaj_wewnetrznie_jeden_do(x) # przypisanie do zmiennej wyniku wywołania funkcji zagnieżdżonej z przekazaniem do niej argumentu, tego samego który został przekazany do funkcji zewnętrznej (tej w której została zdefiniowana funkcja zagnieżdżona).
    return print(wynik) # zwrócenie zmiennej do której został przypisany wynik wywołania funkcji zagnieżdżonej

dodaj_jeden_do(44.4) # wywołanie funkcji wewnątrz której została zdefiniowana funkcja zagnieżdżona.
                     # Wywołanie funkcji następuje z przekazaniem jej argumentu. Który potem jeset przekazywany do funkcji zewnętrznej.

#/////////////////
# Przekazywanie funkcji jako argumentu innej funkcji

# Przekazywanie funkcji jako argumentu innej funkcji odbywa się na podobnej zasadzie jak przypisywanie funkcji do zmiennej.
# W nawiasie funkcji której jako argument przekazujemy inną funkcję musimy nazwę tej przekazywanej funkcji zapisać bez podwójnego nawiasu "()".
# W przeciwnym wypadku gdybyśmy przekazywaną funkcję zapisali z podwójny nawiasem "()" wówczas przekazalibyśmy wynik działania tej funkcji, a nie samą funkcję.
# Funkcja która otrzymała jako arugment inną funkcją w sowim kodzie będzie się posługiwać nazwą argumentu jako nazwą funkcji którą otrzymała.
# Wywołanie takiej funkcji z kodu innej funkcji nastepuje poprzez zapis nazwy argumentu z podwójnym nawiasem "()" a nie nazwy funkcji.
# Jeżeli funkcją którą przekazaliśmy miała argument to musimy w nawiasie wpisać argument jaki chcemy jej przekazać. Czyli nazwa argumentu jako nazwa funkcji i w nawiasie przkazywany argument do przakazanej funkcji :) Zagmatwane.
# Powyższe udowadnia, że przekazanie funkcji jako argumentu do innej funkcji jest podobne do przypisania funkcji do zmiennej, gdyż 
# wewnątrz tej funkcji do której przekazaliśmy inną funkcję jako argument, ten argument jest swego rodzajem zmienną do której przypisaliśmy funkcję.
# Przez co używamy nazwy argumentu jako nazwy funkcji.

# Przykład 5:

def znowu_dodaj_jeden_do(liczba): # definicja funkcji z argumentem - cała ta funkcja będzie z kolei argumentem przekazanym do innej funkcji
    return liczba + 1 # wartość zwracana przez tą funkcję

def funkcja_wywolujaca(funkcja_jako_argument): # definicja funkcji z argumentem którym będzie inna funkcja
    liczba_do_dodania = 5 # zmienna
    return print(funkcja_jako_argument(liczba_do_dodania)) # wartość zwracana przez tę funkcję to będzie wartość zwracana przez funkcję przekazaną do niej jako argument.
                                                           # Zapis "funkcja_jako_argument" to jest nazwa argumentu tej aktualnej funkcji pod posacią którego jest funkcja: "znowu_dodaj_jeden_do".
                                                           # Natomiast argument "liczba_do_dodania" zapisany w nawiasie to argument "liczba" funkcji "znowu_dodaj_jeden_do".
                                                           # Jest to zagmatwane ponieważ funkcja będąca argumentem innej funkcji również ma swój argument w definicji.

funkcja_wywolujaca(znowu_dodaj_jeden_do) # wywołanie funkcji "funkcja_wywolujaca" z funkcją "znowu_dodaj_jeden_do" jako argumentem.
                                         # Funkcja "znowu_dodaj_jeden_do" jest wywoływana wewnątrz funkcji "funkcja_wywolujaca" poprzez nazwę argumentu "funkcja_jako_argument".
                                         # Funkcja "znowu_dodaj_jeden_do" wymagana argumentu swojego, ale on już jest jej przekazywany wewnątrz funkcji "funkcja_wywolujaca".

# Przykład 6:

def czesc_Tomek(): # definicja funkcji bez argumentu - cała ta funkcja będzie z kolei argumentem przekazanym do innej funkcji.
    print("FUNKCJA JAKO ARGUMENT") # wyrzucenie stringa na ekran
    return "Czesc Tomku, mocarzu" # zwrócenie stringa

def funkcja_startowa(funkcja_jako_argument): # definicja funkcji z argumentem którym to będzie inna funkcja
    print("FUNKCJA OTRZYMUJĄCA INNĄ FUNKCJĘ JAKO ARGUMENT") # wyrzucenie stringa na ekran
    print(funkcja_jako_argument()) # wywołanie argumentu "funkcja_jako_argument" tej aktualnej funkcji pod postacią którego jest funkcja: "czesc_Tomek"

funkcja_startowa(czesc_Tomek) # wywołanie funkcji "funkcja_startowa" z funkcją "czesc_Tomek" jako argumentem.
                              # Funkcja "funkcja_startowa" ze swojego wnętrza wywołuje funkcję "czesc_Tomek" poprzez nazwę argumentu "funkcja_jako_argument"

#/////////////////
# Funkcje zwracające inne funkcje

# Zwracanie funkcji przez inną funkcję jest kolejną formą podobną do przypisywaniu funkcji do zmiennej. Na dodatek forma ta łączy się z zagadnieniem wyżej omawianym, a dokładniej ideą funkcji zagnieżdżonych.
# Zagnieżdżanie funkcji zostało już w tym rozdziale omówione. Po krótce: wewnątrz funkcji znajduje się definicja jeszcze jednej funkcji. Konstrukcja definicji funkcji zagnieżdżonej jest identyczna jak każdej innej funkcji.
# W definicji funkcji która ma w założeniu zwracać inną funkcję musimy zagnieździć funkcję która ma być zwracana.
# Zwracanie funkcji zagnieżdżonej odbywa się przez podanie po słówku "return" nazwy funkcji zagnieżdżonej którą chcemy zwrócić.
# Oczywiście nazwa funkcji zwracanej nie może zawierać na końcu podwójnego nawiasu "()". Bo byśmy zwrócili wynik działania funkcji a nie samą funkcję.
# Jendka abyśmy mogli zwrócić funkcję która jest zagnieżdżona w innej funkcji, wówczas musimy tą najbardziej zewnętrzną funkcję wywołać. A to robimy poprzez użycie nazwy funkcji, która ma zwrócić inną funkcję, razem z podwójnymi nawiasami "()".
# Czyli funkcję najbardziej zewnętrzą wywołujemy, używając na końu nazwy funkcji podwójnego nawiasu "()".
# Nastepnie w definicji funkcji najbardziej zewnętrznej umieszczamy definicję funkcji która ma zostać zwrócona.
# Na koniec w funkcji zewnętrznej używamy słówka "return" do oznaczenia co funkcja ma zwrócić, i po tym słówku używamy nazwy funkcji zagnieżdżonej bez podwójnego nawiasu "()".

# Dodatkowo musimy wywołanie funkcji najbardziej zewnętrznej przypisać do jakieś zmiennej.
# Spowoduje to przypisanie do tej zmiennej funkcji zagnieżdżonej w tej funkcji najbardziej zewnętrznej.
# Dzieje się tak dlatego, że funkcja najbardziej zewnętrzna zwracała jako wynik swojego działania funkcję w niej zagnieżdżoną.
# Daje nam to możliwość używania nazwy zmiennej jako funkcji zagnieżdżonej która była zagnieżdżona w funkcji ją zwracającej.
# Dzieki temu możemy wywoływać funkcję która była zagnieżdżona bez konieczności wywoływania funkcji najbardziej zewnętrznej w której to funkcji była definicja funkcji zagnieżdżonej.
# Wywołanie tej funkcji następuje po prostu poprzez wywołanie zmiennej z podówjnym nawiasem "()".
# Gdybyśmy wywołania funkcji najbardziej zewnętrznej nie przypisali do zmiennej to zwórciłaby ona nam adres w pamięci będący adresem funkcji.
# Nie zwróciłaby by ona wyniku tej funkcji zagnieżdżonej ponieważ my zaracaliśmy jej definicję, a nie wynik.

# Przykład 7:

def hello_function(): # definicja funkcji najbardziej zewnętrznej której wynikiem jest zwrócenie funkcji w niej zagnieżdżonej
    def say_hi(): # definicja funkcji zagnieżdżonej
        return "Hi" # wynik wywołania funkcji zagnieżdżonej
    return say_hi # wynik wywołania funkcji najbardziej zewnętrznej.
                  # Funkcja zwraca funkcję w niej zagnieżdżoną.

przywitaj_sie = hello_function() # przypisanie do zmiennej wyniku działania funkcji najbardziej zewnętrznej.
                                 # Wynikiem działania funkcji jest funkcja w niej zagnieżdżona, czyli do zmiennej przypisujemy funkcję która jest zagnieżdżona w funkcji najbardziej zewnętrznej.
                                 # Dzięki temu możemy wywoływać bezpośrednio funkcję zagnieżdżoną w innej funkcji.
print(przywitaj_sie()) # wywołanie zmiennej tak jakbyśmy wywoływali funkcję, a jest to możliwe ponieważ przypisalismy jej wynik działania innej funkcji która zwracała funkcję zagnieżdżoną w niej.
                       # Dzieki temu możemy teraz wywoływać funkcję zagnieżdżoną poprzez wywołanie zmiennej.

# Przykład 8:

def kim_jestes(name="Jarek"): # definicja funkcji z argumentem która jest najbardziej zewnętrzna, której wynikiem jest zwrócenie jedej z dwóch funkcji w niej zagnieżdżonych.
                              # To która funkcja zostanie zwrócona zależy od wartości jakie przyjmie argument. Domyślnie argument przyjmuje wartość "Jarek".
    def wyznawcaPiS(): # definicja funkcji zagnieżdżonej
        return "Jestem starym, grubym, głupim pisowcem." # wynik wywołania funkcji zagnieżdżonej
    def normalnyCzlowiek(): # definicja kolejnej funkcji zagnieżdżonej
        return "PiS to banda gamoni, hochsztaplerów, złodziei i kretynów !!!" # wynik wywołania funkcji zagnieżdżonej
    if name == "Jarek": # wyrażenie warunkowe
        return wyznawcaPiS # jeżeli zmienna "name", która jest argumentem funkcji, ma wartość "Jarek", wówczas jako wynik działania funkcji "kim_jestes" zwracana jest funkcja "wyznawcaPiS"
    else:
        return normalnyCzlowiek # jeżeli zmienna "name", która jest argumentem funkcji, ma wartość każdą inną niż "Jarek", wówczas jako wynik działania funkcji "kim_jestes" zwracana jest funkcja "normalnyCzlowiek"

Jarek = kim_jestes() # przypisanie wyniku działa funkcji "kim_jestes" do zmienej "Jarek".
                     # Funkcja została wywołana bez argumentu, a wiec skoro w definicji funkcji argument przyją domyślną wartosć to w wyniku wyrażenia warunkowego funkcja zwróciła funkcję zagnizdżoną "wyznawcaPiS".
Tomek = kim_jestes("Tomek") # przypisanie wyniku działa funkcji "kim_jestes" do zmienej "Tomek".
                            # Funkcja została wywołana z argumentem "Tomek", a wiec w wyniku wyrażenia warunkowego funkcja zwróciła funkcję zagnieżdżoną "normalnyCzlowiek".
print(Jarek()) # wywołanie funkcji funkcji zagnieżdżonej "wyznawcaPiS" przypisanej do zmiennej "Jarek" będącej wynikiem wywołania funkcji "kim_jestes" bez argumentu.
print(Tomek()) # wywołanie funkcji funkcji zagnieżdżonej "normalnyCzlowiek" przypisanej do zmiennej "Tomek" będącej wynikiem wywołania funkcji "kim_jestes" z argumentem innym niż "Jarek".

#/////////////////
# Funkcje zagnieżdżone, które mają dostęp do zmiennych funkcji zewnętrznych (tych w których są zdefiniowane)

# Python pozwala funkcjom zagnieżdżonym na dostęp do zmiennych wystepujących poza ich definicją.
# Jest to ściśle związane z zasięgiem zmiennych w Pythonie.
# Jeżeli w funkcji użyjemy jakiejś zmiennej to Python najpierw przeszukuje kod należący tylko do tej funkcji,
# jeżeli nie znajdzie w tej funkcji tej zmiennej to przechodzi o poziom wyżej,
# jeżeli funkcja ta była zagnieżdżona w innej funkcji to wówczas szuka zmiennej o tej nazwie w kodzie tej funkcji w której była zagnieżdżona.
# Jeżli też jej nie znajdzie to znowu idzie o poziom wżej. Tak, aż do głównego kodu programu. Jeżeli tam nie znajdzie to zwracany jest błąd braku zmiennej, nazwy.
# Zasięg zmiennych pozwala nie przekazywać do zmiennej wartości w postaci argumentu. Jednak tego nie powinno się stosować jako dobrej praktyki programowania.

# W przypadku dekoratorów jeżeli funkcja zagnieżdżona ma dostęp do zmiennej funkcji zewnętrznej,
# to jest to tak zwana koncepcja krytyczna - ten wzór jest znany jako "Zamknięcie".

# Przykłąd 9:

def wyswietl_wiadomosc(wiadomosc): # definicja funkcji zewnętrzej z argumentem
    "Funkcja zewnętrzna, otaczająca"
    def nadawca_wiadomosci(): # definicja funkcji zagnieżdżonej bez argumentu
        "Funkcja zagnieżdżona"
        print(wiadomosc) # wyświetlenie na ekran zmiennej "wiadomosc" będącą argumentem funkcji zewnętrznej "wyswietl_wiadomosc".
                         # Jak widać nie musieliśmy przekazywać zmiennej "wiadomosc" jako argumentu do funkcji zagniezdzonej "nadawca_wiadomosci".
                         # Po prostu użyliśmy tej zmiennej i Python używając zasadu zakresu zmiennych pobrał jej wartość z najbliższego wystąpienia tej zmiennej, a ta zmienna to argument funkcji "wyswietl_wiadomosc".
    nadawca_wiadomosci() # wywołanie funkcji zagnieżdżonej "nadawca_wiadomosci".

wyswietl_wiadomosc("PiS to samo zło") # wywołanie funkcji "wyswietl_wiadomosc" z przekazaniem do tej funkcji argumentu, który ma zostać wyświetlony.
                                      # Następnie wewnątrz tej funkcji wywoływana jest funkcja zagnieżdżona "nadawca_wiadomosci" która wyświetla wiadomość przakazaną do funkcji zewnętrznej "wyswietl_wiadomosc".
                                      # Argument ten nie jest przekazywany dalej do funkcji zagnieżdżonej "nadawca_wiadomosci", ale ona go i tak pobiera i wyświetla, ponieważ korzysta z zasady zasięgu zmiennych w Pythonie.

#/////////////////
#/////////////////
# Tworzenie dekoratorów

# Zagadnienia wcześniej omawiane w tej lekcji, związane z traktowaniem funkcji jako obiektów i możliwościami z tego wynikającymi,
# były konieczne do nauki, po to aby móc skutecznie tworzyć i wykorzystywać dekoratory.
# Do tworzenia dekoratorów wykorzystywane są takie funkcjonalności jak przypisywanie funkcji do zmiennej, przekazywanie funkcji jako argumentu innej funkcji oraz inne. To zależy od naszego podejścia do tworzenia aplikacji.

# Tak jak na samym początku było wspominane, dekoratory to wzorce projektowe w Pythonie.
# Inaczej mówiąc to swego rodzaju szablony budowania aplikacji, głównie wykorzystywane przez frameworki do budopwania aplikacji webowych.
# Znając sposób ich działania przyspieszamy budowanie aplikacji, ponieważ jedną składową będą dekoratory,
# a że my będziemy znać ich zastosowanie to przy każdej aplikacji tworzyć będziemy szablon stosując w nim dekoratory.
# Oczywiście każda aplikacja jest inna i wynik działania dekoratorów będzie inny, jednakże koncepcja stosowania dekoratorów ta sama.

# Dekorator to nic innego jest funkcja która została tak zdefiniowana, że stanowić będzie podstawę, szablon rozszerzający możliwości
# innych funkcji. Właśnie w zamyśle tworzenia dekoratorów jest to, żeby stworzyć w miarę uniwersalną funkcję która poźniej jako dekorator miała zastosowanie do rozszerzania możliwości innych funkcji.

# Przejdźmy do tworzenia dekoratorów.
# Funkcja będąca dekoratorem musi być zdefiniowana wraz z argumenttem, którym to będzie funkcja przekazywana do dekoratora. I to jest najistotniejsze !
# Przekazywanie funkcji do dekoratora jest najistotniejsze, ponieważ chcemy naszym dekoratorem rozszerzać możliwości innych funkcji.
# Rozszerzanie możliwości odbywa się poprzez przekazanie tej rozszerzanej funkcji jako argumentu do dekoratoram, po to aby dekorator miał do nich dostęp i mógł je rozszerzać.
# W definicji dekoratora znajduje się funkcja zagnieżdżona, która to jest zwracana w momencie wywołania dekoratora, jest ona najważniejsza i w miare możliwości będziemy ją nazywać "wrapper".
# Dodatkowo ta funkcja zagnieżdżona ma dostęp do argumentu przekazywanego do dekoratora, a więc do funkcji która jest do niego przekazywana.
# W definicji funkcji zagnieżdżonej dokonuje się wykonywanie operacji na tej funkcji którą dekorator rozszerza, która została do niego przekazana.
# Dopiero wynik funkcji zagnieżdżonej jest wynikiem ostatecznym działania dekoratora.
# A więc na początku tworzymy uniwersalną funkcję będącą dekoratorem do której będziemy przekazywać inne funkcje które chcemy aby dekorator roszrzerzał.
# Oczywiście dekorator tak definiujemy aby wykonywał na funkcji do nie przekazanej właściwe operacje.
# Ta funkcja bedzie takim naszym szablonem.

def uppercase_decorator(funkcja_jako_argument): # definicja funkcji z argumentem którym będzie inna funkcja
    def wrapper(): # definicja funkcji zagnieżdżpnej, która ma dostęp do argumentu funkcji najbardziej zewnętrznej
        wynik_dziala_funkcji_bedacej_argumentem = funkcja_jako_argument() # przypisanie do zmiennej wyniku działania funkcji będącej argumentem przekazanej jako argumentu do funkcji najbardziej zewnętrznej, a do którego argumentu ma dostęp funkcja zagnieżdżona
        x = wynik_dziala_funkcji_bedacej_argumentem.upper() # przypisanie do zmiennej metody upper() wywołanej na wcześniejszej zmiennej pomocniczej
        return x # wynik zwracany przez wywoływanie funkcji zanigeżdżonej
    return wrapper # wynik wywołania funkcji najbardziej zewnętrznej, zwracana jest definicja funkcji zagnieżdżonej w niej

# Następnie tworzymy funkcję (w budowaniu aplikacji będzie ich wiele) którą chcemy dekorować, w sposób uwzględniający definicję dekoratora. Tak aby po dekorowaniu jej, to znaczy, po przekazaniu do dekoratora jako argument, można było wykonać na niej operacje.
# Następnie przechodzimy do dekorowania stworzonej funkcji.
# Dekorować funkcje możemy manualnie. Odbywa się to poprzez przypisanie do zmiennej wyniku działania funkcji najbardziej zewnętrznej (czyli dekoratora) z przekazanym do niej argumentem będącym funkcją którą dekorujemy.
# Nastepnie w wyniku przypisania do zmiennej funkcji zagnieżdżonej w dekoratorze i przkazanym do niej argumentem, będącym funkcją którą dekorujemy, wykonujemy taką zmienną, tak jakbyśmy wykonywali funkcję.
# Zwracany jest wynik działania funkcji zagnieżdżonej.

def funkcja_z_dekoratorem_manualnym(): # definicja funkcji, która poddana zostanie dekorowaniu, przez funkcję wcześniej zdefiniowaną, będącą dekoratorem "uppercase_decorator", ale odbędzie się to w sposób manualny
    return "Siemanowizna" # wynik wywołania funkcji

dekorator_manualny = uppercase_decorator(funkcja_z_dekoratorem_manualnym) # przypisanie do zmiennej wyniku działania dekoratora "uppercase_decorator" do którego przekazaliśmy funkcję "funkcja_z_dekoratorem_manualnym" którą dekorujemy
print(dekorator_manualny()) # wywołanie zmiennej z wynikiem dokorowanej funkcji

# Jednak cała istota w dekoratorach leży w sposobie ich stosowania.
# Aby nie musieć tworzyć zmiennych do których przypisujemy wynik działania dekoratora z argumentem będącym funkcją dekorowaną, a następnie wywoływać te zmienne,
# tylko po prostu wykonywać od razu funkcję dekorowaną. A resztę wykona za nas Python.
# W tym celu przed definicją funkcji dekorowanej stosujemy następującą konstrukcję:
# @function_name_as_decorator
# def new_function():
#     code
# Powyższe powoduje, że w momencie wywołania funkcji dekorowanej Python niejako w tle przekazuje ją jako argument do dekoratora.
# Następnie w tle dekorator zwraca funkcję w nim zagnieżdżoną z przekazanym do niej arumentem, którym jest ta funkcja którą dekorujemy.
# A na koniec w tle wywoływana jest ta funkcja zagnieżdżona w której zachodzą operacje na argumencie, czyli funkcji dekorowanej.
# A na koniec wyświetlany jest wynik działania funkcji dekorowanej.
# Dzięki temu nie musimy tworzyć pomocniczych zmiennych, przypisywać do nich funkcjie itd.
# Po prostu wywołujemy funkcję z jej nazwy, a nie jakąś pomocniczą zmienną. Daje to pewne poczucie panowania nad kodem.
# Po prostu tworzymy definicję funkcji z dekoratorem nad nią, a następnie wywołujemy tą funkcję.

@uppercase_decorator # przypisanie dekoratora, wcześniej zdefiniowanego jako funkcja "uppercase_decorator", do funkcji poniżej zdefiniowanej
def funkcja_z_dekoratorem_automatycznym():  # definicja funkcji, która poddana zostanie dekorowaniu, przez dekorator wskazany w wierszu powyżej "uppercase_decorator", dekorowanie odbędzie się w sposób automatyczny, o czym świadczy wiersz wcześniejszy
    return "partykuła" # wynik wywołania funkcji

print(funkcja_z_dekoratorem_automatycznym()) # bezpośrednie wywołanie funkcji "funkcja_z_dekoratorem_automatycznym", która była dekorowana poprzez "uppercase_decorator".
                                             # Aby dostać wynik działania tej funkcji dekorowanej nie musieliśmy używać zmiennych pomocniczych.
                                             # To jest duże przewaga w stosowaniu dekoratorów przed definicją funkcji ponieważ nie stosujemy zmiennych pomocniczych a wywołujemy funkcję z jej nazwy a nie zmienną. Daje to pewne poczucie panowania nad kodem.

#/////////////////
# Dekorowanie funkcji wieloma dekoratorami

# Wręcz niemożliwe wydawałoby się, że programowanie nie pozwalałoby na udekorowanie funkcji więcej niż tylko jednym dekoratorem.
# I tak w istocie nie jest. Funkcję można dekorować dowolną ilością dekoratorów.
# Pod warunkiem oczywiście, że każdy dekorator został zdefiniowany w taki sposób, że dekorując funkcję wynik działania jednego dekoratora,
# nie spowoduje wystąpienia błędu podczas stosowania drugiego dekoratora i kolejnego i kolejnego.
# Inaczej mówiąc projektując dekoratory, oraz funkcje które będą kożystać z dekoratorów, należy uwzglednić to co chcemy uzyskać jako wynik dekorowania,
# w perspektywie tego, że jeżeli użyjemy kolejnego dekoratora na tej funkcji to wówczas musimy przemyśle wynik otrzymywany przez pierwszy dekorator.
# Tutaj przechodzimy do kwesti kolejności nakładania, stosowania dekoratorów na funkcję.
# Dekoratory przypisujemy do funkcji w następujący sposób:

# @decoratorThird
# @decoratorSecond
# @decoratorFirst
# def function():
#     Code

# W powyższym schemacie już zostały nazwane dekoratory według kolejności ich nakładania, stosowania na funkcję.
# Dekoratory są nakładane na funkcję od dołu w górę, czyli im bliżej definicji tym w pierwszej kolejności dekorator będzie nakładany.

# Przykład 10:

# Poniżej zdefiniowane zostały dwa dekoratory operujące na stringu zwracanym przez funkcję którą dekorują.
# Nie będe opisywał sposobu definiowania dekoratorów bo to zostalo omówione w rodziale "Tworzenie dekoratorów",
# a poniższe dekoratory mają identyczą konstrukcję jak we wskazanym rozdziale. Różnią się jedynie metodami w nich zastosowanymi.

# A więc dekorator "decorator_invert_object" iteruje od końca wynik jaki jest przekazywany do tego dekoratora.
# A dekorator "decoratr_split_object" dzieli zdanie przekazywanego do tego dekoratora wykorzsytując spację, tworząc przy tym listę składającą się ze słów które podzielił.
# I teraz, wszystko zależy od tego w jakiej kolejności zostaną zastosowane dekoratory.
# Zacznijmy od tego, że funkcja na którą nakłądamy dekoratory zwraca następującego stringa: "PiS to złodzieje".

# Przyopadek 1:

# Gdy pierwszym dekoratorem nałożonym będzie "decoratr_split_object" a drugim "decorator_invert_string",
# to wynik całości będzie następujący: ['złodzieje', 'to', 'PiS'].
# Wynika to z faktu, że dekorator "decoratr_split_object" zwróci listę: ['PiS', 'to', 'złodzieje'] - ponieważ on dzieli stringa na listę wykorzystując spację.
# Czyli najpierw zdanie zostanie podzielone na listę.
# A następnie dekorator "decorator_invert_object" odwraca kolejność w naszym przypadku listy będącej wynikiem działania dekoratora pierwszego.
# I stąd powstaje wynik: ['złodzieje', 'to', 'PiS'].

# Przypadek 2:

# Gdy pierwszym dekoratorem nałożonym będzie "decorator_invert_string" a drugim "decoratr_split_object",
# to wynik całości będzie nastepujący: ['ejeizdołz', 'ot', 'SiP'].
# Wynika to z faktu, że dekorator "decorator_invert_object" zwróci stringa: "ejeizdołz ot SiP" - ponieważ on iteruje od końca obiekty, a że string to obiekt to będzie on odwrócony.
# Czyli najpierw zdanie zostanie utworzone od końca.
# A następnie dekorator "decoratr_split_object" podzieli odwórconego stringa na listę wykorzystując spację.
# I stąd powstaje wynik: ['ejeizdołz', 'ot', 'SiP'].

def decorator_invert_object(funkcja_jako_argument):
    def wrapper():
        object_from_funcion = funkcja_jako_argument()
        inverted_object = object_from_funcion[::-1]
        return inverted_object
    return wrapper

def decoratr_split_object(funkcja_jako_argument):
    def wrapper():
        object_from_funcion = funkcja_jako_argument()
        splitted_object = object_from_funcion.split()
        return splitted_object
    return wrapper

@decorator_invert_object
@decoratr_split_object
def zdanie():
    return "PiS to złodzieje"

print(zdanie())

#/////////////////
# Przekazwywanie argumentów do funkcji zagnieżdżonej w dekoratorze

# Skoro dekorator to nic innego jak odpowiednio skonstruowana funkcja, która ma wpływ na inne funkcje nią dekorowane,
# to możemy stworzyć tak dekorator aby można było od niego przekazywać argumenty.
# Jednak są dwa raodzaje dekoratorów z argumentami.
# Jendym rodzajem są dekoratory, które umożliwiają na przekazywanie argumentów do funkcji w nich zagnieżdżonej, czyli do funkcji odpowiedzialnej za funkcjonalność dekoratora czyli do tzw. "wrappera".
# Drugim rodzajem są dekoratory, które umożliwiają na przekazywanie argumentów bezpośrednio do definicji dekoratora.
# W tym zagadnieniu zajmiemy się tymi pierwszymi.

# W momencie definiowania dekoratora, a zarazem definiowania funkcji zagnieżdżonej, tzw. wrappera, w nawiasie po nazwie "wrappera" dodajemy ilość argumentów,
# które będziemy przekazywać do niego w momencie dekorowania jakiejś funkcji dekoratroem z takim wrapperem.
# Wówczas podczas dekorowania funkcji argumenty przekazane do dekorowanej funkcji będę równocześnie przekazane do funkcji zagnieżdżonej w dekoratorze, do tzw. "wrappera".
# Dlatego istotne jest aby ilość argumentów "wrappera" w dekoratorze odpowiadała ilości argumentów przekazywanych w momencie wywoływania dekorowanej funkcji.
# Należy pamiętać, że kolejność argumetow przekazywanych do wywoływanej funkcji ma znaczenie, taka kolejność trafi wówczas do "wrappera" do argumentów na odpowiednich miejscach.
# Oczywiście funkcja którą dekorujemy również musi być zdefiniowana z argumentami. To znaczy, muszą być w nawiasie po nazwie funkcji wypisane argumenty które chcemy przekazać do tej funkcji.
# W samej funkcji nie muszą one brać udziału. Jednak w momencie wywołania funkcji z argumentami to zostaną one przekazane do "wrappera" dekoratora.

# Ważne jest też to, że argumenty przekazywane do funkcji którą dekorujemy nie są od razu wykorzystywane w momencie wywołania funkcji w głównym kodzie programu.
# Wynika to z faktu działania dekoratora. Jak wiemy, funkcja dekorowana jest przekazywana w momencie wywołania jako argument do dekoratora, a dokładniej do funkcji w nim zagnieżdżonej, tzw. "wrappera".
# Do "wrappera" przekazywane są również argumenty pochodzące z funkcji dekorowanej. Z tym, że nazwy argumentów zdefiniowane we "wrapperze" mogą się różnić od nazw argumentów zdefiniowanych w funkcji dekorowanej.
# Następnie to we "wrapperze" wywoływana jest funkcja ta którą dekorujemy. I dopiero w tym momencie przekazywane są do niej te argumenty, które przekazaliśmy w momencie jej wywoływania w głównym kodzie programu.
# W związku z tym, że argumenty są przekazywane do "wrappera" to możemy się nimi posługiwać i je wykorzystywać tak jakby osobno poza funkcją do której je przekazaliśmy, czyli poza tą którą dekorujemy.
# W momencie wywołania funkcji będącej argumentem we "wrapperze" wykonywany jest kod z tej funkcji, czyli funkcji dekorowanej. Jeżeli jest to funkcja zwracająca wartość to dodatkowo we "wrapperze" wynik tej funkcji zapisujemy do zmiennej.

# Podsumowując, dekorowana funkcja z argumentami jest wywoływana we "wrapperze" dekoratora i wtedy są do tej funkcji przekazywane argumenty.
# Argumenty przekazywane do "wrappera" mogą być wykorzystywane jako zwykłe zmiennej we "wrapperze", poza funkcją z której pochodzą (czyli z funkcji dekorowanej).

# Przykład 11:

# W poniższym przykładzie stworzyliśmy dekorator "decorator_with_arguments" z "wrapperem" "wrapper_accepting_arguments" zdefiniowanym z dwoma argumentami: "arg1" oraz "arg2".
# Funkcję "cities" którą dekorujemy również zdefiniowaliśmy z dwoma argumentami "city_one" oraz "city_two".
# W momencie wywołania funkcji cities z przekazaniem do niej dwóch argumentów zostaje wywołany dekorator do którego funkcja którą wywołaliśmy jest przekazywana.
# Następnie do "wrappera" są przekazywane również argument. Przekazywane zgodnie z kolejnością. A więc tak argument "city_one" przypisywany jest do argumentu "wrappera" "arg1".
# Argumnet "city_two" przypisywany jest do argumentu "wrappera" "arg2".
# Następnie we "wrapperze" argumenty mogą być dowolnie wykorzystywane.
# W naszym przypadku są one podsawiane do stringa i wyświetlane na ekranie.
# W kolejnej opracji wywoływana jest ta funkcja która została przekazana do dekoratora.
# Do tej funkcji przekazywane są argumenty które zostały przekazane do "wrappera" pod posatcią "arg1" oraz "arg2", czyli tak jakby wracają do tej funkcji.
# I dopiero wówczas jest wykonywany kod z definicji tej funkcji dekorowanej.
# I w zależności w jakiej kolejności przekażemy arguemtny "arg1" oraz "arg2" wówczas w takiej zostaną przekazane do funkcji "cities" pod argumenty "city_one" oraz "city_two".
# Widzimy tutaj, że wywołanie dekorowanej funkcji z argumentami w pewnej kolejności nie powoduje takiej kolejności przekazanej do tej funkcji, tylko kolejkność przekazanych argumentów do "wrappera".
# A dopiero we "wrapperze" wywoływana jest funkcja która została przeakazana do dekoratora, czyli ta funkcja deokorowana, i dopiero tam są jej przekazywane argumenty i w tym miejscu decydujemy w jakiej kolejności je tam przekażemy.
# Należy o tym pamiętać, że wywołanie funkcji dekorowanej z argumentami wpisanymi w nawiasie wcale nie oznacza, że w takiej kolejności trafią one do tej funkcji. O tym zdecyduje kolejność ich przekazania we "wrapperze".
# Ponieważ we "wrapperze" ta funkcja jest wywoływana jako funkcja przekazana do dekoratora. Jest bardzo mylne to, że wywołanie funkcji z argumentami spowoduje, że tak argumenty trafią do funkcji. Trzeba o to zadbać konstruując dekorator wraz z "wrapperem".
# W momencie jak "wrapper" wywoła naszą funkcję dokorowaną, to w naszym przykładzie argumenty przekazane do tej funkcji są podstawiane do stringa i wyświeltane na ekranie.

def decorator_with_arguments(funkcja_jako_arugment):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments passing to decorator are: {} and {}".format(arg1, arg2))
        funkcja_jako_arugment(arg1, arg2)
    return wrapper_accepting_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {} and {}".format(city_one, city_two))

cities("Jędrzejów", "Zawiercie")

#/////////////////
# Definiowanie dekoratorów ogólnego przeznaczenia

# Już wiele razy w kontekście dekoratorów było wspominane o tym, że to są zwykłe funkcjie i, że moża w nich wykorzystywać całą funkcjonalność jaką dają nam funkcje.
# W przypadku definiowania dekoratorów ogólnego przeznaczenia najlepiej jest podejść do tego jak do funkcji z niewiadomą ilością argumentów oraz niewiadomą liczbą nazwanych argumentów, czyli takich które oprócz wartości do funkcji przekazują też nazwę przypisaną do tej wartości (tak jakbyśmy przekazywali zmienną z wartością).
# W tym celu wykorzystujemy w definicji "wrappera", w miejscu argumentów, magiczne wyrażenia "*args" oraz "**kwargs".
# Wyrażenie “args” bierze się z od słowa “arguments”, czyli argumenty i jest to zazwyczaj zmienna, która zawiera krotkę z argumentami pozycyjnymi. Po krotce tej z łatwością możemy iterować oraz odwoływać się do jej elementów, aby dostać się do argumentów.
# Natomiast “kwargs” bierze się od “keyword arguments” czyli argumenty nazwane i wartością im przypisanym. Jest to zmienna w formie słownika, która zawiera pary nazwa_argumentu=wartość_argumentu. Przez słownik możemy iterować i odnosić się do jego elementów w sposób znany dla słowników.
# Największa magia kryje się w gwiazdkach poprzedzających powyższe wyrażenia. Natomiast “args” i “kwargs” możemy zastąpić dowolną ilością docelowych wartościami w przypadku "args" oraz dowolną ilością docelowych par nazwa=wartość w przypadku "kwargs".
# Umieszczając w definicji "wrappera" (oraz każdej innej funkcji kiedyś tam) wyrażenie z jedną lub dwoma gwiazdkami pozwalamy na przekazywanie do niej argumentów w dowolniej liczbie i nazwie. Bez konieczności konkretnego określenia tych argumentów oraz ich ilości.

# *args
# Wyrażenia z jedną gwiazdką "*" używamy gdy do funkcji chcemy przekazać dowolną liczbę argumentów pozycyjnych.
# Czyli takich dla których przy wywołaniu funkcji nie podajemy ich nazwy a jedynie wartości.
# Przekazanie wartości do funkcji bazuje na kolejności podania argumentów.
# Z tego powodu jeżeli we "wrapperze" (oraz każdej innej funkcji kiedyś tam) będzie na przykład jeden argument zawsze będzie konieczny, a pozostałe argumenty będą w niewiadomej ilości to parametr "*args" umieszczamy na końcu listy argumentów w definicji "wrappera".
# W momencie wywołania funkcji z niewiadomą liczbą argumentów to przekazane do niej argumenty zostały umieszczone w krotce po której z łatwością możemy iterować oraz odwoływać się do jej elementów, aby dostać się do argumentów.

# **kwargs
# W przypadku gdy do naszej funkcji chcemy przekazywać argumenty wraz z nazwami im przypisanymi to możemy użyć parametru z dwoma gwiazdkami (**).
# Przekazane w ten sposób argumenty są dostępne we "wrapperze" (oraz każdej innej funkcji kiedyś tam) w postaci słownika. Jego pary klucz:wartość odpowiadają nazwie argumentu i wartość do niej przypisanej.
# Przez słownik ten możemy iterować i odnosić się do jego elementów w sposób znany dla słowników, np.: dict[key] - odnosimy się do wartości przypisanej do klucza w słowniku.

# We "wrapperze" możemy używać obu poznanych przed chwilą parametrów.
# W tym przypadku należy jednak pamiętać o kolejności – wyrażenie z dwoma gwiazdkami musi być na końcu (**kwargs), z jedną gwiazdką wcześniej (*args), a jeżeli jeszcze mimo to chcemy przekazywać jakieś stale zdefiniowane argumenty to musimy je wymienić na początku, czyli przed "*args" oraz "**kwargs".

# Tworzenie dekoratora ogólnego przeznaczenia jest niczym innym jak tworzeniem dekoratora z przekazwyaniem do "wrappera" argumentów, ale nie o stałej ilości, a o niewadomej ilości.
# Funkcjonalność umożliwiającą przekazywanie do "wrappera" niewiadomej liczby arguemntów pozycyjnych, czy też argumentów z przypisanymi im nazwami.
# Realizujemy to z wykorzystaniem "*args" oraz "**kwargs".
# Jedyną rzeczą którą musimy uwzględnić jest konieczność zadbania o odwołania się do tych argumentów które przekazaliśmy. A ponieważ przekazujemy argumenty w formie krotki bądź słownika to musimy przez nie iterować bądź odwoływać się do nich tak jak pozwalają na to metody pracy z krtkami bądź słownikami.
# Pozostały mechanizm definiowania dekoratora z "wrapperem" pobierającym argumenty z funkcji dekorowanej jest niezmienny.
# Tak samo to, że argumenty przekazywane do funkcji którą dekorujemy nie są od razu wykorzystywane w momencie wywołania funkcji w głównym kodzie programu.
# To we "wrapperze" wywoływana jest funkcja ta którą dekorujemy. I dopiero w tym momencie przekazywane są do niej te argumenty, które przekazaliśmy w momencie jej wywoływania w głównym kodzie programu.
# Mając powyższe na uwadze musimy tak odpowiednio zdefiniować funkcję dokorowaną i "wrappera" aby argumenty odpowiednio trafiały do jednego jak i durgiego.
# Tak samo wykorzystanie argumentów w funkcji dekorowanej jak i "wrapperze" musimy przemyśleć.

# Należy pamiętać, że to, że do "wrappera" przekazujemy "*args" oraz "**kwargs" to nie znaczy, że musimy jakiekolwiek argumenty faktycznie przekazać.
# Właśnie o to chodzi we "wrapperach" (oraz każdej innej funkcji kiedyś tam) globalnego przeznaczenia.
# Przekazujemy niewiadomą liczbę argumentów. Co oznacza, że możemy nie przekazać tych argumentów wcale.

# Przykład 12:

# W poniższym przykładzie "wrapper" "a_wrapper_accepting_arbitrary_arguments" odbiera niewaidomą liczbę argumentów pozycyjnych jak i niewiadomą liczbę argumentów z przypisanymi im nazwami.
# W momencie jeżeli funkcja którą dekorujemy dekoratorem zawierającym taki "wrapperem" otrzymaj jakąś ilość pozycyjnych argumentów bądż argumentów z nazwami to trafiają one w postaci krotki lub słownika.
# I teraz we "wrapperze" sotosujemy metody do odwołania się do elementów tych kolekcji.
# W naszym przykładzie posłużyliśmy się pętlą for iterowaną przez elementy kortki, jeżeli przekażemy argumenty pozycyjny oraz również pętlę for iterującą przez słownik jeżeli przekażemy argumenty z nazwami.
# Iterując przez wszystkie elementy krotki bądź słownika (w zależności co przekażemy do funkcji) to wyświetlamy je na ekran.
# A następnie wywołujemy funkcję, tą którą dekorujemy i przekazujemy jej również "*args" oraz "**kwargs".
# Należy pamiętać, że to, że przekazujemy "*args" oraz "**kwargs" do funkcji to nie znaczy, że musimy jakiekolwiek argumenty przekazać. Właśnie o to chodzi w funkcjach globalnego przeznaczenia.
# Przekazujemy niewiadomą liczbę argumentów. Co oznacza, że możemy nie przekazać tych argumentów wcale.

def a_decorator_passing_arbitrary_arguments(funkcja_jako_argument):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('The positional arguments are:', args)
        for item in args:
            print(item)
        print('The keyword arguments are:', kwargs)
        for item in kwargs:
            print(item + " = " + kwargs[item])
        funkcja_jako_argument(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

# Przypadek ze zdefiniowaniem funkcji w której nie przekazujemy żadnych argumentów.
# Wywołanie funkcji odbywa się bez argumentów, mimo, że we "wrapperze" dekoratora użyliśmy "*args" oraz "**kwargs".

@a_decorator_passing_arbitrary_arguments
def function_with_no_arbitrary_argument():
    print("No arguments here.")

function_with_no_arbitrary_argument()

# Przypadek ze zdefiniowaniem funkcji do której przekażemt tylko argumenty pozycyjne.
# W definicji funkcji jest iteracja przez krotkę argumentów pozycyjnych.
# Podczas wywołania funkcji przekażemy trzy argumenty pozycyjne.

@a_decorator_passing_arbitrary_arguments
def function_with_argument(*args):
    print("This has shown arguments:")
    for item in args:
        print(item)

function_with_argument(1,2,3)

# Przypadek ze zdefiniowaniem funkcji do której przekarzemy tylko argumenty z przypisanymi im nazwami.
# W definicji funkcji jest iteracja przez słownik argumentów z przypisanymi nazwami.
# Podczas wywołania funkcji przekażemy dwa argumenty z ich nazwami.

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments(**kwargs):
    print("This has shown keyword arguments:")
    for item in kwargs:
        print(item + " = " + kwargs[item])

function_with_keyword_arguments(knur="Jarosław", zaskroniec="Jacek")

# Przypadek ze zdefiniowaniem funkcji do której przekarzemy argumenty pozycyjne oraz argumenty z przypisanymi im nazwami.
# W definicji funkcji jest iteracja przez krotkę argumentów pozycyjnych jak i przez słownik argumentów z przypisanymi nazwami.
# Podczas wywołania funkcji przekażemy dwa argumenty pozycyjne oraz dwa argumenty z ich nazwami.

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments(*args,**kwargs):
    print("This has shown arguments and keyword arguments:")
    for item in args:
        print(item)
    for item in kwargs:
        print(item + " = " + kwargs[item])

function_with_keyword_arguments(11,22,hiena="Andrzej", zmija="Zbigniew")

# CIEKAWOSTKA !!!

# Ciekawostką jest to, że możemy rozpakowywać jakąś kolekcję elemntów do pojedynczych argumentów zdefiniowanych we "wrapperze" (oraz każdej innej funkcji kiedyś tam).
# W tym celu używamy gwiazdki przed nazwą kolekcji którą chcemy rozpakować do argumentów zdefiniowanych w funkcji. Trzeba zwrócić uwagę na to, że liczba elementów w kolekcji musi być równa liczbie argumentów zdefiniowanych w funkcji.
# Spowoduje to rozpakowywanie krotki lub listy z argumentami lub słowników z parami klucz:wartość do argumentów zdefiniowanych w funkcji.
# Oczywiście podanie gwiazdki przed kolekcją następuje w momencie wywoływania funkcji. I stosujemy ten zapis w nawiasie.

# Przykład 13:

lista_argumentow = [1,3,5]
def rozpakowywanie(pierwszy, drugi, trzeci):
    print(pierwszy)
    print(drugi)
    print(trzeci)

rozpakowywanie(*lista_argumentow)

#/////////////////
# Przekazywanie argumentów do samego dekoratora

# W rozdziale dotyczącym przekazywania argumentów do funkcji zagnieżdżonej w dekoratorze, czyli do tzw. "wrappera" wspominaliśmy, że są dwa raodzaje dekoratorów z argumentami.
# Jednym rodzajem są dekoratory, które umożliwiają na przekazywanie argumentów do funkcji w nich zagnieżdżonej, czyli do funkcji odpowiedzialnej za funkcjonalność dekoratora czyli do tzw. "wrappera" - to już omawialiśmy.
# Drugim rodzajem są dekoratory, które umożliwiają na przekazywanie argumentów bezpośrednio do definicji dekoratora - teraz skupimy się właśnie na tym rodzaju dekoratorów z argumentami.

# W momencie definiowania dekoratora, w nawiasie po nazwie dekoratora, podajemy ilość argumentów, które będziemy do niego przekazywać w momencie wywoływania dekoratora nad funkcją którą dekorujemy.
# W tym momenci pojawia się najwięsza różnica w stosunku do tego jak do tej pory definiowaliśmy dekorator.
# Ponieważ do tej pory w definicji dekoratora po jego nazwie, w nawiasie, używaliśmy argumentu, do któego przekazywaliśmy dekorowaną funkcję, którą następnie wywoływaliśmy we "wrapperze".
# A teraz, jak już zostało wspomiane, przy nazwie dekoratora definiujemy argumenty do których będziemy przekazywać wartości, w momencie wywoływania dekoratora przy dekorowaniu funkcji.
# W związku z tym, że teraz definiujemy dekorator z argumentami przekazywanymi do niego jako wartości a nie funkcję to musimy jeszcze zdefiniować w nim dodatkowa funkcję zagnieżdżoną do której przekażemy dekorowaną funkcję jako argument.
# Jest to konieczne, ponieważ do dekoratora musimy przekazać funkcję którą dekorujemy. Na tym polegają dekoratory.
# A więc skoro w dekoratorze tworzymy dodatkową, zagnieżdżoną, funkcję do której będziemy przekazywać funkcję dekorowaną, to gdzie będzie nasz "wrapper" ?
# Otóż "wrapper" będzie jako funkcja zagnieżdżona, tej funkcji zagnieżdżonej którą definiujemy z argumentem będącym funkcją dekorowaną.
# Tą funkcją, która przechwytywać będzie naszą funkcję dekorowaną będziemy nazywać "dekoratorem wewnętrznym".
# I będzie to funkcją skrajnie zewnętrza w dekoratorze, a "wrapper" będzie funkcją skrajnie wewnętrzną.
# Aby to wyjaśnić, poniżej konstrukcja takiego dekoratora:

# def dekorator_z_argumentem(d_arg1, d_arg2, d_arg3):
#    def dekorator_wewnetrzny(funkcja_jako_dekorator):
#        def wrapper(w_arg1, w_arg2):
#            code
#            function(w_arg1, w_arg2)
#        return wrapper
#    return dekorator_wewnetrzny

# Skoro już mamy zdefiniowany dekorator z argumentami to teraz musimy nim udekorować porządaną funkcję.
# Do tej pory nad definicją dekorowanej funkcji pisaliśmy po znaku "@" nazwę dekoratora i tyle. Następnie był kod funkcji dekorowanej.
# W przypadku używania dekoratora z argumentami w momencie dekorowania funkcji (czyli nad funkcją dekorowaną), tuż po nazwie dekoratora, w nawiasie podajemy stosowną liczbę argumentów jakie chcemy do niego przekazać.
# Ilość ta musi być równa ilości argumentów jakie zdefiniowaliśmy podczas definicji dekoratora z argumentami.
# Należy pamiętać, że kolejność argumetow przekazywanych do dekoratora ma znaczenie. Taka kolejność trafi wówczas do dekoratora a dalej będzie używana we "wrapperze".
# Konstrukjca dekorowania funkcji dekoratorem z argumentami:

# @dekorator_z_argumentem(zmienna, "tekst", XX)
# def funkcj_dekorowana(f_arg1, f_arg2):
#     code

# funkcj_dekorowana(YY, "test")

# Powyższy przykład wywołania funkcji z argumentami przekazującej je do dekoratora również zdefiniowanego z argumentami przekazującego je do definicji dekoratora, pokazuje, że wewnątrz "wrappera" takiego dekoratora
# będziemy mieć, aż 5 różnych zmiennych, które możemy wykorzystywać na różne sposoby. Musimy pamiętać aby do funkcji którą wywołujemy z poziomu "wrappera" dekoratora przekazać tylko te argumenty z którymi wywoływaliśmy funkcję dekorowaną na samym początku.

# Przykład 14:

# W poniższym przykładzie stworzyliśmy dekorator o nazwie "dekorator_z_argumentami". Dekorator ten zdefiniowaliśmy z trzema argumentami: "decorator_arg1", "decorator_arg2", "decorator_arg3".
# W dekoratorze tym stworzyliśmy funkcję skrajnie zewnętrzną, czyli "dekorator wewnętrzy" o nazwie "dekorator_wewnetrzny" który odpowada za pobieranie funkcji dekorowanej jako argument: "funkcja_jako_argument".
# Konieczność stworzenia "dekoratora wewnętrznego" wynika z faktu definicji dekoratora z argumentami nie będącymi funkcją do nie go przekazaną.
# Dzięki temu dekorator ma w definicji argumenty będące przekazywanymi do niego wartościami, natomiast "dekorator wewnętrzny" posiada argument będący funkcją dekorowaną.
# W naszym dekoratorze zdefiniowaliśmy również funkcję skrajnie wewnętrzną, czyli "wrapper" o nazwie "wrapper" z trzema argumentami: "wrapper_arg1", "wrapper_arg2", "wrapper_arg3".
# W związku z tym, że "wrapper" w dekoratorze zdefiniowaliśmy z argumetami, a liczba arguemntów "wrappera" zawsze powinna odpowiadać liczbie argumentów zdefiniowanych w funkcji którą dekorujemy.
# A więc dekorowaną funkcję o nazwie "funkcja_dekorowana_z_argumentami" zdefiniowaliśmy również (tak jak "wrappera" w dekoratorze) trzema argumentami: "function_arg1", "function_arg2", "function_arg3".
# W momencie wywołania funkcji "funkcja_dekorowana_z_argumentami" z przekazaniem do niej trzech argumentów, zostaje wywołany dekorator "dekorator_z_argumentami" do którego funkcja którą wywołaliśmy jest przekazywana.
# Jednakże w związku z tym, że dekorator "dekorator_z_argumentami" zdefiniowaliśmy z argumentami to zapis:
# @dekorator_z_argumentami(pandas, "Leniwce", "Misie koala")
# powoduje, że do tego dekoratora są przekazywane trzy argumenty. I te argumenty będą dostępne we "wrapperze".
# W momencie wywołania funkcji dekorowanej we "wrapperze" dekoratora jest aż 6 argumentów do wykorzystania.
# Oczywiście kolejność przypisywania wartości tym argumentom wynika z kolejności ich przekazania czy to do wywoływanej funkcji czy to podczas wywoływania dekoratora podczas dekorowania funkcji.
# Czyli tak, argumenty z wywołania dekoratora: decorator_arg1=pandas, decorator_arg2="Leniwce", decorator_arg3="Misie koala".
# Natomiast argumenty z wywołania funkcji dekorowanej: function_arg1=pandas, function_arg2="Numpaje", function_arg3="Sajkitlerny".
# Sposób wykorzystania tych argumentów we "wrapperze" może być dowolny.
# W naszym przypadku są one podstawiane najpierw do stringa we "wrapperze". Podstawiane są wszystkie argumenty.
# W kolejnej opracji wywoływana jest ta funkcja która została przekazana do dekoratora, czyli dekorowana, poprzez polecenie:
# funkcja_jako_argument(wrapper_arg1, wrapper_arg2, wrapper_arg3)
# Do tej funkcji przekazywane są argumenty które zostały przekazane do "wrappera" pod posatcią "wrapper_arg1", "wrapper_ar2" oraz "wrapper_arg3", czyli tak jakby wracają do tej funkcji.
# I dopiero wówczas jest wykonywany kod z definicji tej funkcji dekorowanej.
# I w zależności w jakiej kolejności przekażemy arguemtny "wrapper_arg1", "wrapper_arg2" oraz "wrapper_arg2", wówczas w takiej zostaną przekazane do funkcji "funkcja_dekorowana_z_argumentami" pod argumenty "function_arg1", "function_arg2", "function_arg3".
# Widzimy tutaj, że wywołanie dekorowanej funkcji z argumentami w pewnej kolejności:
# funkcja_dekorowana_z_argumentami(pandas, "Numpaje", "Sajkitlerny")
# nie powoduje takiej kolejności przekazania argumentów do tej funkcji, tylko za kolejność przekazanych argumentów odpowiada "wrapper" dekoratora.
# Dopiero we "wrapperze" wywoływana jest funkcja która została przeakazana do dekoratora, czyli ta funkcja deokorowana, i dopiero tam są jej przekazywane argumenty i w tym miejscu decydujemy w jakiej kolejności je tam przekażemy.
# Należy o tym pamiętać, że wywołanie funkcji dekorowanej z argumentami wpisanymi w nawiasie wcale nie oznacza, że w takiej kolejności trafią one do tej funkcji. O tym zdecyduje kolejność ich przekazania we "wrapperze".
# Ponieważ we "wrapperze" ta funkcja jest wywoływana jako funkcja przekazana do dekoratora. Jest bardzo mylne to, że wywołanie funkcji z argumentami spowoduje, że tak argumenty trafią do funkcji. Trzeba o to zadbać wywołując funkjcę przekazaną jako argument z argumentami do "wrappera".
# W momencie jak "wrapper" wywoła naszą funkcję dokorowaną, to w naszym przykładzie argumenty przekazane do tej funkcji są podstawiane do stringa i wyświeltane na ekranie.

def dekorator_z_argumentami(decorator_arg1, decorator_arg2, decorator_arg3):
    def dekorator_wewnetrzny(funkcja_jako_argument):
        def wrapper(wrapper_arg1, wrapper_arg2, wrapper_arg3):
            print("Wrapper w dekoratorze ma dostęp do wszystkich zmiennych:\n"
                  "\t- tych z konstruktra dekoratora: {0} {1} {2}\n"
                  "\t- oraz tych wywołanych z funkjcą dekorowaną: {3} {4} {5}\n"
                  "Natomast tylko te wywołane w momencie wywołania funkcji dekorowanej przekazuje z powrotem do tej funkcji"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          wrapper_arg1, wrapper_arg2, wrapper_arg3))
            return funkcja_jako_argument(wrapper_arg1, wrapper_arg2, wrapper_arg3)
        return wrapper
    return dekorator_wewnetrzny

pandas = "Pandy"

@dekorator_z_argumentami(pandas, "Leniwce", "Misie koala")
def funkcja_dekorowana_z_argumentami(function_arg1, function_arg2, function_arg3):
    print("Funkcja dekorowana ma dostęp tylko do następujących argumentów: {0} {1} {2}".format(function_arg1, function_arg2,function_arg3))

funkcja_dekorowana_z_argumentami(pandas, "Numpaje", "Sajkitlerny")

#/////////////////
# Debugowanie dekoratorów

# Dekoratory dynamicznie zmieniają funkcjonalność funkcji, metody lub klasy bez konieczności bezpośredniego korzystania z podklas lub zmiany kodu źródłowego dekorowanej funkcji.
# Jednak co jeżeli będziemy mieć dużą ilość funkcji dekorowanych jednym dekoroatorem i pojawi się błąd. Wówczas debugowanie kodu z dekoratorami staje się uciążliwe.
# Najprostrzym sposobem debugowania dekoratorów jest możliwość uzystkania dostepu do ich danych wewnętrznych poprze metodę ".__name__" wywołaną na funkcji którą dekoroujemy.
# Konstrukcja powyższej metody:

# decorated_function.__name__

# Samo wywołanie metody "__name__" nie odpowie nam na pytanie jaka funkcja została przekazana do dekoratora. Użycie tej metody bez ingerencji w definicję dekoratora spowoduje, że zwórocna zostanie
# informacja: "wrapper". Czyli dostajemy informację o nazwie funkcji zagnieżdżonej w dekoratorze do której przekazywana jest funkcja dekorowana, czyli o nazwie "wrappera".
# Jeżeli chcemy, aby użycie metody "__name__" przyniosło skutek, tzn. pokazało na której funkcji przekazywanej do dekoratora wystąpił błąd, wówczas musimy udekorować "wrappera" dekoratora.
# Do tej pory mówiliśmy o dekorowaniu funkcji zewnę†rznych. A w tym wypadku musimy udekorować funkcję zagnieżdżoną w dekoratorze do której przekazujemy funkcję dekorowaną, czyli "wrappera".
# Zanim to zrobimy to musimy zaimportować bibliotekę "functools".
# Następnie w definicji dekoratora nad definicją funkcji zagnieżdżonej do której przekazujemy funkcję dekorowaną, tzn, nad "wrapperem" stosujemy metodę ".wraps" z biblioteki "functools".
# A dokładnie dekorujemy "wrappera" wyżej wymienioną metodą.
# Konstrukcja:

# def dekorator(funkcja):
#   @functools.wraps(funkcja)
#   def wrapper():
#       code
#   return wrapper

# Tak przygotowany dekorator oraz "wrapper" pozwoli na wywołanie na dekorowanej funkcji metody "__name__".
# Metoda ta jest pomocna przy debugowaniu kodu z dekoratorami.

# Przykład 15:

# Przykład wywołania metody "__name__" na funkcji która była dekorowana dekoratorem któego "wrapper" nie był poprzedzony dekoroatorem "@functools.wraps(funkcja)".
# Wówczas otrzymaliśmy informację "wrapper" czyli funkcję zagnieżdżoną w dekoratorze, przechwytującą funkcję dekorowaną.

print(funkcja_dekorowana_z_argumentami.__name__)

# Przykłąd 16:

# W poniższym przykładzie zaimportowaliśmy bibliotekę "functools" i zastosowaliśmy przed "wrapperem" w dekoratorze dekorator w postaci metody: "@functools.wraps(funkcja)".
# Takie rozwiązanie pozwoli wywołać metodę "__name__" na funkcji dekorowanej dekoratorem zdefiniowanym z dekoratorem "@functools.wraps(funkcja)" nad "wrapperem".
# Wynikiem wywołania tej metody na funkcji dekorowanej będzie zwrócenie jej nazwy a nie nazwy "wrappera" w dekoratorze którym to dekoratorem udekorowaliśmy tą funkcję.

import functools
def debuggujemy_dekoratory(funkcja_jako_argumnet):
    @functools.wraps(funkcja_jako_argumnet)
    def wrapper():
        x = funkcja_jako_argumnet().replace("sracze","klauny")
        return x
    return wrapper

@debuggujemy_dekoratory
def debuggujemy_funkcje():
    return "PiS to sracze"

print(debuggujemy_funkcje())
print(debuggujemy_funkcje.__name__)
