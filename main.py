# 0 kolumna nazwa 1 kolumna liczba 2 kolumna typ 3 kolumna hp 4 kolumna atak 5 kolumna broń 6 kolumna amunicja 7 kolumna przładowyanie 8 kolumna max amunicji 9 kolumna ruch/max	10 kolmna czy jest to karta jedno razowa 11	czy jest tylko na daną jednostke
import io
import sys
import csv
import random

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
karty = []
karty_gracza = [[], [], []]  
aktualny_gracz = 1


class Card:
    def __init__(self, type, name, atak, hp):
        self.name = name
        self.type = type
        self.atak = int(atak)
        self.hp = int(hp)

    def __str__(self):
        return f'{self.name} {self.type} {self.hp} {self.atak}'


def read_cards():
    with open('karty.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for i in range(int(row[1])):
                karty.append(Card(row[2], row[0], row[4], row[3]))


read_cards()
random.shuffle(karty)
'''for card in karty:
    print(card)'''


# pokaż graczowi 4 karty z wierzchu tablicy (z numerami 1 2 3 4)
def proponowane_Karty():
    proponowaneKarty = []
    for i in range(4):
        proponowanaKarta = karty.pop()
        proponowaneKarty.append(proponowanaKarta)

    print(f"Graczu nr {aktualny_gracz}, masz do wyboru takie karty: ", end=' ')
    for numer, karta in enumerate(proponowaneKarty):
        print(f"{numer+1}) {karta.name}, ", end=' ')
    print()

    return proponowaneKarty


def wyborKart():
    wybor = input(f"Wpisz którą karte wybierasz:")
    karty_wybrane = wybor.split(",")
    print(karty_wybrane)
    return karty_wybrane


def usuwanieIDodawanieKart(proponowane_karty, karty_wybrane):
    for i in karty_wybrane:
        karta_dla_gracza = proponowane_karty.pop(int(i) - 1)
        karty_gracza[aktualny_gracz].append(karta_dla_gracza)  

    for a in proponowane_karty:
        karty.append(a)  


def atakuj():
    if aktualny_gracz == 2:
        hp = 0
        for karta in karty_gracza[1]:
            hp += karta.hp
        atak = 0
        for karta in karty_gracza[2]:
            atak += karta.atak
        liczba_kart = len(karty_gracza[1])
        
        if liczba_kart > 0: 
          for karta in karty_gracza[1]:
              karta.hp -= atak / liczba_kart
              if karta.hp <= 0: 
                  karty_gracza[1].remove(karta)


    if aktualny_gracz == 1:
        hp = 0
        for karta in karty_gracza[2]:
            hp += karta.hp
        atak = 0
        for karta in karty_gracza[1]:
            atak += karta.atak
        liczba_kart = len(karty_gracza[2])

        if liczba_kart > 0:  
          for karta in karty_gracza[2]:
              karta.hp -= atak / liczba_kart
              if karta.hp <= 0: 
                  karty_gracza[2].remove(karta)



def jakie_masz_karty(aktualny_gracz):
    print(f'Gracz {aktualny_gracz} ma takie karty:')
    for karta in karty_gracza[aktualny_gracz]:
        print(karta.name)
        print(f'Atak: {karta.atak}')
        print(f'HP: {karta.hp}')


while True:
    proponowane_karty = proponowane_Karty()
    karty_wybrane = wyborKart()
    usuwanieIDodawanieKart(proponowane_karty, karty_wybrane)
    jakie_masz_karty(aktualny_gracz) 
    odpowiedź_gracza = input("Czy chcesz zaatakować przeciwnika? (tak/nie): ") 
    if odpowiedź_gracza.lower() == "tak":  
        print("Zaatakowałeś przeciwnika!")
        atakuj()

    if aktualny_gracz == 1:
        aktualny_gracz = 2
    else:
        aktualny_gracz = 1
#nie usuwać pomysły
#amunicje z przeładywniem
#ruch
#wczytać reszte kart
#podzielic karty na jednorazowe i niejednorazowe 
#podzielic karty na obronne i ofensywne