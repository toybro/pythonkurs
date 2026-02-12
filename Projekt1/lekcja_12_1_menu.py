# +----------------+
# |     Menu       |
# |1.Dodaj         |
# |2.Odejmi        |
# |3.Podziel       |
# |4.Wylosuj liczbę|
# |                |
# |0.Koniec        |
# +----------------+
# Jaki jest twój wybór:
import random
import lekcja_12_2_moduly
print("Funckja pokaz w pliku lekcja_12_1_menu", lekcja_12_2_moduly.tekst)
import lekcja_12_2_moduly as l12m

print("Funckja pokaz w pliku lekcja_12_1_menu", l12m.tekst)
l12m.pokaz()
from lekcja_12_2_moduly import pokaz

lekcja_12_2_moduly.pokaz()

pokaz()
while True:
    print("""
    +----------------+
    |     Menu       |
    |1.Dodaj         |
    |2.Odejmi        |
    |3.Podziel       |
    |4.Wylosuj liczbę|
    |                |
    |0.Koniec        |
    +----------------+
    """)

    wybor = int(input("Jaki jest twoj wybor?"))
    liczba_1 = float(input("Podaj pierwsza liczbe: "))
    liczba_2 = float(input("Podaj druga liczbe: "))
    if wybor == 1:
        suma = liczba_1 + liczba_2
        print(f"Wynik dodawania liczby {liczba_1} i {liczba_2} to {suma}")
    elif wybor == 2:
        roznica = liczba_1 - liczba_2
        print(f"Wynik odejmowania liczby {liczba_1} i {liczba_2} to {roznica}")
    elif wybor == 3:
        iloraz = liczba_1 / liczba_2
        print(f"Wynik dzielenia liczby {liczba_1} i {liczba_2} to {iloraz}")
    elif wybor == 4:
        losowa_liczba = random.randint(int(liczba_1), int(liczba_2))
        print(f"Wylosowana Liczba z przedziału od {liczba_1} do {liczba_2}: {losowa_liczba}")
    elif wybor == 0:
        print("KONIEC")
        break

from random import choice


wybor = None
while wybor != "0":
    lista= ["KOt", "Pies", "List"]
    wybor = input(f"Druga pętla {choice(lista)}")
print("KONIEC")


