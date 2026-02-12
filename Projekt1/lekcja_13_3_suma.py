def suma_wszystkich(a, b, *args):
    """
    Sumuje 'a', 'b', oraz wszystkie dodatkowe argumenty (*args).
    """
    wynik = a + b

    for liczba in args:
        wynik += liczba
    return wynik


wynik = suma_wszystkich(5, 5, 5, 5, 5)
print(wynik)
print()

def suma_wszystkich(*args):
    """
    Sumuje 'a', 'b', oraz wszystkie dodatkowe argumenty (*args).
    """
    wynik = 0

    for liczba in args:
        wynik += liczba
    return wynik


wynik = suma_wszystkich()
print(wynik)
print()
def suma_wszystkich(*args):
    """
    Sumuje 'a', 'b', oraz wszystkie dodatkowe argumenty (*args).
    """

    if args:
        wynik = 0
        for liczba in args:
            wynik += liczba
        return wynik
    else:
        return None



wynik = suma_wszystkich(5)
print(wynik)
print()
