#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/////////////////
#/////////////////
# Pakiety i moduły

# Pakiety i moduły to zbiór często wykorzystywanych funkcji i klas lub innych obiektów zapisanych w osobnym pliku z kodem pythona (np.: moduleFileName.py).
# Pisząc złożoną aplikację bądź skrypt będziemy stosować wiele różnych funkcji i klas lub innych obiektów do których będziemy się odwoływać wiele razy.
# Warto dla czystego i przejrzystego kodu stowrzyć sobie osoby plik tylko z funkcjami, klasami lub innymi obiektami które będziemy importować w główny pliku wykonywalnym naszej aplikacji bądź skryptu.
# Nasz plik z biblioteką funkcji i klas lub innych obiektów nie będzie wykonywalny tylko będą z niego importowane tylko potrzebne funkcje i klasy lub inne obiekty, bądź będziemy importować całe pakiety lub moduły.
# Taki plik z funkcjami i klasami lub innymi obiektami nazywa się modułem lub jeżeli jest to kilka takich plików zebranych w "paczkę"" to nazywamy wówczas je pakietem.

# Python domyślnie zawiera już pewną grupę pakietów i modułów które w naszej dotychczasowej przygodzie z programowaniem w pythonie mogliśmy spotkać.
# Gdybyśmy przeanalizowali sktrukturę katalogów zainstalowanego Pythona spostrzeglibyśmy, że zawiera on wiele plików z rozszerzeniem *.py rozmieszczonych w różnych katalogach.
# Te własnie pliki to nic innego jak pakiety i moduły które albo Python sam importuje w tlen bez naszej wiedzy (ponieważ tak został skonstruowany) bądź my musimy jawnie zaimportować konkretne moduły lub funkcjie, klasy, obiekty z nich.

# Istotną częścią pakietów i modułów jest sposób ich importowania do naszej aplikacji bądź skryptu.
# Teraz omówimy sposoby importowania funkcji bądź klas z pakietów i modułów.
# Są trzy sposoby importowania funkcji i klas z pakietów i modułów.

# Największą zaletą importowania obiektów z pakietów i modułów jest ich bezpieczeństwo, ponieważ możemy jedynie pracować na nich w pliku w którym je importujemy, natomiast w pliku źródłowy, tzn. w pliku pythonowskim będącym modułem nie ma mozliwoci ich zmiany.

##/////////////////
# Sposób I - importowanie CAŁEGO pliku modułów bądź pakietów

# Składnia importowania:
# import moduleFileName

# Plik pythonowski z naszą biblioteką funkcji bądź klas lub innych obiektów musie być zapisany w tym samym katalogu co plik wykonywalny w którym importujemy moduł bądź pakiet.
# Następnie w pliku wykonywalnym pythona wpisujemy na samym początku kodu słówko "import" i po spacji nazwę pliku z naszym modułem bądź pakietem, ale UWAGA !! bez rozszerzenia ".py"
# W ten sposób zaimportowany moduł bądź pakiet umożliwia nam dostep do zawartych w nim funkcji bądź klas lub innych obiektów.

# Wywołanie funkcji z zaimportowanego pliku modułu bądź pakietu odbywa się poprzez następującą składnię:
# moduleFileName.functionNameInModuleFile()

# Inaczej mówiąc odwołanie się do funkcji nastepuje poprzez notację kropkową, którą mozna spotkać min. w wywoływaniu metod klasowych w programowaniu obiektowym.
# Po nazwie modułu stawiamy kropkę i po kropce piszemy nazwę funkcji którą chcemy z tego modułu wywołać.

# W celu wywołania funkcji z zaimportowanego modułu bądź pakietu należy najpeirw wywołać nazwę zaimportowanego moduła a następnie po kropce wywołać nazwę funkcji zapisanej w tym module, pakiecie.
# Oczywiście musimy pamiętać, że jeżeli wywołujemy funkcję bez argumentów to kończymy dwoma nawiasami "()", jeżeli wywołujemy funkcję z argumentami to między nawiasami musimy podać wymagane arumenty "(arg1, arg2)".

# Przykład 1:
import Part6_module_first_way_my # zaimportowanie modułu o nazwie "Part6_module_first_way_my.py". Jak widać rozszerzenie w trakcie importowania jest pomijane
Part6_module_first_way_my.pierwszySposob() # wywołanie funkcji pierwszySposob() z zaimportowanego modułu Part6_module_first_way_my.py

# Do tej porty wspominałem o funkcjach bądź klasa zapisanych w modułach które importujemy.
# Jednak nie muszą być to tylko funkcje bądź klasy. Mogą być to wszystkie rodzaje obiektów które wystepują w Pythonie: listy, słowniki, krotki, zmienne, itd.
# Po prostu jeżeli nie chcemy tworzyć za każdym razem tego samego rodzaju obiektów używanych w róznych aplikacjach wówczas zapisujemy sobie je w module bądź pakiecie i importujemy je i odwołujemy się do nich.
# Możemy te obiekty, funkcje, listy itd które znajdują się w importowynym module do zmiennych w pliku wykonywalnym.
# Dzięki temu mamy czysty kod w naszym główym pliku aplikacji.
# Oczywiście musimy pamiętać o tym aby do obiektów importowanych z modułów odwoływać się w taki sposób w jaki wymaga tego python, np.: do funkcji musimy odwoływać z podwójnym znakiem nawiasu itd.

# Przykład 2:
print(Part6_module_first_way_my.wrogowiePolski[:2]) # wyświetlenie dwóch pierwszych elementów listy wrogowiePolski z zaimportowanego modułu Part6_module_first_way_my.py

# Przykład 3:
nielubiani = Part6_module_first_way_my.wrogowiePolski # przypisanie do zmiennej nielubiani listy wrogowiePolski z zaimportowanego modułu Part6_module_first_way_my
print(nielubiani[2:]) # wyświetlenie elementów listy o indeksie 2 i w górę, ze zmiennej nielubiani do której wyżej została przypisana lista wrogowiePolski z zaimportowanego modułu Part6_module_first_way_my

##/////////////////
# Sposób II - importowanie CAŁEGO modułu ze zmianą jego nazwy poprzez pomocniczną nazwę, alias

# Składnia importowania z pomocniczną nazwą, aliasem:
# import moduleFileName as mod2

# Import modułu odbywa się w taki sam sposób jak w pierwszym sposobie.
# Po słówku "import" po spacji wpisujemy nazwę pliku pythonowskiego bez rozszerzenie który jest naszym modułem, biblioteką zawierającą nasze obiekty.
# Istotną zmianą jest to, że po nazwie modułu dodajemy po spacji słówko "as" i znowu po spacji nazwę którą będziemy używać jeżeli będziemy chcieli wywołać obiekt z importowanego modułu.
# Czyli zaimportowany w ten sposób moduł będziemy wywoływać poprzez słówko pomocnicze po słówku "as", a nie poprzez nazwę modułu.
# W przypadku różnych, skomplikowanych, a często podobnych nazw modułów ten sposób jest bardzo pomocny i upraszcza odwoływanie się do obiektów w modułach.

# Podsumowując sposób drugi importowania modułów umożliwia nam nadanie pomocniczej nazwy, aliasu dla zaimportowanego modułu.
# Dzięki temu w naszej aplikacji będziemy posługiwać się tą pomocniczą nazwą, aliasem w momencie wywoływania obiektów z modułu.

# Wywołanie obiektu z zaimportowanego modułu z pomocniczą nazwą, aliasem odbywa się poprzez następującą składnię:
# mod2.object / mod1.object()

# Inaczej mówiąc odwołanie się do obiektu nastepuje poprzez notację kropkową, którą mozna spotkać min. w wywoływaniu metod klasowych w programowaniu obiektowym.
# Po pomocnicznej nazwie modułu, aliasie stawiamy kropkę i po kropce piszemy nazwę obiektu który chcemy z tego modułu wywołać.

# Wywołanie obiektu z zaimportowanego modułu z pomocniczą nazwą, aliasem następuje w ten sposób, że najpierw podajemy tą pomocniczą nazwę, alias który użyliśmy podczas importowania modułu i po kropce nazwę obiektu z tego modułu.
# Oczywiście musimy pamiętać o tym aby do obiektów importowanych z modułów odwoływać się w taki sposób w jaki wymaga tego python, np.: do funkcji musimy odwoływać z podwójnym znakiem nawiasu itd.

# Przykład 4:
import Part6_module_second_way_my as mod2  # zaimportowanie modułu o nazwie Part6_module_second_way_my.py bez rozszerzenia. Dodatkowo została nadana nazwa pomocnicza, alias modułu o nazwie mod2
mod2.drugiSposob() # wywołanie z zaimportowanego modułu o pomocniczej nazwie mod2 munkcji drugiSposob()

# Przykłąd 5:
krotkaZmodulu = mod2.krajeDoOdwiedzenia # przypisanie krotki krajeDoOdwiedzenia z modułu zaimportowanego z nazwą pomocniczą, aliasem mod2, do zmiennej krotkaZmodulu
print(krotkaZmodulu) # wyświetlenie elementów zmiennej krotkaZmodulu do której wyżej została przypisana krotka krajeDoOdwiedzenia z zaimportowanego modułu Part6_module_second_way_my

##/////////////////
# Sposób III - importowanie TYLKO KONKRETNEGO obiektu z modułu

# Dwa poprzednie sposoby pozwalaly na importowanie CAŁYCH plików pythonowskich, zawierających zdefiniowane obiekty, jako moduły.
# Takie importowanie wymagało najpierw podania nazwy modułu bezpośrednio bądź wykorzystując nazwę pomocniczą, alias a następnie nazwę obiektu zdefiniowanego w pliku importowanego modułu.
# Takie odwoływanie się do obiektów importowanych jest dosyć długie i czasochłonne. Oczywiście można sobie pomagać tworząc zmienną i do niej przypisywać zaimportowany obiekt.
# Jednak jest krótszy sposób.

# Tym sposobem jest trzeci sposób importowania obiektów. Jest to bezpośrednie importowanie TYLKO określonego obiektu z pliku modułu.
# Składnia importowania TYLKO określonego obiektu z pliku modułu:
# from myModuleFile import object1

# Importowanie odbywa się poprzez podanie słówka "from" następnie po spacji nazwy pliku pythonowiskiego bez rozszerzenia py będącego naszym modułem.
# Nastepnie po spacji słówko "import" i znowu po spacji podajemy nazwę obiektu (funkcja, klasa, lista, słownik itd) zdefiniowanego w tym pliku.
# W tym importowaniu w momencie podawania nazwy obiektu który chcemy zaimportować nie musimy poprzedzać go nazwą modułu ponieważ nazwę tą podaliśmy wcześnie po słówku "from".
# Jeżeli chcemy zaimportować większą ilość obiektów z jednego modułu to wymieniamy je po przecinku w jednej lini po słówku "import".

# Omawiany sposób importowania daje tą wielką przewagę nad innymi, że wywoływanie zaimportowanych obiektów odbywa się tylko i wyłącznie poprzez podanie ich nazwy. Ta nazwa która została wymieniona w wierszu importowania to zarazem nazwa zdefiniowana w pliku modułu.
# Wywołanie obiektu w wyniku importowania TYLKO określonych obiektów z pliku modułu:
# object1 / object1()

# Poprostu podajemy nazwę obiektu i tyle.

# UWAGA !!!
# Oczywiście należy pamiętać, że importowane obiekty nie mogą się nazywać tak samo jak obiekty stworzone przez użytkownika w tym pliku do któ®ego importujemy obiekty z modułu.

# Przykład 6:
from Part6_module_third_way_my import trzeciSposob, ulubioneMotocykle # importowanie z modułu Part6_module_third_way_my dwa konkretne obiekty, funkcja trzeciSposob oraz słownik ulubioneMotocykle
trzeciSposob() # wywołanie funkcji trzeciSposob poprzez bezpośrednie podanie jego nazwy. Obiekt ten pochodzi z zaimportowanego wcześniej modułu Part6_module_third_way_my. Jednak obiekt ten zaimportowaliśmy w bezpośredni sposób Jednak obiekt ten zaimportowaliśmy w bezpośredni sposób i nie musimy się do niego odwoływać poprzez natację kropkową i nazwe modułu z którego pochodzi
print(ulubioneMotocykle["ekstra"]) # wyświetlenie wartości ze słownika którego kluczem jest "ekstra". Słownik został zaimportowany w sposób bezpośredni z modułu Part6_module_third_way_my

# Trzeci sposób importowania daje jeszcze jedną mozliwość.
# Jest to mieszny sposób DRUGI I TRZECI.

# Składnia rozwinięcia sposobu trzeciego:
# from myModuleFile import object1 as ob1, object2 as ob2

# Taki zapis powoduje, że bezpośrednio zaimportowanym obiektom nadajemy nazwy pomocniczne, alaisy.
# Powoduje to, że nie dość że do zaimportowanych obiektów będziemy odwoływać się bezpośrednio z pominięciem nazwy, pomocnicznej nazwy, aliasu modułu to będzie się do nich odnosić nie przez ich oryginalne nazywy, takie jakie zostały im zdefiniowane w pliku modułu
# tylko przez nazwy jakim im zostały przypisane czyli poprzez pomocniczne nazwy, aliasy.
# Pomocniczne nazwy to te które są po nazwie obiektu i po słówku "as".
# To tak jakby przypisanie nazwy obiektu do jakiejś zmiennej tylko odbywające się juz w trakcie importowania obiektów z pliku modułu.

# Przykład 7:
from Part6_module_third_B_way_my import trzeciSposobIB as functionFromModule3B, lampy as stringFromModule3B # importowanie z modułu Part6_module_third_B_way_my dwa konkretne obiekty, funkcja trzeciSposobIB oraz zmienną lampy którym zostały przypisane pomocniczne nazwy, aliasy, są to odpowiednio functionFromModule3B oraz stringFromModule3B
functionFromModule3B() # wywołanie funkcji trzeciSposobIB poprzez wywołanie jej pomocnicznej nazwy, aliasu functionFromModule3B, taka nazwa została nadana podczas importowania obiektów z pliku modułu
print(stringFromModule3B) # wyświetlenie zmiennej lampy poprzez wywołanie jej pomocnicznej nazwy, aliasu stringFromModule3B, taka nazwa została nadana podczas importowania obiektów z pliku modułu

# UWAGA !!!
# Bezpośrednie importowanie obiektów z modułów ułatwia późniejsze pisanie kodu jednakże ma sens wtedy kiedy ilość obiektów które chcemy zaimportować jest niewielka.
# Wynika to z tego, że w tym sposobie wypisujemy które obiekty chcemy zaimportować, więc jeżeli tych obiektów jest dużo to nie ma sensu wszystkie wypisywać.
# Jeżeli często będziemy używać różnych obiektów z modułu to warto zaimportować cały moduł, wszystkie jego obiekty.
# Możemy to zrobić stosując jeden z dwóch pierwszych sposobów importowania. Jednak to będzie wymagało odnoszenia się do obiektów z zaimportowaych modułów poprzez notację kropkową, tzn. po nazwię modułu lub pomocnicznej nazwie, aliasie podajemy nazwę obiektu.
# Kolejnym pomysłem na import wszystkich obiektów z modułu bez konieczności odnoszenia się do nich poprzez notację kropkową jest wykorzystanie składni sposobu trzeciego (from ... import ...)
# Wówczas będziemy się do nich odwoływać bezpośrednio poprzez nazwy jakie mają w pliku modułu.

# Składnia importowania wszystkich obiektów z pliku modułu:
# from myModuleFile import *

# Powyższa składnia powoduje, że z modułu importujemy wszystkie obiektu.
# Takie importowanie może wprowadzać pewien chaos do kodu. Ponieważ jeżeli bedziemy używać dużej ilości obiektów z zaimportowanego modułu
# to bez notacji kropkowej nie będzie wiadomo czy obiekty typu funkcje, listy, krotki itd zostały zdefiniowane i zaimportowane z modułu czy może zdefiniowane w tym pliku w który są używane.

# Przukłąd 8:
from Part6_module_third_C_way_my import *  # importowanie z modułu Part6_module_third_C_way_my wszystkie znajdujące się w nim obiekty
trzeciSposobIC() # wywołanie funkcji trzeciSposobIC poprzez bezpośrednie podanie jego nazwy. Obiekt ten pochodzi z zaimportowanego wcześniej modułu Part6_module_third_C_way_my. Jednak obiekt ten zaimportowaliśmy w bezpośredni sposób i nie musimy się do niego odwoływać poprzez natację kropkową i nazwe modułu z którego pochodzi
for item in ulubioneZwierzatka:  # wyświetlenie zawartości krotki wykorzystując pętlę for. Krotka została zaimportowany w sposób bezpośredni z modułu Part6_module_third_C_way_my
    print(item)
