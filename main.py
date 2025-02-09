# 0 kolumna nazwa 1 kolumna liczba 2 kolumna typ 3 kolumna hp 4 kolumna atak 5 kolumna broń 6 kolumna amunicja 7 kolumna przładowyanie 8 kolumna max amunicji 9 kolumna ruch/max	10 kolmna czy jest to karta jedno razowa 11	czy jest tylko na daną jednostke
import io
import sys
import csv
import random

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
karty = []
karty_gracza = [[], [], []]  
postawienione_karty= [[], [], []]
aktualny_gracz = 1


class Card:
    def __init__(self, type, name, atak, hp, maxa_ammo, ammo):
        self.name = name
        self.type = type
        self.atak = int(atak)
        self.hp = int(hp)
        self.maxa_ammo = int(maxa_ammo)
        self.ammo = str(ammo)
        
    def __str__(self):
        return f'{self.name} {self.type} {self.hp} {self.atak} {self.maxa_ammo} {self.ammo}'


def read_cards():
    with open('karty.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
                for i in range(int(row[1])):
                    try:
                        karty.append(Card(row[2], row[0], row[4], row[3], row[8], row[6]))
                    except:
                        print(f"Nie udało się wczytać karty {row[0]}")

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

def postawienie_karty(karta):
    print(f'Postawiasz kartę {karta}')
    if aktualny_gracz == 1:
        karty_gracza[1].remove(karta)
        postawienione_karty[1].append(karta) 

def atakuj(ktora_karta):
    print(f'Atakujesz przeciwnika')
    if aktualny_gracz == 2:
        hp = 0
        for karta in postawienione_karty[1]:
            hp += karta.hp
        atak = 0
        for karta in postawienione_karty[2]:
            atak += karta.atak
        liczba_kart = len(postawienione_karty[1])
        
        if liczba_kart > 0: 
          for karta in postawienione_karty[1]:
              karta.hp -= atak / liczba_kart
              if karta.hp <= 0: 
                  postawienione_karty[1].remove(karta)


    if aktualny_gracz == 1:
        hp = 0
        for karta in postawienione_karty[2]:
            hp += karta.hp
        atak = 0
        for karta in postawienione_karty[1]:
            atak += karta.atak
        liczba_kart = len(postawienione_karty[2])

        if liczba_kart > 0:  
          for karta in postawienione_karty[2]:
              karta.hp -= atak / liczba_kart
              if karta.hp <= 0: 
                  postawienione_karty[2].remove(karta)

#chwilowo nie działa
def przeładowanie(max_amunicja, amunicja, przeładowyanie):
    print(f'Przeładowujesz broń')        

def jakie_masz_karty_reku(aktualny_gracz):
    print(f'Gracz {aktualny_gracz} ma takie karty:')
    for karta in karty_gracza[aktualny_gracz]:
        print(karta.name)
        print(f'Atak: {karta.atak}')
        print(f'HP: {karta.hp}')

def szukaj_karty_po_nazwie(nazwa):
    for karta in karty_gracza[aktualny_gracz]:
        print(karta.name)
        if karta.name == nazwa:
            return karta
    return None

while True:
    proponowane_karty = proponowane_Karty()
    karty_wybrane = wyborKart()
    usuwanieIDodawanieKart(proponowane_karty, karty_wybrane)
    jakie_masz_karty_reku(aktualny_gracz) 
    odpowiedź_gracza = input("Czy chcesz postawić kartę? (tak/nie): ") 
    if odpowiedź_gracza.lower() == "tak":  
        ktora_karta = input(f"która kartę postawiasz?")
        znaleziona_karta=szukaj_karty_po_nazwie(ktora_karta)
        if znaleziona_karta is not None:    
            postawienie_karty(znaleziona_karta)
    odpowiedź_gracza = input("Czy chcesz zaatakować przeciwnika? (tak/nie): ") 
    if odpowiedź_gracza.lower() == "tak":  
        ktora_karta = input(f"która kartą atakujesz?")
        atakuj(ktora_karta)

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