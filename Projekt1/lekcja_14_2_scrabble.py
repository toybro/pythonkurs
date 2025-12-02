from lekcja_14_1_izogram import czy_izogram

punkty = {
    1: list("abcdefghij"),
    2: list("klłmn"),
    3: list("oóp"),
    5: list("rsśtuw"),
    6: list("xyz"),
}

def punkty_za_slowa(slowo):
    slowo = slowo.lower()
    suma = 0
    for litera in slowo:
        for wartosc, litery in punkty.items():
            if litera in litery:
                print(wartosc, litera)
                suma += wartosc
                break
    return suma


punkty_2 = {
    'A': 1, 'E': 1, 'I': 1, 'N': 1, 'O': 1,
    'R': 1, 'S': 1, 'W': 1, 'Z': 1,
    'Y': 2, 'C': 2, 'D': 2, 'K': 2, 'L': 2,
    'M': 2, 'P': 2, 'T': 2,
    'B': 3, 'G': 3, 'H': 3, 'J': 3, 'Ł': 3,
    'U': 3,
    'Ą': 5, 'Ę': 5, 'F': 5, 'Ó': 5, 'Ś': 5,
    'Ż': 5,
    'Ć': 6,
    'Ń': 7,
    'Ź': 9,
    'BLANK': 0  # Dwa puste kafelki (blanki)
}

def scrabble_punkty(slowo):
    slowo = slowo.upper()
    suma = 0
    for litera in slowo:
        suma += punkty_2[litera]
    return suma

if __name__ == "__main__":
    print(czy_izogram("Patelnia"))

    nasze_slowo = input("Podaj slowo: ")

    print(f"Punkty za słowo '{nasze_slowo}': {punkty_za_slowa(nasze_slowo)}")

    wynik = scrabble_punkty(nasze_slowo)
    print(f"Słowo: {nasze_slowo} jest warte {wynik}pkt. w Scrabble")
    while True:
        pytanie = input("Czychcesz kontynuować [T/N]")
        if pytanie.upper() != 'T':
            break


