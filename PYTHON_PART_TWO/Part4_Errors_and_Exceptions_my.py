#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/////////////////
#/////////////////
# Wyjątki i obsługa błędów

# W tym rozdziale poznamy obsługę błędów i wyjątków w Pythonie.

# Skoro dotarliśmy do omównia tematu związanego z obsługą błędów i wyjątkami,
# to znaczy, że przeszliśmy już przez wiele zagadnień związanych z programowaniem
# i na pewno spoktaliśmy się wystąpieniem błądu podczas uruchamiania napisanego przez nas programu.

# Na przykład:
# print('Hello)

# Przy próbie wykonania powyższego kodu otrzymujemy bardzo powszechny błąd jakim jest SyntaxError
# Jest to jeden z wielu typów problemów które możemy spotkać w trakcie programowania.
# Po dwukropku jest informacja EOL (End of Line). I jest to uszczegółowienie błędu typu SyntaxError.
# Oznacza to, że wystąpił błąd składnikowy, że w kodzie występuje błąd składniowy, który powoduje,
# że analizator składni, kompilator lub moduł wykonawczy nie są w stanie określić jaki jest zamiar kodu.
# Po prostu sugeruje nam, że źle zapisaliśmy polecenie w konkretnym położeniu kodu.
# Dodatkowo informacja EOL informuje, że coś brakuje na końcu kodu.
# Jest to dość szczegółowa i jasna informacja która pomoże w ustaleniu i naprawieniu błędu.

# Zrozumienie różnych typów błędów pozwala na dużo szybsze debugowanie kodu.

# Normalnie jeżeli wystąpi błąd w naszym kodzie to program jest zatrzymywany i jak już powyżej opisaliśmy
# zostanie wygenerowany błąd.

# Każdy typ błędu zwracany ma swój wyjątek.
# Wyjątek to konstrukcja która pozwala działać i wykonywać poprawnie inne instrukcje programu,
# nawet jeżeli wystąpi błąd w programie który dotyczy użytego wyjątku.
# To pozwala na kotrolowane występowania błędów przy pomocy wyjątków,
# dzięki którym błędy te nie deklasują poprawności działania programu.

# Są wyjątki konkretne, dla konkretnych błędów i wyjątki ogólne, po prostu jak jakikolwiek błąd wystąpi.

# Cała lista wyjątków znajduje się pod tym adresem:
# https://docs.python.org/3/library/exceptions.html

#/////////////////
#/////////////////
# Konstrukcja: try | except | else

# Podstawową składnią do obsługi błędów jest try | except.
# W bloku try umieszczony jest kod który może spowodować błąd (stąd nazwa tego bloku, try - spróbuj wykonać kod)
# Natomiast w bloku except jest umieszczony kod który zostanie wykonany zamiast tego który znajduje się w bloku try w momencie jeżeli wystąpi w nim błąd.
# (stąd nazwa tego bloku, except - zamiast). Blok except może być szczegółowy, dotyczący konkretnego problemu,
# bądź ogólny, po prostu jeżeli jakikolwiek błąd wystąpi.
# Jeżeli wiemy, że nasz kod może powodować kilka różnych błędów to wówczas możemy stosować kilka bloków except do jednego bloku try.

# Oprócz bloków try | except, jest również inny ciekawy blok dla obsługi błędów, a mnianowicie else.
# Działa on na podobnej zasadzie co w wyrażeniu warunkowym.
# Jednak w przypadku obsługi błędów to kod zapisany w tym bloku zostanie wywołany, jezeli kod z bloku try nie zwróci błędów (stąd nazwa tego bloku, else - jeszcze, oprócz ten kod też będzie wykonany).
# Co oznacza, że kod z bloku try jeżeli nie zwróci błędu to będzie wykonany a zaraz po nim będzie wykonany też kod z bloku else (chyba, że wystąpi błąd to wówczczas zostanie wykonany tylko kod z bloku except).
# Kod z bloku else jest dodatkowo wykonywany. Może służyć w celach informacyjnych itp.

# Składnia:
#     try:
#        Piszemy tutaj nasz kod, który może wywoływać błędy
#        ...
#     except:
#        Ogólny wyjątek, jeżeli po prostu kod z bloku try zwróci jakikolwiek błąd to ten kod zostanie wykonany
#        ...
#     except ExceptionI:
#        Wyjątek szczegółowy, jeżeli kod z bloku try zwróci błąd typu ExceptionI, to wówczas ten kod zostanie wykonany
#        ...
#     except ExceptionII:
#        Wyjątek szczegółowy, jeżeli kod z bloku try zwróci błąd typu ExceptionII, to wówczas ten kod zostanie wykonany
#        ...
#     else:
#        Kod który zostanie wykonany jeżeli kod z bloku try nie zwróci błędu. Należy pamiętać, że kod z bloku try jeżeli nie wywołuje błędu to jest wykonywany na początku a zaraz po nim jest wykonywany kod z bloku else
#        ...

# Dla lepszego zrozumienia poniżej zostaną wykonane pomocne przykłady.

# Przykład 1:
# Wczytamy plik w trybie do zapisu (jest to równoznaczne z tym, że jeżeli ten plik nie istnieje to zostanie utworzony),
# a następnie dodamy do niego linię tekstu. Kod ten umieścimy w bloku try.
# W bloku szczegółowym except umieścimy informację na wypadek gdyby wystąpił błąd podczas wczytywania pliku.

try: # blok try, ten blok z kodem zostanie wykonany, jeżeli wewnątrz tego bloku kod nie spowoduje błędu
    f = open('Part4_Error_Exceptions_file','w') # wczytanie pliku z możliwością zapisu, opcja "w" oznacza, że to co w pliku już było zostanie zastąpione przez nową zawartość
    f.write('Test write this') # dodanie do pliku nowego wiersza z tekstem, który zastąpi wszystko co było już w pliku
    print("Stworzono nowy plik oraz zapisano w nim nową zawartość - przykład 1, kod z bloku try") # zwrócenie informacji na ekran o poprawności wczytania i zapisania pliku
except IOError: # blok except ze szczegółowym błędem, dotyczącym niemożnoci otwarcia pliku, ten blok zostanie wykonany, jeżeli w bloku try kod tam istniejący spowoduje określony błąd
   print("Błąd, nie można wczytać bądź odnaleźć pliku - przykład 1, kod z bloku except") # zwrócenie konkretnej informacji na ekran jeżeli kod z bloku try spowoduje błąd

# Przykład 2:
# Przykład identyczny jak przykład 1, jednak z tą różnicą, że dodany został blok else, w którym umieściliśmy informację która zostanie wyświetlona zaraz po wykonaniu kodu z bloku try,
# oczywiści jeżeli kod z bloku try nie spowoduje błędu.

try: # blok try, ten blok z kodem zostanie wykonany, jeżeli wewnątrz tego bloku kod nie spowoduje błędu
    f = open('Part4_Error_Exceptions_file','w') # wczytanie pliku z możliwością zapisu, opcja "w" oznacza, że to co w pliku już było zostanie zastąpione przez nową zawartość
    f.write('Test write this') # dodanie do pliku nowego wiersza z tekstem, który zastąpi wszystko co było już w pliku
    print("Stworzono nowy plik oraz zapisano w nim nową zawartość - przykład 2, kod z bloku try") # zwrócenie informacji na ekran o poprawności wczytania i zapisania pliku
except IOError: # blok except ze szczegółowym błędem, dotyczącym niemożnoci otwarcia pliku, ten blok zostanie wykonany, jeżeli w bloku try kod tam istniejący spowoduje określony błąd
   print("Błąd, nie można wczytać bądź odnaleźć pliku - przykład 2, kod z bloku except") # zwrócenie konkretnej informacji na ekran jeżeli kod z bloku try spowoduje błąd
else: # blok else, ten blok z kodem zostanie wykonany, jeżeli kod w bloku try nie spowoduje błędu, kod w else zostanie wykonany zaraz po kodzie z bloku try
   print("Wczytano poprawnie zawartość nowego pliku - przykład 2, kod z bloku else") # zwrócenie konkretnej informacji na ekran jeżeli kod z bloku try zostanie wykonany, czyli nie zwróci błędu
   f.close() # zamknięcie pliku

# Przykład 3:
# Dalej opieramy się na przykładzie 1 z tą różnicą, że teraz wczytamy plik w trybie tylko do odczytu,
# a następnie będziemy próbować zapisać w nim nową zawartość. Kod ten umieścimy w bloku try.
# Oczywiste jest, że zostanie zwrócony błąd. Nie można otworzyć pliku w trybie tylko do odczytu i próbować zapisać w nim nową zawartość.
# W bloku szczegółowym except, obslugującym konkretny błąd typu IOError, umieścimy informację która zostanie wyświetlona w momencie jak wystąpił błąd podczas wczytywania pliku w trybie tylko do odczytu i próbie zapisania do niego nowej informacji.

try: # blok try, ten blok z kodem zostanie wykonany, jeżeli wewnątrz tego bloku kod nie spowoduje błędu
    f = open('Part4_Error_Exceptions_file','r') # wczytanie pliku tylko do odczytu, opcja "r" oznacza, że możemy tylko odczytywać dane z pliku, ale nic nie możemy w nim zapisywać
    f.write('Test write this') # próba dodania do pliku nowego wiersza z tekstem, który zastąpiłby wszystko co było już w pliku, ale wiemy, że to spowoduje wywołanie błędu bo plik został wczytany tylko do odczytu
    print("Stworzono nowy plik oraz zapisano w nim nową zawartość - przykład 3, kod z bloku try") # zwrócenie informacji na ekran o poprawności wczytania i zapisania pliku, jeżeli kod byłby poprawny
except IOError: # blok except ze szczegółowym błędem, dotyczącym niemożnoci otwarcia pliku, ten blok zostanie wykonany, jeżeli w bloku try kod tam istniejący spowoduje określony błąd
   print("Błąd, nie można wczytać bądź odnaleźć pliku - przykład 3, kod z bloku except") # zwrócenie konkretnej informacji na ekran jeżeli kod z bloku try spowoduje błąd
else: # blok else, ten blok z kodem zostanie wykonany, jeżeli kod w bloku try nie spowoduje błędu, kod w else zostanie wykonany zaraz po kodzie z bloku try
   print("Wczytano poprawnie zawartość - przykład 3, kod z bloku else") # zwrócenie konkretnej informacji na ekran jeżeli kod z bloku try zostanie wykonany, czyli nie zwróci błędu, ale jak wiemy w tym przykładzie ten blok nie zostanie wywołany
   f.close() # zamknięcie pliku

# Przykład 4:
# Ten przykład to nic innego jak przykład 3 tylko przerobiliśmy blok except.
# W tym przykładzie użyliśmy ogólnego except, w związku z czym blok ten nie obsługuje już konkretnego typu błędu tylko wszystkie.
# Niezależnie jaki błąd się pojawi w kodzie w bloku try, to i tak kod z bloku except zostanie wykonany.
# We wcześniejszych przykładach musiał pojawić się błąd szczególnego typu aby blok except został wykonany. Jeżeli ten szczegółowy błąd się by nie pojawił ale jakiś inny to except nie zostałoby wywołane i program by się zatrzymał i zwróciłby błąd.
# Dodatkowo w tej wersji naszego przykładu usunęliśmy blok else.

try: # blok try, ten blok z kodem zostanie wykonany, jeżeli wewnątrz tego bloku kod nie spowoduje błędu, jak wiemy spowoduje
    f = open('Part4_Error_Exceptions_file','r') # wczytanie pliku tylko do odczytu, opcja "r" oznacza, że możemy tylko odczytywać dane z pliku, ale nic nie możemy w nim zapisywać
    f.write('Test write this') # próba dodania do pliku nowego wiersza z tekstem, który zastąpiłby wszystko co było już w pliku, ale wiemy, że to spowoduje wywołanie błędu bo plik został wczytany tylko do odczytu
    print("Stworzono nowy plik oraz zapisano w nim nową zawartość - przykład 4, kod z bloku try") # zwrócenie informacji na ekran o poprawności wczytania i zapisania pliku, jeżeli kod byłby poprawny
except: # blok except ogólny, nie dotyczącym jakiegoś szczególnego typu błędu, jeżeli w bloku try kod tam istniejący spowoduje jakikolwiek błąd to zostanie z bloku except wykonany kod
   print("Błąd, nie można wczytać bądź odnaleźć pliku - przykład 4, kod z bloku except") # zwrócenie konkretnej informacji na ekran jeżeli kod z bloku try spowoduje błąd

# Dzięki ogólnemu bloku except nie musimy zapamiętywać szczegółowych typów błędów.
# Użycie oolnego bloku except zawsze pomoże.
# Oczywiście mogą być okoliczności które będą wymagać użycia szczególowego bloku except.
# To już będzie zależne od sytuacji.

#/////////////////
#/////////////////
# Konstrukcja: finally

# Jest jeszcze jeden rodzaj bloku, a mianowicie: finally

# Działa on na podobnej zasadzie co blok else.
# W przypadku bloku else to był on wywoływany jeżeli kod z bloku try został wykonany. Jeżeli wystąpi tam błąd to wówczas wykonywany jest kod z bloku except a co za tym idzie kod z bloku else nie będzie wywoływany.
# W przypadku bloku finally kod w nim zawarty zostanie wykonany niezależnie czy kod z bloku try zostanie wykonany czy w wyniku błędu zostanie wykonany kod z bloku except (ogólnego bądź szczegółowego).
# Oznacza to kod z bloku finally zawsze będzie wykonany i zawsze na samym końcu konstrukcji obsługi błędów. Wcześniej zostanie wykonany kod z bloku try (jeżeli nie zwróci błędu), bądź z bloku except (jeżeli kod z bloku try zwróci błąd).

# Składnia:
#     try:
#        ...
#     except:
#        ...
#     finally:
#        Kod który zostanie wykonany zawszne niezależnie czy kod z bloku try zwróci błąd czy nie

# Przykład 5:

# Wczytamy plik w trybie do zapisu (jest to równoznaczne z tym, że jeżeli ten plik nie istnieje to zostanie utworzony),
# a następnie dodamy do niego linię tekstu. Kod ten umieścimy w bloku try.
# W bloku ogólnym except umieścimy informację na wypadek gdyby wystąpił błąd podczas wczytywania pliku.
# Na końcu dodamy blok finally który zostanie wywołany niezależnie czy kod z bloku try zostanie wykonany czy zwróci błąd i zostanie wykonany kod z bloku except.
# W tym przykładzie kod z bloku try nie zwróci błędu a wiec kod z tego bloku zostanie wykonany, a następnie zostanie wykonany kod z bloku finally.

try: # blok try, ten blok z kodem zostanie wykonany, jeżeli wewnątrz tego bloku kod nie spowoduje błędu, jak wiemy nie spowoduje
   f = open("Part4_Error_Exceptions_file", "w") # wczytanie pliku z możliwością zapisu, opcja "w" oznacza, że to co w pliku już było zostanie zastąpione przez nową zawartość
   f.write("Test write statement") # dodanie do pliku nowego wiersza z tekstem, który zastąpi wszystko co było już w pliku
   print("Stworzono nowy plik oraz zapisano w nim nową zawartość - przykład 5, kod z bloku try") # zwrócenie informacji na ekran o poprawności wczytania i zapisania pliku
except: # blok except ogólny, nie dotyczącym jakiegoś szczególnego typu błędu, jeżeli w bloku try kod tam istniejący spowoduje jakikolwiek błąd to kod z bloku except zostanie wykonany
    print("Błąd, nie można wczytać bądź odnaleźć pliku - przykład 5, kod z bloku except") # zwrócenie konkretnej informacji na ekran jeżeli kod z bloku try spowoduje błąd
finally: # blok finally, ten blok z kodem zostanie wykonany, niezależnie czy kod z bloku try spowoduje błąd czy też nie, kod w bloku finally zostanie wykonany zaraz po kodzie z bloku try (jeżeli nie wystapi błąd) bądź po kodzie z bloku except (jeżeli wystapi błąd)
   print("Nie zależnie od tego czy plik został poprawnie wczytayn czy wystapił błąd ten komunikat zawsze się wyświetli - przykład 5, kod z bloku finally") # zwrócenie konkretnej informacji na ekran niezlaeżnie czy zostanie wykonany kod z bloku try czy bloku except

# Przykład 6

# Dalej opieramy się na przykładzie 6 z tą różnicą, że teraz wczytamy plik w trybie tylko do odczytu,
# a następnie będziemy próbować zapisać w nim nową zawartość. Kod ten umieścimy w bloku try.
# Oczywiste jest, że zostanie zwrócony błąd. Nie można otworzyć pliku w trybie tylko do odczytu i próbować zapisać w nim nową zawartość.
# W bloku ogólnym except, umieścimy informację która zostanie wyświetlona w momencie jak wystąpił błąd podczas wczytywania pliku w trybie tylko do odczytu i próbie zapisania do niego nowej informacji.
# Na końcu dodamy blok finally który zostanie wywołany niezależnie czy kod z bloku try zostanie wykonany czy zwróci błąd i zostanie wykonany kod z bloku except.
# W tym przykładzie kod z bloku try zwróci błąd, a zatem zostanie wykonany kod z bloku except, a następnie zostanie wykonany kod z bloku finally.

try: # blok try, ten blok z kodem zostanie wykonany, jeżeli wewnątrz tego bloku kod nie spowoduje błędu, jak wiemy spowoduje
   f = open("Part4_Error_Exceptions_file", "r") # wczytanie pliku tylko do odczytu, opcja "r" oznacza, że możemy tylko odczytywać dane z pliku, ale nic nie możemy w nim zapisywać
   f.write("Test write statement") # próba dodania do pliku nowego wiersza z tekstem, który zastąpiłby wszystko co było już w pliku, ale wiemy, że to spowoduje wywołanie błędu bo plik został wczytany tylko do odczytu
   print("Stworzono nowy plik oraz zapisano w nim nową zawartość - przykład 6, kod z bloku try") # zwrócenie informacji na ekran o poprawności wczytania i zapisania pliku, jeżeli kod byłby poprawny
except: # blok except ogólny, nie dotyczącym jakiegoś szczególnego typu błędu, jeżeli w bloku try kod tam istniejący spowoduje jakikolwiek błąd to kod z bloku except zostanie wykonany
    print("Błąd, nie można wczytać bądź odnaleźć pliku - przykład 6, kod z bloku except") # zwrócenie konkretnej informacji na ekran jeżeli kod z bloku try spowoduje błąd
finally: # blok finally, ten blok z kodem zostanie wykonany, niezależnie czy kod z bloku try spowoduje błąd czy też nie, kod w bloku finally zostanie wykonany zaraz po kodzie z bloku try (jeżeli nie wystapi błąd) bądź po kodzie z bloku except (jeżeli wystapi błąd)
   print("Nie zależnie od tego czy plik został poprawnie wczytayn czy wystapił błąd ten komunikat zawsze się wyświetli - przykład 6, kod z bloku finally") # zwrócenie konkretnej informacji na ekran niezlaeżnie czy zostanie wykonany kod z bloku try czy bloku except

#/////////////////
#/////////////////
# Tworzenie własnych wyjątków, błędów

# Powyżej przedstawione zostało jak rodzić sobie z występującymi błędami podczas działania programów oraz tworzeniem wyjątków do ich obsługi.

# W tym rozdziale przedstawiona zostanie funkcjonalność Pythona, która pozwala programiście na stworzenie własnych, indywidualnych błędów, wyjątków jakie mają zostać wyświetlone użytkownikowi jeżeli spełniony zostanie określony warunek. Spełnienie określonego warunku wymaga zastosowania wyrażenia warunkowego if.
# Takie własne, indywidualne błędy, wyjątki są tworzone tylko w konkretnym kodzie programu. Są stworzone przez programistę więc dotyczą tylko tego jednego programu przez niego napisanego. Są to błędy, wyjątki spersonalizowane a więc inne niż te domyślnie występujące w Pythonie.

# Oczywiście tak jak w przypadku domyślnych błędów i wyjątków Pythona tak w przypadku naszych własnych, indwywidualnych błędów, wyjątków program się zatrzyma i zwróci błąd, wyjątek. Program dalej nie będzie wykonywany.

# Aby stwprzyć jakiś własny wyjątek należy połączyć go z wyrażeniem warunkowym. Dzięki temu, jeżeli warunek zostanie spełniony to wówczas pojawi się nasz własny wyjątek.
# Tworzenie własnych wyjątków wymaga połączenia ich z wyrażeniem warunkowym, ponieważ Python nie wie kiedy my byśmy chcieli aby taki wyjatek został wyświetlony. Dlatego potrzebuje warunku.
# W przypadku domyślnych wyjątków Pythona to on ma to już wbudowane. W przypadku naszych wyjątków to my musimy mu pokazać kiedy mają zostac wyświetlone.
# W konstrukcji wyjątku w nawiasie zawsze podajemy informację dla użytkownika opisującą wyświetlony wyjątek. Dzięki temu użytkownik wie co zostało błędnie zrobione.

# Konstrukcja tworzenia wyjątku:
# if condition:
#   raise Exception("information about exception")

# Przykłąd 7:

# Stworzymy wyrażenie if które będzie sprawdzać czy zmienna jest mniejsza od zera.
# Jeżeli zmienna będzie mniejsza od zera to program zostanie zatrzymany i wyświetlony zostanie wyjątek z konkretną informacją dla użytkownika.

x = -1 # deklaracja zmiennej x
if x < 0: # wyrażenie warunkowe, zostanie ono spełnione jeżeli zmienna x będzie mniejsza niż 0
    raise Exception("Zmienna powinna mieć wartość powyżej zera") # jeżeli warunek zostanie spełniony to program się zatrzyma i zwrócony zostanie wyjątek z informacją ujętą po rise.

# Aby stworzyć jakiś własny błąd konkretnego typu również musimy go połączyć z weniem warunkowym. Dzięki temu, jeżeli warunek zostanie spełniony to wówczas pojawi się typ błędu jaki chcemy. Nawet jeżeli nie jest on związany z warunkiem (w sensie logicznym, na przykład błąd SyntaxError dla warunku x < 0, dla x = -1)
# Tworzenie własnych błędów konkretnego typu wymaga połączenia ich z wyrażeniem warunkowym, ponieważ Python nie wie kiedy my byśmy chcieli aby taki błąd został wyświetlony. Dlatego potrzebuje warunku.
# W przypadku domyślnych błędów szczegółowych Pythona to on ma to już wbudowane. W przypadku naszych błędy szczegółowe to my musimy mu pokazać kiedy mają zostać wyświetlone.
#  konstrukcji błędu w nawiasie zawsze podajemy informację dla użytkownika opisującą wyświetlony błąd szczegółowy. Dzięki temu użytkownik wie co zostało błędnie zrobione.

# Konstrukcja tworzenia własnego błędu określonego typu:
# if condition:
#   raise ERROR_TYPE("error description")

# Przykład 8:

# Stworzymy wyrażenie if które będzie sprawdzać czy zmienna jest typu integer.
# Jeżeli zmienna nie będzie typu integer to program zostanie zatrzymany i wyświetlony zostanie błąd typu TypeError z konkretną informacją dla użytkownika.

y = "Tomek" # deklaracja zmiennej y
if not type(y) is int: # wyrażenie warunkowe, zostanie ono spełnione jeżeli rodzaj zmiennej y nie będzie liczbą całkowitą
    raise TypeError("Zmienna przyjmuje tylko liczby całkowite") # jeżeli warunek zostanie spełniony to program się zatrzyma i zwrócony zostanie błąd typu TypeError z konkretną informacją ujętą po rise.
