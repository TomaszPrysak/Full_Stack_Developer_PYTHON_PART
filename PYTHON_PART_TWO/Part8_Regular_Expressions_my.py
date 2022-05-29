#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/////////////////
#/////////////////
# Wyrażenia regularne

# Wyrażenia regularne (zwane też RegEx, regex — od angielskiego wyrażenia regular expressions)
# to wzorce, dzięki którym możemy sprawdzać czy jakiś ciąg znaków (np. taki, który odczytamy od użytkownika)
# ma określony przez nas format (np. czy może być datą). Czyli mówiąc prościej najczęściej spotkamy się z nimi,
# przy walidacji danych wprowadzanych przez użytkowników czy to w formie danych wypełnianych w formularzu czy to,
# w formie wpisywania linku strony internetowej w przeglądarce.
# Jednak nie jest to ich jedyne zastosowanie, za ich pomocą możemy odnaleźć wzorzec w tekście,
# pociąć tekst na fragmenty, czy też zamienić tekst zgodny ze wzorcem na inny.

# Wyrażenie regularne lub wyrażenia regularne to sekwencja znaków tworzących wzorzec wyszukiwania.
# Te wzorce służą do sprawdzania, czy dany, sprawdzany ciąg znaków wpisuje się w ten określony wzorzec wyszukiwania.

# Otóż wyrażenia regularne są opisem jakiegoś ciągu znaków. Taki opis nazywamy wzorcem.
# Co właściwie znaczy, że wyrażenia regularne są opisem jakiegoś ciągu znaków ?
# Wyobraźmy sobie, że dostajesz zadanie opisania jak wygląda kod pocztowy np. 00-935. Co powiesz ?
# Mój opis by mówił: “Kod pocztowy składa się z 6 znaków, dwie cyfry, myślnik, trzy cyfry”.
# Taki słowny opis musimy zamieniać na opis zdolny do przeczytania przez komputer.
# Do tego służą wyrażenia regularne.
# Wzorzec zapisu kodu pocztowego wg. wyrażenia regularnego mógłby wyglądać następująco:

# Przykład 1: \d\d-\d\d\d
# Przykłąd 2: [0-9]{2}-[0-9]{3}
# Przykłąd 3: \d{2}-\d{3}

# Jak widać zapis kodu pocztowego w postaci wzorca zapisanego wyrażeniem regularnym można stworzc na kilka różnych sposobów.
# Dlatego ważne jest aby podczas tworzenia takiego wzorac dobrać takie wyrażenie regularne które w miare możliwości
# będzie jak najlepiej opisywać szukaną, porównywaną, sprawdzaną frazę tekstu.

# Python ma wpudowany moduł "re" który służy do pracy z wyrażeniami regularnymi.
# Oczywiście moduł ten trzeba uprzednio zaimportować.

import re

# Wzorcem może być też zwykłe słowo. Jednakże wówczas nie trzebaby stosować modułu
# wykorzystującego wyrażenia regularne do efektywnego przeszukiwania, sprawdzania, porównywania tekstu.

#/////////////////
#/////////////////
# Funkcje modułu RegEx

# Moduł re do pracy z wyrażeniami regularnymi w pythonie posiada zestaw funkcji
# pozwalających wyszukiwać ciąg znaków wg. zadanego wzorca w zależności od wymaganego w danym
# momencie zastosowania.

# W zależności od tego co chcemy znaleźć wg. wzorca wykorzystując wyrażenie regularnie możemy skorzystać
# z czterech funkcy modułu re.

#/////////////////
# re.findall()

# Funkcja ta zwraca listę wszystkich wystąpień wzoraca w przeszukiwanym tekście.
# Kolejność wystąpień w liście będzie zależna od miejsca ich obecności w przeszukiwanym tekście.
# Pierwszym (posiadającym indeks zero) elementem listy będzie wystąpieni które jako pierwsze zostało znalezione w przeszukiwanym tekście.
# Dugiem (z indeksem jeden) elementem listy będzie wystąpienie które zostało znalezione jako drugie z kolei.
# I tak dalej.
# Wystąpienia znajdujące się w liście zawsze będą dokładnie dopasowane do wzorca.

# Jeżeli w przeszukiwanym tekście nie zostanie znaleziony wzorzec wówczas lista będzie pusta.

# Składnia:
# re.findall("wzorzec", "przeszukiwany tekst")

# Jak najabardziej jako argumentami tej funkcji mogą być zmienne. To tak oczywiste w programowaniu, że nie wiem po co to pisze.

# Przykład 1:
txtE1 = "To jest topaz w torsie" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca
print(re.findall("to", txtE1)) # wyświetlenie listy zwracanej przez funkcję re.findall() gdzie szukanym wzorcem jest string "to",
                               # natomiast przeszukiwanym tekstem, w celu poszukiwania wzorca, jest zmienna tekstowa txtE1.
                               # Lista zawiera dwa elementy "to" zgodne ze wzorcem pochodzące ze słów "topaz" oraz "torsie"

# Przykład 2:
txtE2 = "Kot ma Kaczynskiego" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca
print(re.findall("Ala", txtE2)) # wyświetlenie listy zwróconej przez funkcję re.findall() gdzie szukanym wzorcem jest string "Ala",
                                # natomiast przeszukiwanym tekstem, w celu poszukiwania wzorca, jest zmienna tekstowa txtE2.
                                # Lista jest pusta ponieważ wzorzec "Ala" nie jest znaleziony w przeszukiwanym tekście

#/////////////////
# re.search()

# Funkcja ta zwraca obiekt typu Match jeżeli w przeszukiwanym tekście zostanie znaleziony wzorzec.
# Funkcja zawsze będzie szukać dokładnego dopasowania do wzorca.
# Jeżeli zostanie znalezione więcej niż jedno dopasowanie, wówczas zwrócone zostanie tylko pierwsze dopasowanie.

# Jeżeli funkcja nie znajdzie żadnego dopasowania do wzorca wówczas zwóci wartość None

# Sładnia:
# re.search("wzorzec", "przeszukiwany tekst")

# Jak najabardziej jako argumentami tej funkcji mogą być zmienne. To tak oczywiste w programowaniu, że nie wiem po co to pisze.

# Przykład 3:
txtE3 = "Na Nowogrodzkiej czai sie zlo" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca
print(re.search("\s", txtE3)) # wyświetlenie obiektu typu Match zwracanego prez funkcję re.search() zawierającego znalezione dopasowanie do wzorca.
                              # Wzorcem jest symbol "\s" oznaczający w wyrażeniu regularnym spację.
                              # Przeszukiwanym tekstem, w celu poszukiwania wzorca, jest zmienna tekstowa txtE3.
                              # W tekście przeszukiwanym są cztery spacje, jednak zwrócony obiekt Match,
                              # będzie dotyczył pierwszego wystąpienia dopasowania spacji, czyli spacji pod indeksem dwa z
                              # przeszukiwanego wzorca.

# Przykłd 4:
txtE4 = "Samoloty loty loty" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca
print(re.search("\d", txtE4)) # wyświetlenie wartości None ponieważ w przeszukiwanym stringu nie zostało znalezione
                              # dopasowanie do wzorca: "\d". Wzorzec ten oznacza występowanie dowolnej cyfry z przedziału 0-9.
                              # Przeszukiwanym tekstem, w celu poszukiwania wzorca, jest zmienna tekstowa txtE4.

# Opisywana funkcja re.search() w przypadku znalezienia dopasowania wzorca zwraca obiekt typu Match.
# Obiekt ten jest czymś więcej niż tylko swego rodzaju wartością logiczną informującą nas w przypadku wystąpienia czy dopasowanie się powiodło czy nie.
# Jeżeli dopasowanie nie zostanie znalezione to otrzymamy wartość None zamiast obiektu typu Match.
# Obiekt ten zawiera informacje o wyszukiwaniu i jego rezultatach. Zwracana informacja po wykonaniu funkcji re.search() składa się z trzech części:

# <re.Match object; span=(2, 3), match=' '> - informacja zwrócona z Przykładu 3.

# re.Match object - ta część informuje o tym, że jest to obiekt typu Match, powstał on w wyniku znalezienia dopasowania do wzoraca
                # - oraz umieszczony jest tutaj oryginalny string z przeszukiwanym tekstem.
                # - Informacja zwrócona z Przykładu 3.
                # - Potwierdzeniem rodzaju obiektu zwracanego przez funkcję re.search() jest użycie metody type(), jak na poniższym przykładzie:

outputE3 = re.search("\s", txtE3) # przypisanie do zmiennej wyniku działania funkcji re.search()
print(type(outputE3)) # sprawdzenie typu obiektu będącego wynikiem działąnia funkcji re.search().
                      # Informacją zawracaną przez type() w tym wypadku jest: <class 're.Match'>, co dokładnie nas informuje o tym, że obiekty zwracane przez funkcję re.search() to obiekty typu Match.

# span=(2, 3) - ta część informuje o miejsu wystąpienia pierwszego dopasowania do wzorca, ponieważ jak wiemy funkcja re.search() zwraca pierwsze wystąpienie dopasowane do wzorca.
            # - infomacja ta jest zbudowana w ten sposób, że pierwszą cyfrą jest indeks oznaczaący początek naszego wystąpniena w tekście przeszukiwanym, natomiast druga cyfa informuje o zakresie jaki zamuje znaleziony wzorzec.
            # - Przy czym należy pamiętać, że druga cyfra oznacza koniec naszego wystąpienia, czyli indeks końcowy naszego wystąpienia w tekście przeszukiwanym, ale UWAGA tak jak w przypadku operacji na stringach ;) jest to znak graniczny nie brany pod uwagę.
            # - A więc w powyższym przypadku pierwsze wystąpienie wzorca jest pomiędzy indeksami 2  oraz 3 (indeks 3 jest granicą która nie jest brana pod uwagę), a więc dopasowanie do wzorca wystepuje pod indeksem 2 przeszukiwanego tekstu,
            # - Jeżeli wzorzec byłby dłuższy i by zostało znalezione do niego dopasowanie to zakres byłby odpowiednio dłuższy.
            # - Informacja zwrócona z Przykładu 3.

# match=' ' - ta część informuje o użytym wzorcu, wyrażeniu regularnym do przeszukiwania tekstu.
          # - W tym wypadku spacja zgadza się z użytym przez nas wyrażeniem regularnym, tj.: "\s".
          # - Informacja zwrócona z Przykładu 3.

# Obiekt typu Match ma właściwości i metody używane do pobierania informacji o wynikach wyszukania dopasowania.
# Są to następujące metod:

# .start() - zwraca indeks oznaczaący początek tylko i wyłącznie pierwszego dopasowanego w tekście przeszukiwanym zgodnie z funkcją re.search() jaką użyliśmy do przeszukiwania tekstu wg. wzorca
# .end() - zwraca indeks oznaczający zakres tylko i wyłącznie pierwszego dopasowanego, czyli indeks końcowy naszego pierwszego wystąpienia w tekście przeszukiwanym z funkcją re.search() jaką użyliśmy do przeszukiwania tekstu wg. wzorca.
       # - UWAGA tak jak w przypadku operacji na stringach ;) jest to znak graniczny nie brany pod uwagę.
# .span() - zwraca krotkę dwuelementową, której pierwszym elementem jest indeks oznaczający początek pierwszego dopasowania (patrz metoda .start()), a drugim elementem jest indeks oznaczający koniec pierwszego dopasowania (patrz metoda .end())
# .string - zwraca oryginalny tekst będący tekstem przeszukiwanym w celu dopasowania wzorca, inaczej mówiąc tekst przekazany do funkcji re.search()
# .group() - zwraca tekst będący wzorecem dopasowania należącym do konkretnej grupy.

# UWAGA jeżeli wzorzec nie został odnaleziony w tekście to cała funckja re.search() zwróci wartość None. A więc powyższe metody i właściwości będą zwracać błędy ponieważ nie funkcja re.search() nie zwróci obiektu typu Match na którym powyższe metody i właściwości działąją.

# Przykład 5:
print(re.search("\s", "Na Nowogrodzkiej czai sie zlo").start()) # wyświetla indeks początkowy dopasowanego wystąpienia wg. wzorca użytego w funkcji re.search() na której metoda start() została wywołana
print(re.search("\s", "Na Nowogrodzkiej czai sie zlo").end()) # wyświetla indeks końcowy dopasowanego wystąpienia wg. wzorca użytego w funkcji re.search() na której metoda end() została wywołana.
                                                              # UWAGA tak jak w przypadku operacji na stringach ;) jest to znak graniczny nie brany pod uwagę.
print(re.search("\s", "Na Nowogrodzkiej czai sie zlo").span()) # wyświetla krotkę dwuelementową, zawierającą indeks początkowy dopasowanego wystąpienia wg. wzorca oraz indeks końcowy dopasowanego wystąpienia wg. wzorca użytego w funkcji re.search() na której metoda .span() została wywołana.
print(re.search("\s", "Na Nowogrodzkiej czai sie zlo").string) # wyświetla tekst jaki był przeszukiwany w celu znalezienia dopasowania do wzorca użytego w funkcji re.search() na której właściwość .string została użyta.
print(re.search("cza", "Na Nowogrodzkiej czai sie zlo").group()) # wyświetla tekst będący wzorecem dopasowania szukanym w przeszukiwanyn tekście który został użyty w funkcji re.search() na którym metoda .group() została użyta.

# Najprościej jest stworzyć zmienną do której przypiszemy wynik działania funkcji re.search() i następnie wykorzystując notację kropkową wywołamy te dodatkowe metody

#/////////////////
# re.split()

# Funkcja ta najpierw wyszukuje w przeszukiwanym tekście dopasowanie według zadanego wzorca.
# Następnie wzorzec ten słuzy do podziału tekstu na mniejsze elementy typu string.
# Ilość tych elementów jest zależna od ilości znalezionych dopasowań do wzorca.
# Jeżeli zostanie znaleziony jeden wzorzec wówczas cały przeszukiwany tekst zostanie podzielony na dwa mniejsze elementy typu string.
# Czyli na elementy po lewej i po prawej stronie dopasowanego wzorca. Analogicznie jeżeli zostaną znalezione dwa dopasowania wówczas przeszukiwany tekst zostanie podzielony na trzy elementy. I tak dalej.
# Elementy typu string będące wynikiem podziału przeszukiwanego tekstu nie będą zawierać wzorca. Wzorzec jest elementem podziału nie wchodzącym w skłąd elementów wynikowych.
# Nastepnie elementy te zostają umieszczone w liście. Pierwszym elementem tej listy (o indeksie zero) będzie część przeszukiwanego tekstu która była po lewej stronie pierwszego znalezionego dopasowania wzorca będącego elementem podziału. I tak dalej.
# Dopasowania do wzorca będące elementami podziału nie zawierają się w żadnym z elementów listy.

# Podsumowując funkcja re.search() zwraca listę elementów typu string będących wynikiem podziału przeszukiwanego tekstu gdzie elementem podziału był wzorzec.
# Funkcja ta działa bliźniaczo do zwykłej funkcji split() wykonanej na jakimkolwiej stringu.

# Sładnia:
# re.split("wzorzec", "przeszukiwany tekst")

# Przykład 5:
txtE5 = "Motocykle to cos co jest cudowna rzecza" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca
print(re.split("co", txtE5)) # wyświetlenie listy zwracanej przez funkcję re.split() gdzie elementem podziału jest wzorzec "co".
                             # natomiast przeszukiwanym tekstem, w celu poszukiwania wzorca, jest zmienna tekstowa txtE5.
                             # Zwrócona lista posiada trzy elementy, ponieważ znaleziono dwa dopasowania do wzorca będącego elementem podziału.
                             # Te dwa elementy dzielą przeszukiwany tekst na trzy elementy typu string umieszczone w liście w kolejności ich występowania w tekście przeszukiwanym.
                             # Dopasowania do wzorca będące elementami podziału nie zawierają się w żadnym z elementów listy.
                             # Elementy podziału są wykorzystywane tylko i wyłącznie do podziału.

# Ciekawym, dodatkowym, nie wymaganym parametrem w funkcji re.split() jest możliwość określenia limitu poszukiwań wzorca jako elementu podziału przeszukiwanego tekstu.
# Wówczas jeżeli w przeszukiwanym tekście jest więcej dopasowań wzorca niż liczba którą podaliśmy to tekst zostanie podzielony z wykorzystaniem tylko tej ilości wzorca podziału jaką wskazaliśmy w tym dodatkowym parametrze.
# Kolejnośc dopasowanych wzorców podziału, które zostaną wzięte pod uwagę jest zgodna z ich kolejnością wystąpienia w przeszukiwanym tekście.
# Natomiast jeżeli wskazaliśmy większą liczbę niż faktyczna ilość wystąpień wzorca to wówczas użyta zostanie maksymalna wystepująca ilość dopasowanych wzorców podziału. Nie zostanie zwrócony błąd, że podaliśmy błędą liczbę mozliwych wystąpnień wzorca.
# Podając wartość zero funkcja zachowa się tak jakbyśmy nie podali żadnej liczby jako parametru oznaczającego ile dopasowań wzorca chcemy użyć jako elementu dzielącego tekst, czyli podzieli tekst wykorzystując wszystkie wystąpnienia wzorca.
# Natomiast jeżeli podamy wartość ujemną to tekst nie zostanie podzielony tylko jako całość umieszczony w liście pod indeksem zerowym.

# Sładnia:
# re.split("wzorzec", "przeszukiwany tekst", liczba_okreslająca_ilość_możliwych_znalezień_wzorca_podziału)

# Przykład 6:
txtE6 = "Motocykle to jest to czego człowiek potrzebuje tonami" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca
print(re.split("to", txtE6, 3)) # wyświetlenie listy zwracanej przez funkcję re.split() gdzie elementem podziału jest wzorzec "to".
                                # natomiast przeszukiwanym tekstem, w celu poszukiwania wzorca, jest zmienna tekstowa txtE6.
                                # Wzorzec "to" w przeszukiwanym tekście występuje cztery razy.
                                # A więc tekst może być podzielony maksymalnie na pięć elementów typu string jako elementy listy.
                                # Ostatnim argumentem jest liczba określająca ile wystąpień wzorca jako elementu dzielącego tekst chcamy uwzglądnić.
                                # W naszym przypadku jest liczba 3, a zatem nasz tekst będzie podzielony na cztery części.
                                # Tekst będzie podzielony zgodnie z kolejnością występowania wzorców, jako elementów podziału, w tekście.

#/////////////////
# re.sub()

# Funkcja ta zwraca tekst w którym dopasowania do wzorca są zastąpione zadanym tekstem podanym jako jeden z parametrów funkcji.

# Sładnia:
# re.sub("wzorzec", "tekstZastępującyWzorzecz", "przeszukiwany tekst")

# Przykład 7:
txtE7 = "Mam bzika na punkcie motocykli" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca
print(re.sub("\s", "TAK", txtE7)) # wyświetlenie zmienionego tekst zwróconego przez funkcję re.sub() gdzie wzorcem do zmiany jest tekst "\s" czyli spacja,
                                  # a tekstem który był podstawiany pod dopasowany wzorzec jest tekst "TAK".
                                  # Podsumowując każda znaleziona spacja w przeszukiwanym tekście została zamieniona tekstem "TAK".
                                  # Przeszukiwanym tekstem, w celu poszukiwania wzorca do podmiany, jest zmienna tekstowa txtE7.


# Ciekawym, dodatkowym, nie wymaganym parametrem w funkcji re.sub() jest możliwość określenia limitu poszukiwań wzorca jako elementu do podmiany w przeszukiwanym tekście.
# Wówczas jeżeli w przeszukiwanym tekście jest więcej dopasowań wzorca niż liczba którą podaliśmy to wzorzec zostanie podmieniny tylko taką ilości razy jaką wskazaliśmy w tym dodatkowym parametrze.
# Kolejnośc dopasowanych wzorców do podmiany, które zostaną wzięte pod uwagę jest zgodna z ich kolejnością wystąpienia w przeszukiwanym tekście.
# Natomiast jeżeli wskazaliśmy większą liczbę niż faktyczna ilość wystąpień wzorca to wówczas użyta zostanie maksymalna wystepująca ilość dopasowanych wzorców do podmiany. Nie zostanie zwrócony błąd, że podaliśmy błędą liczbę możliwych wystąpnień wzorca.
# Podając wartość zero funkcja zachowa się tak jakbyśmy nie podali żadnej liczby jako parametru oznaczającego ile dopasowań wzorca chcemy użyć do podmiaty, czyli podmieni wszystkie wystąpnienia wzorca.
# Natomiast jeżeli podamy wartość ujemną to żaden wzorzec nie zostanie podmieniony. Zwrócony zostanie oryginalny tekst.

# Sładnia:
# re.sub("wzorzec", "tekstZastępującyWzorzecz", "przeszukiwany tekst", liczba_okreslająca_ilość_możliwych_znalezień_wzorca_podmiany)

# Przykład 8:
txtE8 = "Nie wiem co bym zrobil bez motocykla" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca
print(re.sub("\s", "YES", txtE8, 3)) # wyświetlenie zmienionego tekst zwróconego przez funkcję re.sub() gdzie wzorcem do zmiany jest tekst "\s" czyli spacja,
                                     # a tekstem który był podstawiany pod dopasowany wzorzec jest tekst "YES".
                                     # Przeszukiwanym tekstem, w celu poszukiwania wzorca do podmiany, jest zmienna tekstowa txtE7.
                                     # Wzorzec "\s" w przeszukiwanym tekście występuje sześć razy.
                                     # A więc w przeszukiwanym tekście wzorzec może być podmieniony maksymalnie na sześć razy.
                                     # Ostatnim argumentem jest liczba określająca ile wystąpień wzorca jako elementy do podmiany chcamy uwzglądnić.
                                     # W naszym przypadku jest liczba 3, a zatem pierwsze trzy wystąpnienia wzorca zostaną zastąpione zadanym tekstem. Pozostałe będą bez zmian.
                                     # Wzorce będą zastąpione zgodnie z ich kolejnością występowania w przeszukiwanym tekście.

#/////////////////
#/////////////////
# Tworzenie wyrażeń regularnych

# Opisywanie modułu re wraz z jego funkcjami wykorzystywanymi podczas obsługi wyrażeń regularnych
# dokonywaliśmy na prostych przykładach. Wzorcami były proste wyrazy, frazy, zwroty, które jako całość były szukane
# w przeszukiwanym tekście. Tak naprawdę w przypadku przeszukiwania tekstu gdzie wzorcem jest jakiś wyraz bądź fraza,
# to nie jest najbardziej optymalne wykorzystanie modułu re.
# Jeżeli szukamy w teksćie całych wyrazów bądź fraz itp. to można to zrobić bez modułu re, wykorzystując wyrażenia warunkowe pythona.

# Moduł re jest wykorzystywany do bardziej skomplikowanych wyszukań wzorców w tekstach.
# Aby budować złozone, wydajne wzorce do dopasowania powinniśmy używać metaznaki, sekwencje specjalne oraz zestawy metaznaków.

#/////////////////
# Metaznaki

# Metaznaki to znaki o specjalnym znaczeniu przy tworzeniu wzorca.
# Najczęściej stosowane metaznaki"

# "[]" - umieszczony międzi tymi nawiasami (metaznak) zestaw znaków zostanie wyszukany w przeszukiwanym tekście.
# Możliwe kombinacje zestawów znaków:
txtESet1 = "The rain in_Spain 19" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia zestawów znaków.
txtESet2 = "NBA to koszykówka, a NHL to hokej" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia zestawów znaków.
txtESet3 = "Ze Szczekocin do Częstochowy jest 60 km" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia zestawów znaków.
txtESet4 = "Big Apple to potoczna nazwa na NYC" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia zestawów znaków.
txtESet5 = "$5 + $10 = $15" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia zestawów znaków.
# "[arn]" - zwraca dopasowanie dla dowolnej z małych liter: a, r lub n
# "[a-n]" - zwraca dopasowanie dla dowolnej małej litery z przedziału alfabetycznego od a do n
# "[N-Z]" - zwraca dopasowanie dla dowolnej dużej litery z przedziału alfabetycznego od N do Z
# "[N][A-Z][A-Z]" - zwraca dopasowanie dla trzyliterowego wzorca, w którym pierwszą literą jest duże N, a dwie kolejne litery są z przedziału dużych liter od A do Z.
                  # UWAGA !! W przypadku jezeli we wzoru użyjemy jednego zestawu z przedziałem wówczas każdy pojedynczy znak w przeszukiwanym tekście będzie dopasowywany do wzorca.
                  # Natomiast jeżeli użyjemy kilku zestaów znaków obok siebie to zbudujemy z nich wzorzec szukanego formatu wyrazów bądź cyfr.
                  # W tym przykładzie szukamy trzyliterowego wzorca, w którym pierwszą literą jest duże N, a dwie kolejne litery są z przedziału dużych liter od A do Z.
# "[^arn]" - zwraca dopasowanie dla dowolnej małej litery z POMINIĘCIEM liter: a, r i n (to wyrażenie uwzgldnia znaki typu spacka, myślnik, podkreślnik itp)
           # UWAGA !! Zastosowanie metaznaku ^ wewnątrz metaznaku jakim jest zestaw znaków [] ma inne znacznie niż, użycie tego znaku pozna zestawem znaków.
           # Tutaj ma znaczenie NOT, czyli nie bierz do dopasowania znaków: a, r i n.
           # Inne metaznaki nie maja specjalnego znaczenia wewnątrz zestawów znaków [].
           # Tylko ten jeden ^ specjalny znak ma dwa znaczenia. Wewnątrz metaznaku zestaw znaków [] oraz na zewnątrz. W każdym przypadku ma inne znaczenie.
# "[0123]" - zwraca dopasowanie dla dowolnej cyfry: 0, 1, 2 lub 3
# "[0-9]" - zwraca dopasowanie dla dowolnej cyfry z przedziału od 0 do 9
# "[0-6][0-9]" - zwraca dopasowanie dla dowolnej dwucyfrowej liczby z przedziału od 00 do 69
               # UWAGA !! W przypadku jezeli we wzoru użyjemy jednego zestawu z przedziałem wówczas każdy pojedynczy znak w przeszukiwanym tekście będzie dopasowywany do wzorca.
               # Natomiast jeżeli użyjemy kilku zestaów znaków obok siebie to zbudujemy z nich wzorzec szukanego formatu wyrazów bądź cyfr.
               # W tym przykładzie szukamy dwucyfrowej liczby od 00 do 69.
# "[a-zA-Z]" - jest to bardzo podobny wzorzec do wzorca [a-z], jednak w tym wypadku zwraca dopasowanie dowolnej MAŁEJ BĄDŹ DUŻEJ litery z przedziału alfabetycznego od a do z.
             # UWAGA !! Przedział alfabetyczny małych liter oraz przedział dużych liter nie muszą być sobie równe.
                      # W innym przedziale alfabetycznym możemy szukać liter małych, a w innym dużych liter.
# "[+]" - poza jednym metaznakiem, tj. ^, pozostałe metaznaki nie maja specjalnego znaczenia przy stosowaniu ich wewnątrz zestawów znaków [].
        # A więc poza tym jednym, umieszczenie metaznaku wewnątrz zestawu znaków [] zwróci dopasowanie występowania tego znaku w przeszukiwanym tekście.
        # Takie "zwykłe" działanie będą miały następujące metaznaki: +, *, ., |, (), $, {}.
print(re.findall(r"[arn]", txtESet1)) # zwraca dopasowania które są małymi literami: a, r lub n
print(re.findall(r"[a-n]", txtESet1)) # zwraca dopasowania które są małymi literami z przedziału od a do n
print(re.findall(r"[N-Z]", txtESet1)) # zwraca dopasowania które są dużymi literami z przedziału od N do Z
print(re.findall(r"[N][A-Z][A-Z]", txtESet2)) # zwraca dopasowanie które jest trzyliterowym wyrazem zaczynającym się na dużą literę N, a dwie kolejne litery są z przedziału duzych liter od A do Z
print(re.findall(r"[^arn]", txtESet1)) # zwraca dopasowania które są małymi literami z POMINIĘCIEM liter a, r i n (z uwzględnieniem spacji, podkreślnika i cyfr)
print(re.findall(r"[0123]", txtESet1)) # zwraca dopasowanie którym jest cyfra: 0, 1, 2 lub 3
print(re.findall(r"[0-9]", txtESet1)) # zwraca dopasowanie którym jest cyfra z przedziału od 0 do 9
print(re.findall(r"[0-6][0-9]", txtESet3)) # zwraca dopasowanie którym jest dwucyfrowa liczba z przedziału od 00 do 69
print(re.findall(r"[a-kA-Z]", txtESet4)) # zwraca dopasowania które są małymi literami z przedziału od a do k oraz
                                        # te które są dużymi które z przedziału od A do Z.
print(re.findall(r"[$+]", txtESet5)) # zwraca dopasowanie które są następującymi znakami: % lub +

# "\" - metaznak ten oznacza rozpoczęcie specjalnej sekwencji, której funkcja jest zależna od znaku nastepującego. Właśnie znak następny po znaku \ świadczyć będzie o konkretnej funkcji sekwencji specjalnej.
      # Znak ten stosujemy również w momencie jak chcemy aby znak który w występuje w przeszukiwanym tekście i jest jednocześnie jednym z metaznaków wykorzystywanych w wyrażeniach regularnych był traktowany jako zwykły znak używany w przeszukiwanym tekście.
      # Najlepszym przykładem jest kropka kończąca zdanie.
      # Jeżeli chcielibyśmy wymienić kropę kończącą zdanie we wzorcu aby zostało znalezione dopasowanie w przeszukiwanym tekście to bez zastosowania przed tą kropą metaznaku \ kropka wymieniona we wzorcu miałaby zastosowanie jak metaznak "." zastępujący dowolny znak. A więc tak naprawde kropka kończąca zadanie wzięta byłaby za metaznak oznaczający, że tutaj może wystąpić jeszcze jakiś znak, nie koniecznie byłaby to kropka.
      # Zastosowanie we wzorcu przed kropą metaznaku "\." spowoduje, że w tym wypadku kropkę traktujemy po prostu jak kropkę którą szukamy w przeszukiwanym tekście a NIE jako metaznak "." oznaczający/zastępujący dowolny możliwy do wystąpnienia znak.
      # I tak samo postepujemy w przypadku innych metaznaków które chcemy wyszukać w przeszukiwanym tekście jako znaki które tam występują.
# Możliwe znaki specjalne używane w sekwencjach specjalnych:
txtESpec1 = "The rain in Spain" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia sekwencji specjalnej.
txtESpec2 = "Dzisiaj 09.03 o godzinie 17:00 bede jesc obiad" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia sekwencji specjalnej.
txtESpec3 = "Mam-3_4 lata" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia sekwencji specjalnej.
txtESpec4 = "Ile masz lat ?" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia dezaktuywacji metaznaku a wystąpienia jego znaczenia w normalnym tekście.
txtESpec5 = "Ferrari ma silnik o mocy 60[KM]"
# r"\znak_Specjalny" - literka r przed wzorcem oznacza, że chcemy aby wzorzec był traktowany jako oryginalny, nieprzetworzony ciąg znaków.
                     # Ma to znaczenie ponieważ niektóre wzorce Python może nie przyjąć z powodu błędnej interpretacji przez niego ciągu znaków jako wyrażenia regularnego.
                     # Dobrym przykładem jest tutaj znak specjalny \ oznaczający start specjalnej sekwencji. Znak ten w innych metodach i zastosowaniach w czystym Pythonie informuje go o tym, że kończymy stosowanie znaków specjalnych czystego Pythona, jak tabulator \t, przejście do nowej linii \n itd.
                     # Bez użycia r przed wzorcem z wyrażeniem regularnym Python może wymagać stosowania dodatkowych znaków aby znaczenie znaku \ nie było błędnie interpretowane przez czystego Pyhona jako zakończenie używania znaków spacjalnych czystego Pythona. A tym samym aby znak \ mógł mieć swoje znaczenie specjalne w wyrażeniu regularnym a nie czystym Pythonie. Jednak taka ochrona znaku \ utrudniałąby czytanie kodu z wyrażeniami regularnymi.
                     # A zatem użycie r zabezpieczna nas przed tego typu sytuacjami i ułatwi czytanie i rozumienie kodu.
# "\A" - zwraca dopasowanie jeżeli określony ciąg znaków umieszczony bezpośrednio PO tej sekwencji występuje na POCZĄTKU przeszukiwanego tekst.
# "\Z" - zwraca dopasowanie jeżeli określony ciąg znaków umieszczony bezpośrednio PRZED tą sekwencją występuje na KOŃCU przeszukiwanego tekst.
       # UWAGA !! Jako ostatni znak nie może być min. znak zapytania ?, ponieważ zostanie zwrócony brak dopasowania. Możliwe, że są jeszcze jakieś inne znaki które spowodują zwrócenie braku dopasowania.
# "\b" - zwraca dopasowanie jeżeli okreslone znaki umieszczone bezpośrednio PO tej sekwencji występują na POCZĄTKU każdego ze słów wystepujących w przeszukiwanym tekście
       # bądź jeżeli okreslone znaki umieszczone bezpośrednio PRZED tą sekwencji występują na KOŃCU każdego ze słów wystepujących w przeszukiwanym tekście.
       # Funkcja przeszukuje tekst w tej sekwencji analizując każde słowo z których tekst jest złozony i sprawdza czy wzorzec wystepuje na początku bądź na końcu każdego ze słów składowych.
# "\B" - zwraca dopasowanie jeżeli okreslone znaki umieszczone bezpośrednio PO tej sekwencji są OBECNE ale NIE na POCZĄTKU każdego ze słów wystepujących w przeszukiwanym tekście
       # bądź jeżeli określone znaki umieszczone bezpośrednio PRZED tą sekwencji są OBECNE ale NIE na KOŃCU każdego ze słów wystepujących w przeszukiwanym tekście.
       # Funkcja przeszukuje tekst w tej sekwencji analizując każde słowo z których tekst jest złozony i sprawdza czy wzorzec wystepuje na początku bądź na końcu każdego ze słów składowych.
# "\d" - zwraca dopasowanie dla dowolnych cyfr z przedziału od 0 do 9 występujących w przeszukiwanym tekście.
# "\D" - zwraca dopasowanie dla znaków NIE będących cyfrą z przedziału od 0 do 9.
# "\s" - zwraca dopasowanie dla białych znaków.
# "\S" - zwraca dopaswoanie dla znaków NIE będących spacją.
# "\w" - zwraca dopasowanie dla znaków alfanumerycznych (małe i duże litery od a do Z, cyfry od 0 do 9, podkreślnik też się wlicza, ale spacja i myślnik się nie wliczają)
# "\W" - zwraca dopasowanie dla znaków NIE alfanumerycznych (spacja oraz myślnik są znakami nie alfanumerycznymi)
print(re.findall(r"\AThe", txtESpec1)) # zwraca dopasowanie jeżeli na początku przeszukiwanego tekstu występuje ciąg znaków "The"
print(re.findall(r"Spain\Z", txtESpec1)) # zwraca dopasowanie jeżeli na końcu przeszukiwanego tekstu wystepuje ciąg znaków "Spain"
print(re.findall(r"\bra", txtESpec1)) # zwraca dopasowanie jeżeli jakiekolwiek słowo w przeszukiwanym tekście zaczyna się od znaków "ra"
print(re.findall(r"in\b", txtESpec1)) # zwraca dopasowanie jeżeli jakiekolwiek słowo w przeszukiwanym tekście kończy się znakami "in"
print(re.findall(r"\Bin", txtESpec1)) # zwraca dopasowanie jeżeli jakiekolwiek słowo w przeszukiwanym tekście ZAWIERA ale NIE zaczyna się od znaków "in"
print(re.findall(r"ra\B", txtESpec1)) # zwraca dopasowanie jeżeli jakiekolwiek słowo w przeszukiwanym tekście ZAWIERA ale NIE kończy się znakami "ra"
print(re.findall(r"\d", txtESpec2)) # zwraca dopasowanie będące cyfrą z przedziału od 0 do 9
print(re.findall(r"\D", txtESpec2)) # zwraca dopasowanie NIE będące cyfrą z przedziału od 0 do 9
print(re.findall(r"\s", txtESpec2)) # zwraca dopasowanie będące spacją
print(re.findall(r"\S", txtESpec2)) # zwraca dopasowanie nie będące spacją
print(re.findall(r"\w", txtESpec3)) # zwraca dopasowanie dla znaków alfanumerycznych
print(re.findall(r"\W", txtESpec3)) # zwraca dopasowanie dla znaków NIE alfanumerycznych
print(re.findall(r"lat \?", txtESpec4)) # zwraca dopasowanie zawierające metaznak mający zastosowanie w wyrażeniach regularnych, ale w tym wypadku zostało jego działanie jako metaznaku wyłączone i jest on rozumiany jako zwykły znak
print(re.findall(r"60\[KM\]", txtESpec5)) # zwraca dopasowanie zawierające metaznak mający zastosowanie w wyrażeniach regularnych, ale w tym wypadku zostało jego działanie jako metaznaku wyłączone i jest on rozumiany jako zwykły znak

# "." - metaznak ten we wzorcu dopasowania oznacza/zastępuje dowolny znak w przeszukiwanym tekście (poza znakiem oznaczającym przejście do nowej linii (\n), a wiec znaki tabulatora (\t) czy spacji, itd też są brane pod uwagę).
      # Najczęściej stosuje się ten metaznak w budowie wzorca za pomocą którego chcemy znaleźć ciąg znaków zbudowany z określonej liczby znaków w którym niektóre znaki chcemy aby wystapiły w oryginalenj formie, wówczas podajemy te znaki, a niektóre znaki są dla nas nieistotne wówczas zastępujemy je kropką.
      # Ważnym aspektem jest sposób przeszukiwania tekstu w poszukiwaniu dopasowania do wzorca. W zależności od ilości znaków wzorca tak będzie przszukiwany tekst. Jeżeli wzorzec składa się z czterech znaków, wówczas w przeszukiwanym tekście będą sprawdzane pierwsze cztery znaki ze zgodnością wzorca, następnie znowu cztery znaki i tak dalej aż do końca tekstu. Ostatnim możliwym wzorcem zawsze będzie ciąg złożony z czterech znaków.
      # Analogiczne będzie postępowanie z inną ilością znaków wzorca. Jeżeli wzorzec będzie mieć tylko jeden metaznak . to zwócone zostaną wszystkie znaki z tekstu, prócz znaku przejścia do nowej linii.
txtE9 = "Kogo witam, kogo goszcze" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku ".".
print(re.findall(r".", txtE9)) # zwraca dopasowanie dla każdego, dowolengo znaku z przeszukiwanego tekstu.
print(re.findall(r".....", txtE9)) # zwraca dopasowanie dla wzroca złożonego z pięciu dowolnych znaków. A więc w tekście będą poszukiwane ciągi złożone z pięciu dowolnych znaków. Zaczynając od początku tekstu. Pierwszym ciągiem będzie ciąg od znaku o indeksie zero do znaku o indeksie cztery - pięć znaków. Następny ciąg to będzie ciąg od znaku o indeksie pięć do znaku o indeksie dziwięć - pięć znaków. I tak dalej. Aż do końca tekstu.
print(re.findall(r".og.", txtE9)) # zwraca dopasowanie dla wzorca złożonego z czterech znaków w którym pierwszy i ostatni znak może być dowolny, a drugi i trzeci to odpowiednio znaki o i g.

# "^" - metaznak ten zwraca dopasowanie jeżeli określony ciąg znaków umieszczony bezpośrednio PO tym znaku występuje na POCZĄTKU przeszukiwanego tekst.
      # Znak ten ma takie samo zastosowanie jak sekwencja specjalna "\A" po której umieszczony ciąg znaków jest sprawdzany czy występuje na początku przeszukiwanego tekstu.
txtE10 = "Ducati czy Honda ? co wybrac ?" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "^".
print(re.findall(r"^Ducati", txtE10)) # zwraca dopasowanie jeżeli na początku przeszukiwanego tekstu występuje ciąg znaków "Ducati"

# "$" - metaznak ten zwraca dopasowanie jeżeli określony ciąg znaków umieszczony bezpośrednio PRZED tym znakiem występuje na KOŃCU przeszukiwanego tekst.
      # Znak ten ma takie samo zastosowanie jak sekwencja specjalna "\Z" przed którą umieszczony ciąg znaków jest sprawdzany czy występuje na końcuś przeszukiwanego tekstu.
      # UWAGA !! Jako ostatni znak nie może być min. znak zapytania ?, ponieważ zostanie zwrócony brak dopasowania. Możliwe, że są jeszcze jakieś inne znaki które spowodują zwrócenie braku dopasowania.
txtE11 = "Tomek ma marzenia" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "$".
print(re.findall(r"marzenia$", txtE11)) # zwraca dopasowanie jeżeli na końcu przeszukiwanego tekstu występuje ciąg znaków "marzenia"

# "*" - wykorzystując ten metaznak we wzorcu sprawdzamy czy znak umieszczony bezpośrednio przed tym metaznakiem nie występuje ani razu razy lub występuje po kolei więcej razy po sobie.
      # Warunkiem jest aby we wzorcu przed tym metaznakiem był conajmniej jeden znak aby wzorzec miał co sprawdzać i dopasowywać w przeszukiwanym tekście.
      # Dziwne jest to, że sprawdzamy czy coś występuje zero lub więcej razy. Bo jeżeli tylko jeden znak umieścimy we wzorcu przed tym metaznakiem to wiadomo, że cały przeszukiwany tekst nie składa się tylko z jednego znaku, a więc zwróci nam jako dopasowania puste miejsca tam gdzie ten znak nie wystepuje oraz faktyczny znak którego szukamy w miejscu gdzie on wystepuje w tekście.
      # Jeszcze do powyższego: nie zwróci nam tylko tego znaku którego szukam, ale też puste miejsca świadczące o tym, że w tym miejscu jest jakiś znak, ale on nie jest tym którego szukamy. A więc ilość dopasowań będzie równa ilości znaków w przeszukiwanym tekście, ale w miejscach gdzie nie znalazł tego szukanego znaku to zwróci puste miejsca.
      # Ważne jest też, że jeżeli przed tym metaznakiem umieścimy więcej niż jeden znak. To tylko ostatni znak przed metaznakiem z ciągu znaków będzie sprawdzany czy występuje zero lub więcej razy po kolei po sobie. Natomiast wcześniejsze znaki muszą wystąpić dokładnie w takiej kolejności jak we wzorcu, jeżeli chcemy aby znalazł dopasowanie.
      # Powyższe daje nam pewną elastyczność, ponieważ ostatni znak przed "*" może, ale nie musi wystapić. Wcześniejsze znaki wystapić muszą. W specyficznych przeszukiwaniach może mieć zastosowanie.
txtE12 = "The rainnn in Spain falls mainly in the plain!" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "*".
print(re.findall(r"i*", txtE12)) # zwraca dopasowanie sprawdzając czy znak "i" występuje zero lub więcej razy po kolei po sobie. W efekcie zwraca puste miejsca tam gdzie w tekście przeszukiwanym były inne znaki niż "i", natomiast tam gdzie było "i" zwraca "i".
print(re.findall(r"aic*", txtE12)) # zwraca dopasowanie zawierające ciąg znaków "ai" oraz jeżeli ten ciąg znaków na końcu zawiera "c" to zwróci ciąg znaków "aic" z taką ilością znaków "c" ile ich było po sobie, a jeżeli nie zawiera "c" to zwróci samo "ai". To się dzieje dzięki temu, że metaznak "*" sprawdza ostatni znak ze wzorca czy wystepuje zero lub więcej razy. Czyli może, ale nie musi on wystapić. Wcześniejsze znaki wystapić muszą wystąpić.
print(re.findall(r"ain*", txtE12)) # zwraca dopasowanie zawierające ciąg znaków "ai" oraz jeżeli ten ciąg znaków na końcu zawiera "n" to zwróci ciąg znaków "ain" z taką ilością znaków "n" ile ich było po sobie, a jeżeli nie zawiera "n" to zwróci samo "ai". To się dzieje dzięki temu, że metaznak "*" sprawdza ostatni znak ze wzorca czy wystepuje zero lub więcej razy. Czyli może, ale nie musi on wystapić. Wcześniejsze znaki wystapić muszą wystąpić.

# "+" - wykorzystując ten metaznak we wzorcu sprawdzamy czy znak umieszczony bezpośrednio przed tym metaznakiem występuje dokładnie jeden raz lub wystepuje po kolei więcej razy po sobie.
      # Warunkiem jest aby we wzorcu przed tym metaznakiem był conajmniej jeden znak aby wzorzec miał co sprawdzać i dopasowywać w przeszukiwanym tekście.
      # Jeżeli tylko jeden znak umieścimy we wzorcu przed tym metaznakiem to zwróci nam tylko dopasowania będące tym konkretnym jednym znakiem występującym jeden raz lub kilka razy po sobie. Jeżeli nie znajdzie żadnego tego znaku w przeszukiwanym tekście to zwróci brak dopasowań.
      # Ważne jest też, że jeżeli przed tym metaznakiem umieścimy więcej niż jeden znak. To tylko ostatni znak przed metaznakiem z ciągu znaków będzie sprawdzany czy występuje jeden lub więcej razy po kolei po sobie. Natomiast wcześniejsze znaki muszą wystąpić dokładnie w takiej kolejności jak we wzorcu, jeżeli chcemy aby znalazł dopasowanie.
      # Jeszcze do powyższego: wszystkie znaki ze wzorca muszą wystapić tylko ostatni znak przed metaznakiem musi wystąpić conajmenij raz. A może wystapić więcej niż raz po kolei po sobie.
      # Tutaj jest troche inne zachowanie w przeciwieństwie do metaznaku "*". Tam ostatni znak przed metaznakiem mógł ale nie musiał wystąpić, pozostałe musiały wystąpić w takim położeniu w jakim były we wzorcu. W przypadku metaznaku "+" wszystkie znaki będące we wzrocu muszą wystapić dokładnie w takim położeniu jak w wzrocu, jednak ostatni przed metaznaki może wystapić jeden lub więcej razy po sobie.
txtE13 = "The raiiin in Spain falls mainly in the plain!" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "+".
print(re.findall(r"i+", txtE13)) # zwraca dopasowanie sprawdzając czy znak "i" występuję jeden lub więcej razy po sobie. Jeżeli występuje więcej razy po sobie to to dopasowanie będzie jako ciąg znaków "i" występujących tyle razy ile wystapiły po sobie w przeszukiwanym tekście. Natomiast inne, pojedyncze występowania "i" będą zwrócone jako pojedyncze występowania.
print(re.findall(r"ai+", txtE13)) # zwraca dopasowanie zawierające ciąg znaków "ai" z jednym znakiem "i" bądź więcej. W zależności ile znaków "i" było po sobie w tekście przeszukiwanym.

# "{m}" - ten meta znak jest rozwinięciem metaznaków "*" i "+". Wyżej opisywane znaki okreslają, że umieszczony bezpośrednio przed nimi znak może odpowiednio nie wystąpić ani razu lub występuje po kolei więcej razy po sobie oraz występuje dokładnie jeden raz lub wystepuje po kolei więcej razy po sobie.
# "{m,n}" Z kolei ten metaznak {} wraz z umieszczoną w nim liczbą określa ile razy znak umieszczony bezpośrednio przed tym metaznakiem występuje. Liczba określa dokładną ilość razy ile ma wystąpić, a NIE, że stanowi granicę.
        # Jeżeli w tym metaznaku umieścimy dwa {2} to znaczy, że znak umieszczony bezpośrednio przed tym metaznakim musi wystapić bezpośrednio po sobie dwa razy. I tak dalej.
        # Ważne jest też, że jeżeli przed tym metaznakiem umieścimy więcej niż jeden znak. To tylko ostatni znak przed metaznakiem z ciągu znaków będzie sprawdzany czy występuje taką ilość razy po kolei po sobie jaką mu zadamy umieszczając liczbę pomiędzy mietaznak {liczba}. Natomiast wcześniejsze znaki muszą wystąpić dokładnie w takiej kolejności jak we wzorcu, jeżeli chcemy aby znalazł dopasowanie.
        # UWAGA !! Możemy również określić zakres, przedział ilości wystąpień po kolei po sobie znaku braną pod uwagę umieszczonego bezpośrednio przed metaznakiem {}.
                # Wówczas między metaznakim {m, n} opdajemy dwie liczby rozdzielone przecinkiem. Pierwsza "m" musi być mniejsza od drugiej "n".
                # Pierwsza "m" oznacza minimalną ilość wystapień po sobie znaku, braną pod uwagę w szukaniu dopasowania.
                # Druga "n" oznacza maksymalną ilość wystąpień po sobie znaku, braną pod uwagę w szukaniu dopasowania.
                # NAJWAŻNIEJSZE !! Zwracane jest dopasowanie którego znak opisany metaznakiem z przedziałem {m, n} występuje maksymalną ilość razy z przedziału od m do n.
                                 # Czyli nawet jeżeli znak będzie wystepować mniejszą ilość razy ale będzie się łapać w przedział ale będzie też sytuacja w której ten sam znak będzie powtarzać się maksymalną ilość razy określoną przez drugą liczbę "n" to wówczas będzie zwrócona tylko sytuacja dopasowania które zawiera znak powtarzający się maksymalną bądź najbliższą do maksymalnej ilość razy.
        # UWAGA !! Jeżeli nie podamy wartości "m" wówczas metaznak ten będzie oznaczał, że poprzedzający go znak może wystąpić maksymalnie n razy po sobie.
                 # Na przykład: {,3} - oznacza, że poprzedzający go znak może wystąpić maksymalnie 3 razy po sobie.
                 # Jeżeli nie podamy wartości "n" wówczas metaznak ten będzie oznaczał, że poprzedzający go znak musi wystąpić conajmniej m razy po sobie.
                 # Na przykład: {2,} - oznacza, że poprzedzający go znak musi wystąpić conajmniej 2 razy po sobie.
txtE14 = "The rain in Spain fallllls mainly in the plain!" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "{}".
print(re.findall(r"al{2}", txtE14)) # zwraca dopasowania zawierające ciąg znaków "all" gdzie znak "l" musi wystąpić dwa razy, zgodnie z liczbą umieszczoną w mateznaku {2}.
print(re.findall(r"al{1}", txtE14)) # zwraca dopasowania zawierające ciąg znaków "al" gdzie znak "l" musi wystąpić jeden raz, zgodnie z liczbą umieszczoną w mateznaku {1}.
print(re.findall(r"al{0}", txtE14)) # zwraca dopasowania zawierające ciąg znaków "a" bez znaku "l" który nie może wystąpić, zgodnie z liczbą umieszczoną w metaznaku {0}.
print(re.findall(r"al{2,4}", txtE14)) # zwraca dopasowanie zawierające ciąg znaków "al" ze znakiem "l" powtarzającym się maksymalną bądź zbliżoną do maksymalnej ilość razy z przedziału wystąpień między 2 a 4 {2, 4}. A więc będzie tylko jedno dopasowanie.

# "?" - wykorzystując ten metaznak we wzorcu sprawdzamy czy znak umieszczony bezpośrednio przed tym metaznakiem występuje zero lub jeden razy.
      # Czyli inaczej mówiąc znak przed tym metaznakiem jest opcjonalny. Może wystąpić, ale nie musi.
      # Warunkiem jest aby we wzorcu przed tym metaznakiem był conajmniej jeden znak aby wzorzec miał co sprawdzać i dopasowywać w przeszukiwanym tekście.
      # Dziwne jest to, że sprawdzamy czy coś występuje zero razy. Bo jeżeli tylko jeden znak umieścimy we wzorcu przed tym metaznakiem to wiadomo, że cały przeszukiwany tekst nie składa się tylko z jednego znaku, a więc zwróci nam jako dopasowania puste miejsca tam gdzie ten znak nie wystepuje oraz faktyczny znak którego szukamy w miejscu gdzie on wystepuje w tekście.
      # Jeszcze do powyższego: nie zwróci nam tylko tego znaku którego szukam, ale też puste miejsca świadczące o tym, że w tym miejscu jest jakiś znak, ale on nie jest tym którego szukamy. A więc ilość dopasowań będzie równa ilości znaków w przeszukiwanym tekście, ale w miejscach gdzie nie znalazł tego szukanego znaku to zwróci puste miejsca.
      # Ważne jest też, że jeżeli przed tym metaznakiem umieścimy więcej niż jeden znak. To tylko ostatni znak przed metaznakiem z ciągu znaków będzie sprawdzany czy występuje zero lub jeden raz. Natomiast wcześniejsze znaki muszą wystąpić dokładnie w takiej kolejności jak we wzorcu, jeżeli chcemy aby znalazł dopasowanie.
      # Powyższe daje nam pewną elastyczność, ponieważ ostatni znak przed "?" może, ale nie musi wystapić. Wcześniejsze znaki wystapić muszą. W specyficznych przeszukiwaniach może mieć zastosowanie.
txtE15 = "Testyy testom testowanym" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "?".
print(re.findall("s?", txtE15)) # zwraca dopasowanie sprawdzając czy znak "s" występuje zero lub jeden razy. W efekcie zwraca puste miejsca tam gdzie w tekście przeszukiwanym były inne znaki niż "s", natomiast tam gdzie było "s" zwraca "s".
print(re.findall("sty?", txtE15)) # zwraca dopasowanie zawierające ciąg znaków "st" oraz jeżeli ten ciąg znaków na końcu zawiera "y" to zwróci ciąg znaków "sty" ale tylko jeżeli "y" wystepuje raz, a jeżeli nie zawiera "y" to zwróci samo "st". To się dzieje dzięki temu, że metaznak "?" sprawdza ostatni znak ze wzorca czy wystepuje zero lub jeden raz. Czyli może, ale nie musi on wystapić. Wcześniejsze znaki wystapić muszą wystąpić.

# "|" - ten metaznak stosujemy jednocześnie z ciągami znaków zarówno po lewej jak i po prawej jego stronie. Za jego pomocą sprawdzamy czy w przeszukiwanym tekście jest dopasowanie będące ciągiem znaków z jego lewiej strony LUB ciągiem znaków z jego prawej strony.
      # W przeszukiwanym tekście mogą występować oba ciągi znaków, zarówno ten po lewej jak i ten po prawej stronie metaznaku "|". Wówczas zwrócone zostaną oba znalezione dopasowania. Przy czym pierwszym będzie ten który występuje wcześniej w kolejności.
      # Jeżeli w przeszukiwanym tekście występuje jeden z ciągów znaków występujących po lewej bądź po prawej stronie metaznaku "|". Wówczas zwrócone zostanie dopasowanie odpowiadające ciągowi z lewej bądź z prawej strony. O to w tym metaznaku chodzi, że szukamy albo jeden ciąg znaków (ten z lewej) albo drugi (ten z prawej). Oczywiście, jeżeli wystąpią oba to też dobre rozwiązanie.
      # Można powiedzieć, że metaznak "|" oznacza wartość logiczną LUB. Albo ciąg znaków z lewej wystepuje albo ciąg znaków z prawej występuje.
      # UWAGA !! Nie ma znaczenia po której stronie metaznaku "|" napiszemy ciąg znaków którego szukamy w przeszukiwanym tekście.
               # Nawet jeżeli ciąg znaków który napisaliśmy z prawej strony metaznaku wystepuje w przeszukiwanym tekście wcześniej niż ciąg znaków który napisaliśmy z lewej strony metaznaku "|", to i tak dopasowania zostaną zwrócone prawidłowo według kolejności ich występowania w przeszukiwanym tekście.
      # UWAGA !! Jeżeli nie umieścimy żadnych ciągów znaków po obu stronach metaznaku "|" to napotkamy na sytuację w której zostanie zwrócone dopasowanie w którym będzie taka ilość pustych miejsc ile jest znaków w tekście. I będzie to traktowane, że dopasowanie zostało znalezione.
               # Jeżeli umieścimy ciągów znaków tylko po jednej ze stron metaznaku "|", czy to po lewej jego stronie, czy to prawej jego stronie to wówczas jeżeli zostanie znaleziony ciąg znaków który podaliśmy po którejś ze stron to zostanie zwrócone dopasowanie z taką ilość pustych znaków ile jest znaków w tekście pomniejszoną o ewentualne występowanie tego ciągu znaków którego szukamy. A ciąg ten będzie najdował się wśród tych pustych miejsc. Ale jako jedno całe dopasowanie.
               # To całe dopasowanie będzie zajmowało odpowiednie w kolejności miejsce od początku teksu. A więc będzie wśród znaków pustych ponieważ jedna ze stron metaznaku "|" była pozostawiona pusta.
txtE16 = "Wybiore miedzy motocyklem Honda a Ducati" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "|".
print(re.findall(r"|", txtE16)) # z powodu braku umieszczenia ciągu znaków z obu stron metaznaku "|" i pozostawienie go samego zwrócona zostanie taka ilość pustych miejsc ile jest znaków w tekście. Co stanowi informację o poprawnym znalezieniu dopasowania.
print(re.findall(r"Honda|", txtE16)) # z powodu umieszczenia ciągu znaków tylko z jednej strony metaznaku "|" zwrócony zostanie ten ciąg znaków ale w odpowiedniej kolejności w której występował w przeszukiwanym tekście oraz puste miejsca w miejscu innych niedopasowanych znaków.
print(re.findall(r"Ducati|Honda", txtE16)) # zwraca dopasowanie zawierające ciąg znaków "Ducati" bądź ciąg znaków "Honda".

# UWAGA !! WAŻNE !! UWAGA !!
# () - grupowanie wyrażeń regularnych.
# I. - Wyrażenia regularne pozwalają nam nie tylko od razu szukać wzorców w przeszukiwanym tekście, ale także wyodrębniać informacje. To znaczy, że możemy wyodrębnić pewne podwzorce, wewątrz całego wzorca. Te podwzorce będą stanowiły pewną całość która dokładnie tak musi być wyszukiwana w połączeniu z resztą wzorca.
     # Odbywa się to poprzez definiowanie grup znaków we wzorcu jako podwzorzec który ma stanowić pewną grupę która jako całość będzie wraz z dalszym rozwinięciem wzorca przeszukiwana w tekście. Do grupowania znaków w podwzorce służy metaznak ().
     # Każdy podwzorzec wewnątrz pary nawiasów zostanie przechwycony jako grupa. Wówczas tylko elementy wewnąrz tej grupy będą zwracane jako dopasowanie pomimo, że znaki poza podwzorcem również brały udział w dopasowaniu. Są one wymagane i muszą być obecne w dopasowaniu ale nie są wymagane do ich zwracania w dopasowniu.
     # Znaki które są poza metaznakami () nazywamy grupami nieprzechwytywanymi. Znaki te pozwalają odpowoednio dopasować grupę i również biorą udział we właściwym dopasowaniu grupy ale nie są zwracane w wynikach.
     # A więc cały wzorzec brał udział w szukaniu dopasowania, ale jako dopasowanie zostanie zwrócony tylko podwzorzec umieszczony w metaznaku ().
     # W gupowaniu wzorców najważniejszą cechą jest to, że to co jest zgrupowane jest konieczne w dopasowaniu i jednocześnie jest też zwracane jako efekt dopasowania, natomiast wszystko to co jest poza grupą, poza nawiasem, jest konieczne w dopasowaniu ale nie jest zwracane jako dopasowanie, czyli jest to grupa nieprzechwytywana.
txtE17 = "file_record_transcript.pdf" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "()".
print(re.findall(r"^(file.+)\.pdf$", txtE17)) # zwraca dopasowanie które zaczynają się od słowa "file", a następnie ma jakiekolwiek znaki, a zakończy się znakami: ".pdf".
                                              # Umieszczenie części wzorca w grupie, powoduje, że tylko ta część będąca grupą bedzie zwracana jako doapsowanie, a pozostała część wzorca służy jako dokładność przeszukiwania teksu która nie musi być zwracana, ale która musi być w przeszukiwanym tekście, czyli grupa nieprzechwytywana.
# II. - Podczas pracy ze złożonymi danymi można łatwo wyodrębnić wiele warstw informacji.
      # Możemy to osiągnąć dzięki zagnieżdżaniu grup. Wewnątrz jednej większej grupy możemy umieścić mniejszą podgrupę.
      # W takim wypadku dopasowania będą zwracane dla:
      # - całej, większej grupy w ramach której wchodzi również mniejsza podgrupa biorąc pod uwagę podwzorzec w niej zawarty. Poza tą większą grupą może być jeszcze część wzorca należąca do grupy nieprzechwytywanej.
      # - mniejszej podgrupy, grupy zagnieżdżonej, tylko dla podwzorca w niej zawartego, bez całości wzorca poza tą podgrupą. Cały Wzorzec jest wciąż potrzeby do obecności dopasowani w przeszukiwanym tekście ale nie jest wyświetlany.
      # I tak dalej jeżeli tych podgrup w ramach większych grup jest więcej.
      # Zagnieżdżone grupy są odczytywane we wzorcu od lewej do prawej, przy czym pierwszą grupą zwracaną jest zawartość pierwszej grupy w nawiasach itd.
      # A więc o kolejności zwracanych dopasowań decyduje kolejność tworzenia grup, czyli kolejność nawiasów otwierających. Pierwszą grupą dla której będzie zwracane dopasowanie jest grupa której nawias otwierający jest pierwszy.
      # Pierwsze dopasowanie będzie dla największej grupy. Dopasowania podgrup będą zwracane w późniejszej kolejności.
      # Jeżeli tworzymy grupy zagnieżdżone we wzorcach to możemy stosować metodę .group() w celu odwoływania się do określonej zwróconej grupy zgodnej z grupą wzorca dopasowań.
      # Metodę tę wywołujemy na wyniku metody re.search():
      # re.search(wzorzec,tekst).group(Num) - Num jest to liczba określająca której grupy dopasowanie chcemy wyświetlić. 0 i 1 - oznacza pierwszą grupę wg. umieszczenia nawiasów, 2 - oznacza drugą grupę, itd.
      # W praktyce można to wykorzystać do wyodrębnienia informacji, takich jak numery telefonów lub wiadomości e-mail, z wszelkiego rodzaju danych.
txtE19 = "February 1987" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "()".
print(re.findall(r"(\w+.(\d+))", txtE19)) # zwraca dwa dopasowania, ponieważ są dwie grupy. Przyczym druga grupa jest podgrupą grupy pierwszej.
                                          # Pierwszym będzie dopasowanie zgodne ze wzorcem zawartym w pierwszej grupie, łącznie z podwzorcem wchodzącym w skład podgrupy. Czyli z grupą zagnieżdżoną.
                                          # Drugim będzie dopasowanie zgodne z podwzorcem wchodzącym w skłąd podgrupy.
                                          # Jeżeli jakieś elementy wzroca znajdowałyby się poza grupami to one byłby wymagane w trakcie szukania dopasowania, ale ich znaki w dopasowaniu nie były zwracane. Należały do tak zwanej grupy nieprzechwytywanej.
print(re.search(r"(\w+.(\d+))", txtE19).group(0)) # zwraca dopasowanie pierwszej grupy w kolejności, kolejność określana jest na podstawie kolejności nawiasów otwierających.
print(re.search(r"(\w+.(\d+))", txtE19).group(1)) # zwraca dopasowanie pierwszej grupy w kolejności, kolejność określana jest na podstawie kolejności nawiasów otwierających.
print(re.search(r"(\w+.(\d+))", txtE19).group(2)) # zwraca dopasowanie drugiej grupy w kolejności, kolejność określana jest na podstawie kolejności nawiasów otwierających.
txtE18 = "1280x720" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia metaznaku "()".
print(re.findall(r"(\d+)x(\d+)", txtE18)) # wzorzec zawiera dwie grupy, które są grupami równoległymi. Żadna nie jest grupą zagnieżdżoną. W wynikach będą dwa dopasowania. Najpierw będzie grupa która jest pierwsza w kolejności wg. zasady kolejności występowania nawiasów otwierających.
                                          # Częśc wzorca będąca w grupie nieprzechwytywanej jest wymagana do znalezienia dopasowania, ale nie będzie obecna w wynikach.
# III. - Bardzo przydatną funkcjonalnością grup jest możliwość połączenia ich wraz z operatorem logicznym OR, czyli metaznakiem "|".
       # Tak naprawdę sam wystepujący metaznak "|" bez grupy jest mało przydatny. Dopiero w połączeniu go z grupą zyskujemy duże możliwości w poszukiwaniu różnych zestawów znaków.
       # Metaznak "|" wraz z ciągami znaków po lewej jak i po prawej stronie tego metaznaku zamykamy w grupę (ciagZnakowL|ciagZnakowP). Oprócz tej grupy we wzorcu znajdują się również inne ciągi znaków, wyrażenia regularne, które pozwalają nam szukać różnych zestawów informacji, dopasowań.
       # Oczywiście wewnątrz grupy z metaznakim "|" ciągi znaków po lewej, jak i po prawej jego stronie mogą zawierać również wszelkiego rodzaju kombinacje wyrażeń regularnych.
       # Wówczas całość wzorca jest szukana i zwracana tyle, że w miejscu wystąpienia grupy z metaznakiem "|" zwrócony zostanie wzorzec z lewej lub prawej strony tego metaznaku. Pozostała część wzorca będzie nie zmienna.
       # Takie połączenie grupy oraz metaznaku "|" jest bardzo pomocne jednakże wykorzystanie go w Pythonie zawsze musi się odbywać poprzez metodę re.search(wzorzec,tekst).group(Num). Ta metoda i jej wykorzystanie była opisywana w części II opisu grupowania wyrażeń regularnych.
       # Gdybyśmy nie zastosowali metody re.search().group() wówczas wynikiem dopasowania byłaby tylko i wyłącznie wartość po lewej albo po prawej stronie metaznaku "|" objętego w grupę.
       # Pozostała część byłaby potrzebna do znalezienia dopasowania, ale byłaby tak zwaną grupo nieprzechwytywaną.
       # Dzieje się to z tego samego powodu jak opisywaliśmy w części I opisu grupowania wyrażeń regularnych.
       # Podwzorzec wewnątrz pary nawiasów zostanie przechwycony jako grupa. Wówczas tylko elementy wewnąrz tej grupy będą zwracane jako dopasowanie pomimo, że znaki poza podwzorcem również brały udział w dopasowaniu. Są one wymagane i muszą być obecne w dopasowaniu ale nie będą zwracane w dopasowaniu.
       # Oczywiście w przypadku grupowania metaznaku "|" grybyśmy nie zastosowali re.search().group() to zwrócone zostanie dopasowanie z lewej bądź z prawej strony metaznaku "|".
       # Opisywany problem rozwiązuje zastosowanie metody re.search().group().
       # Oczywiście jeżeli grupą byśmy obięli cały wzorzec, wraz z, wówczas już, podgrupą z metaznakiem "|" wówczas nie jest konieczne stosowanie metody re.search().group().
       # Jednakże to ma swoje konsekwencje. Takie objęcie całego wzorca w grupę wraz z podgrupą z metaznakiem "|" spowoduje, że będą zwracane dopasowania wg. zasady kolejności występowania nawiasów otwierających oznaczających początek określonej grupy. Opisywane to było w części II opisu grupowania wyrażeń regularnych.
       # A niekoniecznie takie dopasowania chcemy. Możemy chcemy dokładnie jedno występujące dopasowanie, które może być użyte dla dwóch różnych tekstów gdzie doapsowanie może się różnić tylko jedną ifnromacją. Wówczas musimy zastosować re.search().group() wraz z metaznakiem "|" objętym w grupę.
       # We wzorcach gdzie metaznak "|" został objęty grupą, a my nie chcemy obejmować większą grupą całego wzorca bo szukamy tylko konkretnego dopasowania różniącego się w różnych tekstach tylko jedną informacją składową wówczas metoda .group(0) musi mieć argument 0.
txtE19 = "Ziama obraca się 365 dni wokol slonca" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia grupowaniania metaznaku "|" wewnątrz metaznaku "()".
txtE20 = "Mars obraca się 685 dni wokol slonca" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia grupowaniania metaznaku "|" wewnątrz metaznaku "()".
print(re.search(r"(365|685).*slonca", txtE19).group(0)) # zwraca dopasowanie całego wzorca, a nie tylko tego co występuje w grupie, jak można by sądzić. W zależności czy w przeszukiwanym tekście występuje "365" czy "685" to zwróci takie dopasowanie.
                                                        # Po prostu może w tekście wystapić albo "365" albo "685". Pozostała część wzorca pozostaje niezmienna i musi wystąpić w przeszukiwanym tekście i też zostanie zwrócona jako doapsowanie.
                                                        # Bardzo dobre rozwiązanie jeżeli przeszukujemy plik tekstowy linia po lini. A szukami lini zawierających konkretne informajce.
print(re.findall(r"(365|685).*slonca", txtE19)) # zwróci dopasowanie będące albo ciągiem znaków "365" albo "685". Wynika to z tego, że nie wykorzystaliśmy metody re.search().group(0). A we wzorcu jest jedna grupa.
                                                # Nieużycie metody re.search().group(0) spowoduje, że traktujemy wzorzec normalnymi zasadami grupowania wyrażeń regularnych. Czyli dopasowanie wymaga znalezienia całego wzorca, ale jako wynik zostanie wyświetlony tylko podwzorzec z grupy. Grupa jest tylko jedna.
                                                # Pozostała część wzorca należy do grupy nieprzechwytywanej i nie będzie zwrócona jako wynik ale jest potrzebna do dopasowania.
print(re.findall(r"((365|685).*slonca)", txtE19)) # zwraca dwa dopasowania, ponieważ są dwie grupy. Przyczym druga grupa jest podgrupą grupy pierwszej.
                                                  # Pierwszym będzie dopasowanie zgodne ze wzorcem zawartym w pierwszej grupie, łącznie z podwzorcem wchodzącym w skład podgrupy. Czyli z grupą zagnieżdżoną.
                                                  # A więc pierwsze dopasowanie będzie zawierać cały wzorzec w skład którego będzie wchodzić albo ciąg znaków "365" albo ciąg znaków "685".
                                                  # Drugie dopasowanie będzie zgodne z podwzorcem wchodzącym w skłąd podgrupy. I będzie to tylko ciąg znaków "365" albo ciąg znaków "685".
                                                  # Jeżeli jakieś elementy wzroca znajdowałyby się poza grupami to one byłby wymagane w trakcie szukania dopasowania, ale ich znaki w dopasowaniu nie były zwracane. Należały do tak zwanej grupy nieprzechwytywanej.
print(re.search(r"(365|685).*slonca", txtE20).group(0)) # zwraca dopasowanie całego wzorca, a nie tylko tego co występuje w grupie, jak można by sądzić. W zależności czy w przeszukiwanym tekście występuje "365" czy "685" to zwróci takie dopasowanie.
                                                        # Po prostu może w tekście wystapić albo "365" albo "685". Pozostała część wzorca pozostaje niezmienna i musi wystąpić w przeszukiwanym tekście i też zostanie zwrócona jako doapsowanie.
                                                        # Bardzo dobre rozwiązanie jeżeli przeszukujemy plik tekstowy linia po lini. A szukami lini zawierających konkretne informajce.
print(re.findall(r"(365|685).*slonca", txtE20)) # zwróci dopasowanie będące albo ciągiem znaków "365" albo "685". Wynika to z tego, że nie wykorzystaliśmy metody re.search().group(0). A we wzorcu jest jedna grupa.
                                                # Nieużycie metody re.search().group(0) spowoduje, że traktujemy wzorzec normalnymi zasadami grupowania wyrażeń regularnych. Czyli dopasowanie wymaga znalezienia całego wzorca, ale jako wynik zostanie wyświetlony tylko podwzorzec z grupy. Grupa jest tylko jedna.
                                                # Pozostała część wzorca należy do grupy nieprzechwytywanej i nie będzie zwrócona jako wynik ale jest potrzebna do dopasowania.
print(re.findall(r"((365|685).*slonca)", txtE20)) # zwraca dwa dopasowania, ponieważ są dwie grupy. Przyczym druga grupa jest podgrupą grupy pierwszej.
                                                  # Pierwszym będzie dopasowanie zgodne ze wzorcem zawartym w pierwszej grupie, łącznie z podwzorcem wchodzącym w skład podgrupy. Czyli z grupą zagnieżdżoną.
                                                  # A więc pierwsze dopasowanie będzie zawierać cały wzorzec w skład którego będzie wchodzić albo ciąg znaków "365" albo ciąg znaków "685".
                                                  # Drugie dopasowanie będzie zgodne z podwzorcem wchodzącym w skłąd podgrupy. I będzie to tylko ciąg znaków "365" albo ciąg znaków "685".
                                                  # Jeżeli jakieś elementy wzroca znajdowałyby się poza grupami to one byłby wymagane w trakcie szukania dopasowania, ale ich znaki w dopasowaniu nie były zwracane. Należały do tak zwanej grupy nieprzechwytywanej.
txtE21 = "I love dogs" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia grupowaniania metaznaku "|" wewnątrz metaznaku "()".
txtE22 = "I love seals" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia grupowaniania metaznaku "|" wewnątrz metaznaku "()".
print(re.search(r".*(dogs|seals)", txtE21).group(0)) # zwraca dopasowanie całego wzorca, a nie tylko tego co występuje w grupie, jak można by sądzić. W zależności czy w przeszukiwanym tekście występuje "dogs" czy "seals" to zwróci takie dopasowanie.
                                                     # Po prostu może w tekście wystapić albo "dogs" albo "seals". Pozostała część wzorca pozostaje niezmienna i musi wystąpić w przeszukiwanym tekście i też zostanie zwrócona jako doapsowanie.
                                                     # Bardzo dobre rozwiązanie jeżeli przeszukujemy plik tekstowy linia po lini. A szukami lini zawierających konkretne informajce.
print(re.findall(r".*(dogs|seals)", txtE21)) # zwróci dopasowanie będące albo ciągiem znaków "dogs" albo "seals". Wynika to z tego, że nie wykorzystaliśmy metody re.search().group(0). A we wzorcu jest jedna grupa.
                                             # Nieużycie metody re.search().group(0) spowoduje, że traktujemy wzorzec normalnymi zasadami grupowania wyrażeń regularnych. Czyli dopasowanie wymaga znalezienia całego wzorca, ale jako wynik zostanie wyświetlony tylko podwzorzec z grupy. Grupa jest tylko jedna.
                                             # Pozostała część wzorca należy do grupy nieprzechwytywanej i nie będzie zwrócona jako wynik ale jest potrzebna do dopasowania.
print(re.findall(r"(.*(dogs|seals))", txtE21)) # zwraca dwa dopasowania, ponieważ są dwie grupy. Przyczym druga grupa jest podgrupą grupy pierwszej.
                                               # Pierwszym będzie dopasowanie zgodne ze wzorcem zawartym w pierwszej grupie, łącznie z podwzorcem wchodzącym w skład podgrupy. Czyli z grupą zagnieżdżoną.
                                               # A więc Pierwsze dopasowanie będzie zawierać cały wzorzec w skład którego będzie wchodzić albo ciąg znaków "dogs" albo ciąg znaków "seals".
                                               # Drugie dopasowanie będzie zgodne z podwzorcem wchodzącym w skłąd podgrupy. I będzie to tylko ciąg znaków "dogs" albo ciąg znaków "seals".
                                               # Jeżeli jakieś elementy wzroca znajdowałyby się poza grupami to one byłby wymagane w trakcie szukania dopasowania, ale ich znaki w dopasowaniu nie były zwracane. Należały do tak zwanej grupy nieprzechwytywanej.
print(re.search(r".*(dogs|seals)", txtE22).group(0)) # zwraca dopasowanie całego wzorca, a nie tylko tego co występuje w grupie, jak można by sądzić. W zależności czy w przeszukiwanym tekście występuje "dogs" czy "seals" to zwróci takie dopasowanie.
                                                     # Po prostu może w tekście wystapić albo "dogs" albo "seals". Pozostała część wzorca pozostaje niezmienna i musi wystąpić w przeszukiwanym tekście i też zostanie zwrócona jako doapsowanie.
                                                     # Bardzo dobre rozwiązanie jeżeli przeszukujemy plik tekstowy linia po lini. A szukami lini zawierających konkretne informajce.
print(re.findall(r".*(dogs|seals)", txtE22)) # zwróci dopasowanie będące albo ciągiem znaków "dogs" albo "seals". Wynika to z tego, że nie wykorzystaliśmy metody re.search().group(0). A we wzorcu jest jedna grupa.
                                             # Nieużycie metody re.search().group(0) spowoduje, że traktujemy wzorzec normalnymi zasadami grupowania wyrażeń regularnych. Czyli dopasowanie wymaga znalezienia całego wzorca, ale jako wynik zostanie wyświetlony tylko podwzorzec z grupy. Grupa jest tylko jedna.
                                             # Pozostała część wzorca należy do grupy nieprzechwytywanej i nie będzie zwrócona jako wynik ale jest potrzebna do dopasowania.
print(re.findall(r"(.*(dogs|seals))", txtE22)) # zwraca dwa dopasowania, ponieważ są dwie grupy. Przyczym druga grupa jest podgrupą grupy pierwszej.
                                               # Pierwszym będzie dopasowanie zgodne ze wzorcem zawartym w pierwszej grupie, łącznie z podwzorcem wchodzącym w skład podgrupy. Czyli z grupą zagnieżdżoną.
                                               # A więc pierwsze dopasowanie będzie zawierać cały wzorzec w skład którego będzie wchodzić albo ciąg znaków "dogs" albo ciąg znaków "seals".
                                               # Drugie dopasowanie będzie zgodne z podwzorcem wchodzącym w skłąd podgrupy. I będzie to tylko ciąg znaków "dogs" albo ciąg znaków "seals".
                                               # Jeżeli jakieś elementy wzroca znajdowałyby się poza grupami to one byłby wymagane w trakcie szukania dopasowania, ale ich znaki w dopasowaniu nie były zwracane. Należały do tak zwanej grupy nieprzechwytywanej.
# IV. - Wyodrębnianie grup za pomocą metody re.search().group() pokazuje, że każda grupa ma swój alias - numer znalezionej grupy w przeszukiwanym tekście.
      # Numer grupy wynika z kolejności przeszukiwanych grup. Kolejność jest wyznaczana zasadą występowania nawiasu otwierającego grupę licząc od lewej. Ta grupa jest pierwsza której nawias otwierający jest pierwszy we wzorcu.
      # Metody .group() w celu odniesienia się do konkretnej grupy używamy w momencie kiedy stosujemy metodę re.search(). Metoda ta zwraca obiekt typu Match.
      # Jednak jest jeszcze jeden sposób na odniesienie się do konkretnej grupy.
      # Sposób ten używamy z metodą re.sub(). Czyli metodą do zmiany znalezionego dopasowania na inny tekst.
      # Oznacza to, że nowy sposób odnoszenia się do grup dotyczyć będzie sytuacji w których będziemy chcieli zamienić miejscami dopasowania znalezione w przeszukiwanym tekście za pomocą grup. Jest to bardzo pomocna funkcja aliasów grup.
      # Dlaczego stosowanie aliasów grup w połączeniu z metodą re.sub() spowoduje zamianę miejscami znalezionych grup ?
      # Wynika to ze składni metody re.sub() i wynikającej z niej możliwości stosowania aliasów grup.
      # Metoda re.sub() ma następującą składnię:
      # re.sub("wzorzec", "tekstZastępującyWzorzecz", "przeszukiwany tekst")
      # I właśnie w sekcji "tekstZastępującyWzorzecz" używamy odnoszenia się do znalezionych grup.
      # Do grup odnosimy się w następujący sposób: r"\numerGrupy" jeżeli zastosujemy symbol "r" jako przetwarzanie surowego tekstu lub "\\numerGrupy" jeżeli nie zastosujemy symbolu "r" surowego tekstu.
      # Oczywiści symbol przetwarzania surowego tekstu umieszczamy przed tekstem który ma być bym który zastępuje dopaswoanie. A więc:
      # r"tekstZastępującyWzorzecz"
      # Należy pamiętać, że numeracja grup następuje według zasady występowania nawiasów otwierających, licząc od lewej.
      # Przykładowe zapisanie sekcji zastepującej wzorzec:
      # r"\2 \3 \1" - oznacza to, że wzorzec tekstu którego szukamy do zamiany, zawiera co najmenij trzy grupy.
                    # Znalezione dopasowanie zastapimy tekstem według wzorca:
                    # - jako pierwszy będzie ciąg znaków znaleziony według drugiej z kolei grupy we wzorcym
                    # - następnie będzie spacja
                    # - kolejnym ciagiem znaków będzie ciąg znaleziony według trzeciej z kolei grupy we wzorcu
                    # - następnie będzie znowu spacja
                    # - ostatnim ciągiem znaków będzie ciąg znaleziony według pierwszej z kolei grupy we wzorcu.
      # Powyższe świadczy o tym, że to w jaki sposób zapiszemy sekcję oznaczającą tekst który zastąpi nasz wzorzec, to tak on zostanie zastąpiony.
      # Jeżeli oprócz aliasów grup umieścimy we wzorcu jakiś inny symbol, np. spacje, to ona zostanie umieszczona w tym miejscu co we wzorcu.
      # UWAGA !! We wzorcu tekstu który zastąpi tekst dopasowany nie mają zastosowania symbole wyrażeń regularnych poza odnośnikami aliasów do grup.
      # Często mamy dłuższy tekst, zdanie w którym chcemy zamienić miejscami konkretne słowa.
      # W takim wypadku we wzorcu który będzie szukać dopasowania musimy zgrupować nie tylko wyrażenia regularne które odnoszą się do tych dwóch słów, które chcemy zamnieć miejscami, ale również pozostałe ciągi znaków wchodzące w skład tekstu, zdania.
      # Tak by wykorzystując aliasy grup poskładać tekst, zdanie w taki sposób aby zamiana miejscami dotyczyła tylko tych konkretych słów.
      # Wówczas, aby to zrobić, we wzorcu, który zastapi nasze znalezione dospasowanie, będziemy używać aliasów do konkretnych grup aby poskładać z nich poprawnie tekst, zdanie.
      # Dlatego tak, ważne jest poprawnie zapisanie wzorca dopasowania oraz wzorca zawracajacego tekst którym zastępujemy znalezione dopasowanie.
      # Poniższy przykłąd pomoże to zrozumieć.
txtE23 = "Mam Ducati a chce kupic Kawasaki" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia stosowania aliasów grup.
print(re.sub(r"(.+)(\bD\w+)(.+)(\bK\w+)", r"\1\4\3\2", txtE23)) # chcemy zamienić miejscami wyrazy "Ducati" i "Kawasaki".
                                                                # Cały wzorzec podzieliliśmy na grupy z których żadna nie jest grupą zagnieżdżoną,
                                                                # Dwie najważniejsze grupy to grupy nr 2 której wyrażenie regularne jest: "(\bD\w+)", szuka ono wyrazu "Ducati i grupa nr 4 której wyrażenie regularne jest: "(\bK\w+)", szuka ono wyrazu "Kawasaki". Grupy liczymy według zasady występowania nawiasów otwierających.
                                                                # Grupa nr 2 wyszukuje wyrazów rozpoczynających się na literę "D". Grupa nr 4 wyszukuje wyrazów rozpoczynających się na liternę "K".
                                                                # Grupa nr 1 i grupa nr 3 to grupy które szukają ciągów znaków występujących pomiędzy wyrazami szukanymi przez grupy nr 2 i 4.
                                                                # Taki podział na grupy jest konieczny ponieważ pomimo, że chcemy zamienić miejscami dwa wyrazy to pozostały szyk znadania chcemy zostawić bez zmian.
                                                                # Tak przygotowane grupy pozwalają nam zapisać wzorzec którym zamienimy znalezione dopasowania.
                                                                # Ten wzorzec to: r"\1\4\3\2".
                                                                # Wyczytamy z niego, że na początku zwróconego tekstu będzie dopasowanie znalezione przez grupę nr 1. Czyli początek tekstu, przed wyrazem "Ducati".
                                                                # Następnie będzie tekst z dopasowania grupy nr 4, czyli znaleziony wyraz "Kawasaki".
                                                                # Następnie będzie dopasowanie znalezione dla grupy 3. Czyli tekst pomiędzy wyrazami "Ducati", a "Kawasaki". Oczywiście tekst pomiędzy tymi słowami z dopasowania pierwotnego tekstu.
                                                                # I na samym końcu będzie tekst z dopasowania grupy nr 2, czyli znaleziony wyraz "Ducati".
                                                                # Proszę zwrócić uwagę, że we wzorcu który będzie zastępował tekst nie użyliśmy żadnych znaków białych ponieważ one zawierają się w grupach nr 1 i 3. Bo tak skonstruowaliśmy wyrażenia regularne dla tych grup, żeby zawierały znaki białe (spacje).
                                                                # A więc jako wynik działania tej metody będzie tekst w którym wyrazy "Ducati" i "Kawasaki" zostaną zastąpione miejscami.
                                                                # Pozostała część zdania się nie zmieni.
# V. - grupy w połączeniu z metaznakami oznaczającymi ilość wystąpień: *, +, ?, {n,m}
     # Stosowanie metaznaków oznaczających ilość wystapień dotyczy znaku zapisanego bezpośrednio przed nimi. Dotyczy to tylko jednego znaku umieszczonego bezpośrednio przed metaznakiem określającym ilość.
     # Niekiedy definiując ciągów znaków we wzorcu chcemy aby traktować pewien ciąg jako jeden spójny, nierozdzielalny kawałek i szukać ilości jego wystąpień po sobie. Ale, właśnie, jako całęgo kawałka teksu, pewnego ciągu znaków, a nie tylko jednego znaku umieszczonego przed metaznakiem oznaczającym ilość.
     # I właśnie tutaj przydają się grupy.
     # Wówczas we wzorcu ujmujemy w nawiasy segment, kawałek tekstu, który ma stanowić całość. Metaznak oznaczający ilość nie będzie odnosi się wtedy do ostatniego znaku, ale do całęgo ciągów znaków, segmentu, który ujeliśmy w grupe.
     # Ten ciąg znaków, segment, kawałek tekstu, ujęty w grupę we wzrocu będzie szukany dokładnie tak jak został zapisany.
     # W zależności od tego jaki metaznak oznaczający ilość zastosujemy po fragmencie tekstu objętym w grupę to będziemy szukać dopasoawnia w którym ta grupa tekstu dokładnie tak jak została zapisana we wzrocu będzie wystepować określoną przez metaznak ilość razy po sobie.
     # Takie połączenie grup i znaków określających ilość zawsze musi się odbywać wraz z metodą re.search(wzorzec,tekst).group(Num). Ta metoda i jej wykorzystanie była opisywana w części II opisu grupowania wyrażeń regularnych.
     # Gdybyśmy nie zastosowali metody re.search().group() wówczas wynikiem dopasowania nie byłoby dokłądne dopasowani, a byłby dopasowania związane tylko i wyłącznie z zawartością grupy.
     # UWAGA !! Przeszukiwanie ilości wystapień tekstu ujętego w grupę według metaznaku nastepuje od lewej do prawej.
              # A więc jeżeli znajdziemy tekst który pasuje do wzorca przy maksymalnej mozliwej ilości wystapień po sobie to zwracany jest on od razu.
              # Nie będą zwracane dopasowania które by świadczyły o mniejszej ilości wystąpień, nawet jeżeli będą występować.
              # Po prostu zawsze szukane jest dopasowanie zawierające największą możliwą ilość wystąpień. Oczywiście mieszczące się w granicach ilości wstazywanych przez metaznak.
txtE24 = "cocoty mowisz ?" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia stosowania grup w połączeniu z metaznakami określającymi ilość wystapień po sobie.
print(re.search(r"(co)+t", txtE24).group(0)) # zwrócone zostanie dopasowanie w którym ciąg znaków "co" wystepuje po sobie conajmniej raz i dodatkowo po ostatnim możliwym wystapieniu ciągu "co" znajduje się znak "t".
                                             # W przeszukiwanym tekście znajduje się fragment w którym znajdziemy nasze doapsowanie, to znaczy: "cocot".
                                             # Została zastosowana zasada
txtE25 = "cocotcoty mowisz ?" # zmienna tekstowa będąca przeszukiwanym tekstem w poszukiwaniu wzorca. Wykorzystywana do omówienia stosowania grup w połączeniu z metaznakami określającymi ilość wystapień po sobie.
print(re.search(r"(cot){1}y", txtE25).group(0)) # zwrócone zostanie dopasowanie w którym ciąg znaków "cot" wystepuje tylko raz i dodatkowo po nim następuje literka "y".
# VI - Lookarounds

#/////////////////
# Wykorzystanie wyrażeń regularnych

# Opisane metaznaki używane w wyrażeniach regularnych możemy łączyć ze sobą w potężne wzorce.
# Takie wzorce pomogą nam sprawnie i bezbłędnie szukać wymaganych informacji.
# Które potem mogą nam posłużyć do dalszego ich przetwarzania, bądź do wykonania innych operacji po znalezieniu wzorca.

# Do ćwiczenia wyrażeń regularnych polecam stronę internetową gdzie będziemy mogli przećwiczyć stosowanie prostych wyrażń jak ich skomplikowanych połączeń:
# https://regex101.com
