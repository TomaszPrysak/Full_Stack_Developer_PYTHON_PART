#!/usr/bin/env python
# -*- coding: utf-8 -*-

# W Pythonie podczas definiowania funkcji mamy możliwość tworzenia kilkulinijkowych
# komentarzy które są wykorzystywane do opisywania funkcji przez środowisko IDE w którym pracujemy.
# W momencie kiedy chcemy wywołać naszą funkcję i środowisko IDE będzie nam podpowadać
# możliwe funkcje to wyświetli nam się okienko z informacją co nasza funkcja wykonuje.
# Te wielolinijkowe komentarze twrzymy pomiędzy parą złożoną z potrójego cudzysłowa: """
# Przykład mamy poniżej.

def my_func(parametr="mój parametr default"):
    """
    Opisa działania funkcji
    Opis ten wyświetla się w środowisku IDE
    w momencie kiedy środowisko nam podpowiada jaką chcemy użyć funkcję.
    Od razu dostajemy informację o funkcji
    """
    print("To jest moja funkcja z {x} i opisem w IDE".format(x=parametr))


my_func()

# Przykłady funkcji:

# Przykład 1:
def hello():
    """
    Bez argumentów
    """
    return "hello" # wynik działania tej funkcji będzie zwracany
                   # w miejscu gdzie wywołujemy tą funkcję,
                   # czyli tak naprawdę możemy przypisać wywołanie tej funkcji do jakiejś zmiennej,
                   # tak jak to zostało przedstawione poniżej

result1 = hello()
print(result1)

# Przykład 2:
def addNum(num1, num2):
    """
    Argumenty num1, num2 muszą być liczbami całkowitymi
    """
    if type(num1) == type(num2) == type(10): # przykład ze sprawdzaniem czy argumenty które przekazujemy do funkcji
                                             # są typu który jest potrzebny do prawidłowego działania funkcji.
                                             # sprawdzenie dokonuje się za pomocą metody type().
                                             # metoda ta zwraca klasę do jakiej należy obiekt który umieścimy w metodzie type()
                                             # należy pamiętać, że liczba całkowita jest klacy "integer, jakiś tekst klasy "string",
                                             # dlatego podczas sprawdzenia w tej funkcji porównujemy czy argumenty przekazywane do funkcji
                                             # są tego samego typu co liczba 10, a więc będziemy mieć pewność, że jest klasy "integer
        return num1 + num2
    else:
        return "Musisz podać liczby całkowite"

print(addNum(2,2))

# Wyrażenie LAMBDA

# W niektórych przypadkach nie ma sensu używać dużej funkcji.
# LAMBDA to funkcja jednolinijkowa, nie posiadająca nazwy, ponieważ wywołujemy ją w jednym konkretnym miejscu,
# w którym chcemy dokonać jakiś operacji. Jeżeli chcielibyśmy podobnych operacji dokonać w innym miejscu wówczas musimy
# jeszcze raz użyć LAMBDY.
# Często wyrażenie LAMBDA wykożystujemy po to aby dokonać operacj na każdym elemencie jakiejś kolekcji.
# Wówczas wyrażenie to stosujemy z innymi metodami.

# Metody z którymi stosujemy wyrażenie LAMBDA:

# filter(funkcja, kolekcjaElementów) - metoda zwraca te elementy z kolekcjiElementów na których operacje
#                                      występujących w funkcji jest możliwe do wykonania. Możliwośc wykonania
#                                      operacji zwraca do wiadomości funkcji filter() wartość TRUE. Dzięki temu funkcja ta wie które elemnty zwrócić.
#                                      Zwracane elemenety kolekcji są w oryginalne postaci, nie przetworzone przez funkcje.
#                                      Jednym słowem metoda filter() wykorzystywana jest do sprawdzania możliwości wykonania funkcji
#                                      na elementach kolekcji.

mojaLista = [1,2,3,4]
result2 = filter(lambda x: x%2 == 0, mojaLista) # na każdym elemencie kolekcji mojaLista wykonywane jest wyrażenie LAMBDA.
#                                                Działa to tak, że każdy element listy jest przypisywany do zmiennej operacyjnej x,
#                                                a następnie dokonywana jest operacja ze zmienną x, w tym przypadku dokonywane jest pobieranie reszty
#                                                z dzielenia elementu przez 2 i sprawdzenie czy reszta jest równa 0.
#                                                Jeżeli tak to metoda filter zwróci ten element w postaci royginalne. Doda go do nowej listy result2.
print(result2)

# Gdybyśmy nie chcieli zastosować LAMBDY wówczas musilibyśmy napisać następującą funkcję:
# def checkReszte(num):
#     return num%2 == 0
# result2 = filter(checkReszte, mojaLista)

# map(funkcja, kolekcjaElementów) - metoda ta jest bardzo podobna do metody filter(). Jednak w tym przypadku
#                                   na każdym elemencie z kolekcjiElementów wykonywana jest operacja zapisana w funkcji.
#                                   I zwracany jest wynikowy, końcowy, już "przeliczony" element z kolekcjiElementów.

mojaLista2 = [1,"2",3,"4"]
result3 = map(lambda x: x*2, mojaLista2) # na każdym elemencie kolekcji mojaLista2 wykonywane jest wyrażenie LAMBDA.
#                                          Działa to tak, że każdy element listy jest przypisywany do zmiennej operacyjnej X,
#                                          a nastepnie dokonywana jest operacje ze zmienną X, w tym przypadku dokonywane jest podwojenie zmiennej X o 2.
#                                          A nastepnie wynik podowjenia zmiennej X jest zwracany i dodawany do nowej listy result3.
print(result3)

# Gdybyśmy nie chcieli zastosować LAMBDY wówczas musilibyśmy napisać następującą funkcję:
# def multiplitaction(num):
#     return num*2
# result3 = map(checkReszte, mojaLista)

# Przykładowe wbudowane funkcje różnych obiektów:

string = 'hello'
print(string.lower()) # lower() zamienia wszystkie znaki w tekście na małe litery
print(string.upper()) # upper() zamienia wszystkie znaki w tekście na wielkie litery
print(string.split()) # split() dzieli tekst z wykorzystaniem okreslonego znaku, w naszym przypadku nie podaliśmy żdnego znaku podziału, dlatego znakiem podziału jest spacja,
#                       i po podzieleniu umieszcza poszczególne części tekstu w liście. W tym przypadku nie było spacji więc cały tekst umieszczono w liście. I teraz zawiera jeden element.

tweet = "Go Sports! #Sports"
print(tweet.split()) # split() dzieli tekst z wykorzystaniem spacji i umieszcza cześci tekstu w liście w kolejności w jakiej występowały w tekście
#                      pierszym elementem listy będzie "Go", drugim "Sports!", a trzecim: "#Sports"
print(tweet.split("#")) # spit("#") dzielimy tekst wykorzystując znak podziału: "#". Pierwszym elementem listy będzie: "Go Sports! ", a drugim: "Sports",
#                         warto zauważyc, że znak podziału nie jest brany do żadnego elementu listy, po prostu przepada.
print(tweet.split("#")[1]) # po podziale tesktu z wykorzystaniem split("#") zwracamy drugi element listy

d = {'k1':1,'k2':2}
print(d.keys()) # keys() zwraca listę wszystkich kluczy w słowniku
print(d.items()) # items() zwraca listę dwuelementowych krotek, gdzie pierwszym elementem krotki jest klucz, a drugim wartośc do tego klucza przypisana

lst = [1,2,3]
x = lst.pop() # pop() zwraca ostatni element z listy i jednocześnie usuwa go z listy.
print(x)
print(lst)

print("x" in [1,2,3]) # sprawdzamy czy tekst "x" jet w kolekcji elementów, zwracana jest wartość prawda fałsz.
print("x" in ["x","y","z"]) # sprawdzamy czy tekst "x" jet w kolekcji elementów, zwracana jest wartość prawda fałsz.
