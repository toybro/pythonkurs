print("Zadanie 1")

print("Sprawdź, czy liczba jest szczęśliwa")

liczba = int(input("Podaj sześciocyfrową liczbę: "))

if 100000 <= liczba <= 999999:
    tekst = str(liczba)
    suma_lewa = int(tekst[0]) + int(tekst[1]) + int(tekst[2])
    suma_prawa = int(tekst[3]) + int(tekst[4]) + int(tekst[5])

    if suma_lewa == suma_prawa:
        print("To szczęśliwa liczba!")
    else:
        print("To nie jest szczęśliwa liczba.")
else:
    print("Toż to istny błąd: liczba musi mieć dokładnie 6 cyfr.")

print("Zadanie 2")
print("*"*50)

print("Zamiana cyfr w sześciocyfrowej liczbie")

liczba = int(input("Podaj sześciocyfrową liczbę: "))

if 100000 <= liczba <= 999999:
    tekst = str(liczba)
    nowa_liczba = (tekst[5] + tekst[4] + tekst[2] + tekst[3] + tekst[1] + tekst[0])
    print("Nowa liczba po zamianie cyfr:", nowa_liczba)
else:
    print("Upsik: liczba musi mieć dokładnie 6 cyfr.")

print("Zadanie 3")
print("*"*50)

print("Podaj numer miesiąca (od 1 do 12):")
miesiac = int(input("Miesiąc: "))

if miesiac in [1, 2, 12]:
    print("Zima")
elif 3 <= miesiac <= 5:
    print("Wiosna")
elif 6 <= miesiac <= 8:
    print("Lato")
elif 9 <= miesiac <= 11:
    print("Jesień")
else:
    print("Błąd: podaj liczbę od 1 do 12.")