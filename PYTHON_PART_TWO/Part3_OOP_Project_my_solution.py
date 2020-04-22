#############################################
### PROJEKT Z PROGRAMOWANIA OBIEKTOWEGO #####
#############################################

# Projekt dotyczy stworzenia gry karcianej wykorzystując programowanie obiektowe.
# Będzie to gra w wojne dla gry jednoosobowej, tzn. gracz przeciwko komputerowi.
# Zasady gry:
# Talia kart jest tasowana i dzielona równomiernie na każdego z graczy (gracz i komputer). Każdy otrzymuje 26 kart.
# Rozdawanych po kolei, naprzemiennie. Gracze nie widzą swoich kart. Dosatają stos swoich kart symbolami do dołu.
# Następnie gracze w tej samej chwili odkrywają  pierwszą kartę ze swojego stosu.
# Garcz którego kartą jest wyższa bierze swoją kartę i kartę przeciwnika i odkłada je zakryte u siebie na osobnym stosie.
# Jeżeli karty mają tę samą wartośc zaczyna się Wojna.
# Wówczas każdy z graczy dobiera jedną zakrytą kartę ze swojego stosu i kładzie ją na karcie która zapoczątkowała wojnę.
# Każdy z gray ma wówczas przed sobą dwie karty: jedną na spodzie odkrytą i drugą na nie zakrytą.
# Następnie gracze w tej samamej okrywają kolejną kartę. Jeżeli jeden z graczy ma kartę o wyższej wartości wówczas wygrywa karty które brały udział w wojnie.
# Czyli te co były odkryte i te co były zakryte.
# Wojna trwa do momentu kiedy jeden z graczy będzie miał wyższą kartę. Im dłużej trwa wojna tym więcej kart jest do wygrania za jednym razem.

import random
import itertools

# Dwie kolekcje elementów które mogą być przydatne
suite = 'S D W Z'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
highRanksDict = {"J":11, "Q":12, "K":13, "A":14}

class Deck():
    """
    To jest klasa Deck (talia). Klasa ta powinna mieć zdefiniowane następujące metody:
    - tworzenia listy z talią kart
    - tasowanie powstałej listy z talią kart, po to abyśmy mogli sami inicjować tasowanie tali kart,
      dlatego ważne aby metoda tworząca talię kart nie tasowała jej tylko wywoływała metodę tasującą
    - podział tali kart na dwie osobne talie dla każdego z graczy, ważne jest to aby podział tali na dwie odbywał się po kolei, jedna karta po drugiej,
      a nie w ten sposób, że pierwsza połowa dla pierwszego gracza, druga połowa dla drugiego gracza,
    """
    def __init__(self):
        print("Utworzona została talia kart")
        self.deck = [(b, a) for a, b in itertools.product(suite, ranks)]

    def shuffleDeck(self):
        print("Talia kart została potasowana")
        random.shuffle(self.deck)

    def splitDeck(self):
        print("Rozdano karty graczom")
        return (self.deck[0::2][::-1], self.deck[1::2][::-1])

class Hand(Deck):
    """
    To jest klasa Hand (ręka). Klasa ta zawiera karty gracza. Powinna mieć zdefiniowane następujące metody:
    - usuwanie pierwszej karty z talii, w celu jej zagrania,
    - w momencie dodawania wygranych kart do swojej tali na sam koniec, aby można było nimi grać jak się skończą karty z pierwszego rozdania,
    - sprawdzanie ile zostało kart na w tali gracza.
    """
    def __init__(self, cards):
        self.cards = cards

    def removeFirstCardToTable(self):
        return self.cards.pop()

    def getAllCardFromTable(self, cardOnTable):
        self.cards.extend(cardOnTable)

    def qtyCardsHand(self):
        return len(self.cards)

class Player(Hand):
    """
    To jest klasa Player (gracz). Klasa ta zawierająca dane gracza powinna mieć zdefiniowane następujące metody:
    - przypisywanie imienia gracza,
    - zagranie karty, metoda ta łączyć się będzie z metodą z klasy Hand(),
    - sprawdzenie czy gracz ma jeszcze karty w tali.
    """
    def __init__(self, imie, hand):
        self.imie = imie
        self.hand = hand

    def playCard(self):
        zagranaKarta = self.hand.removeFirstCardToTable()
        print("{x} zagrał: {y}{z}".format(x=self.imie, y=zagranaKarta[0], z=zagranaKarta[1]))
        return zagranaKarta

    def still_has_cards(self):
        return len(self.hand.cards) != 0

def turnMenu():
    action = input("(W)yłóż kartę na stół, (P)rzerwij grę, Twój wybór: ")
    while (action != "W" and action != "w" and action != "P" and action != "p"):
        action = input("Wprowadzono nieprawidłowy klawisz, popraw się, (W)yłóż kartę na stół, (P)rzerwij grę, Twój wybór: ")
    if action == "W" or action == "w":
        return True
    elif action == "P" or action == "p":
        return False

def decodeRankCard(card):
    if card[0] in "JQKA":
        # print(highRanksDict[card[0]])
        return highRanksDict[card[0]]
    else:
        # print(int(card[0]))
        return int(card[0])

##################################
#### Niech się zacznie gra #######
##################################
print("Witaj na wojnie...")
print("")

talia = Deck()
# print(talia.deck)
talia.shuffleDeck()
# print(talia.deck)
firstPlayerDeck, secondPlayerDeck = talia.splitDeck()
# print(firstPlayerDeck)
# print(secondPlayerDeck)

nameHuman = "Człowiek"
nameComputer = "komputer"
playerList = [nameHuman, nameComputer]

random.shuffle(playerList)
random.shuffle(playerList)
random.shuffle(playerList)
random.shuffle(playerList)
random.shuffle(playerList)
# print(playerList)

if playerList[0] == "komputer":
    computer = Player(nameComputer, Hand(firstPlayerDeck))
    human  = Player(nameHuman, Hand(secondPlayerDeck))
else:
    human  = Player(nameHuman, Hand(firstPlayerDeck))
    computer = Player(nameComputer, Hand(secondPlayerDeck))

# print(human.hand.cards)
# print(computer.hand.cards)

print("Zaczynamy wojnę !!!")

cardsOnTable = []
bitwaCounter = 0

while human.still_has_cards() and computer.still_has_cards():

    # if turnMenu() == False:
    #     break

    print("Karty na stole:")

    h_card = human.playCard()
    # print(human.hand.cards)
    c_card = computer.playCard()
    # print(computer.hand.cards)

    cardsOnTable.append(h_card)
    cardsOnTable.append(c_card)

    if decodeRankCard(h_card) > decodeRankCard(c_card):
        print("Człowiek zdobywa karty ze stołu.")
        human.hand.getAllCardFromTable(cardsOnTable)
        cardsOnTable = []
        # print(cardsOnTable)
        # print(human.hand.cards)
    elif decodeRankCard(c_card) > decodeRankCard(h_card):
        print("Komputer zdobywa karty ze stołu.")
        computer.hand.getAllCardFromTable(cardsOnTable)
        cardsOnTable = []
        # print(cardsOnTable)
        # print(computer.hand.cards)
    else:
        if human.hand.qtyCardsHand() > 1 and computer.hand.qtyCardsHand() > 1:
            bitwaCounter += 1
            print("WOJNA !!!")
            h_Card_War = human.playCard()
            c_Card_War = computer.playCard()
            cardsOnTable.append(h_Card_War)
            cardsOnTable.append(c_Card_War)
            # print(cardsOnTable)
            # print(human.hand.cards)
            # print(computer.hand.cards)

    if not human.still_has_cards():
        computer.hand.getAllCardFromTable(cardsOnTable)
        cardsOnTable = []
        # computer.hand.getAllCardFromTable(human.hand.cards)
    elif not computer.still_has_cards():
        human.hand.getAllCardFromTable(cardsOnTable)
        cardsOnTable = []
        # human.hand.getAllCardFromTable(computer.hand.cards)

    print("Człowiekowi w tali zostało {x} kart, komputerowi zaś {y}".format(x=len(human.hand.cards), y=len(computer.hand.cards)))
    
if human.still_has_cards() == True:
    print("Wygrał Człwoiek :) !!")
else:
    print("Wygrał komputer :( ")

print("Liczba stoczonych bitew: " + str(bitwaCounter))
