def czy_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

tekst = input("Podaj liczbę całkowitą: ")
liczba = int(tekst)

wynik = czy_pierwsza(liczba)
print("Czy liczba jest pierwsza?")
if wynik == True:
    print("TAK")
else:
    print("NIE")
