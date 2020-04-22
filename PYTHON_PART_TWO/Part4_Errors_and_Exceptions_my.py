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
# Jednak w przypadku obsługi błędów to kod zapisany w tym blok zostanie wywołany, jezeli kod z bloku try nie zwróci błędów (stąd nazwa tego bloku, else - jeszcze, oprócz ten kod też będzie wykonany).
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
#        Kod który zostanie wykonany jeżeli kod z bloku try nie zwróci błędu. Należy pamiętać, że kod z bloku try jeżeli nie wywołuje błędu to jest wykonywany a zaraz po nim jest wykonywany kod z bloku else
#        ...

# Dla lepszego zrozumienia poniżej zostaną wykonane pomocne przykłady.

# Przykład 1:

try:
    f = open('testfile','w')
    f.write('Test write this')
    print("Stworzono nowy plik oraz zapisano w nim nową zawartość - przykład 1, kod z bloku try")
except IOError:
   print("Error: Could not find file or read data")
else:
   print("Wczytano poprawnie zawartość nowego pliku - przykład 1, kod z bloku else")
   f.close()

# Przykład 2:

try:
    f = open('testfile','r')
    f.write('Test write this')
    print("Stworzono nowy plik oraz zapisano w nim nową zawartość - przykład 2, kod z bloku try")
except IOError:
   print("Błąd, nie można wczytać bądź odnaleźć pliku - przykład 2, kod z bloku except")
else:
   print("Wczytano poprawnie zawartość - przykład 2, kod z bloku else")
   f.close()


# Great! Notice how we only printed a statement! The code still ran and we were
# able to continue doing actions and running code blocks. This is extremely
# useful when you have to account for possible input errors in your code.
# You can be prepared for the error and keep running code, instead of your code
# just breaking as we saw above.
#
# We could have also just said except: if we weren't sure what exception would occur.
# For example:

try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
   print("Error: Could not find file or read data")
else:
   print("Content written successfully")
   f.close()


# Great! Now we don't actually need to memorize that list of exception types!
# Now what if we kept wanting to run code after the exception occurred? This is
#  where **finally** comes in.

###################
# finally
###################

# The finally: block of code will always be run regardless if there was an
# exception in the try code block. The syntax is:
#
#     try:
#        Code block here
#        ...
#        Due to any exception, this code may be skipped!
#     finally:
#        This code block would always be executed.
#
# For example:

try:
   f = open("testfile", "w")
   f.write("Test write statement")
finally:
   print("Always execute finally code blocks")



# **Great! Now you know how to handle errors and exceptions in Python with the
# try, except, else, and finally notation!**
