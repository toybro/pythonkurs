def suma_wszystkich(a, b, *args):
    """
    Fukcja sumuje 'a', 'b', oraz wszystkie możliwe argumenty (*args*).

    """
    wynik = a + b
    for liczba in args:
        wynik += liczba
    return wynik

wynik = suma_wszystkich(5, 5, 5)
print(wynik)


