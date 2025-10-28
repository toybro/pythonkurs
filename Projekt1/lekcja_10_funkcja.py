from lekcja_2_2 import liczba_2


def nazwa_funkcji():
    if 2 < 3:
       wynik = "2 jest mniejsze od 3"
       return wynik #zwraca wynik i przerywa działanie

       # pass  # pass unieważnia to działanie i przechodzi dalej

    print("Funkcja o nazwie 'nazwa_funkcji'")
    return "3 jest wieksze od 2"


nazwa_funkcji()  # wywołanie funkcji
print(nazwa_funkcji())

def dodaj_dwie_liczby(liczba_1, liczba_2):
    print("To jest funcja o nazwie 'dodaj_dwie_liczby")
    print(f"Wynik dodawania: \n{liczba_1} + {liczba_2} = {liczba_1+liczba_2}")

dodaj_dwie_liczby(5,7)
dodaj_dwie_liczby(10,255)


liczba1_uzytkownika = float(input("Podaj liczbę 1: "))
liczba2_uzytkownika = float(input("Podaj liczbę 2: "))

def dodaj_dwie_liczby_uzytkownika(liczba1, liczba2):
    print("To jest funkcja o nazwie 'dodaj_dwie_liczby'")
    print(f"Wynik dodawania:\n{liczba1} + {liczba2} = {liczba1 + liczba2}")

dodaj_dwie_liczby_uzytkownika(liczba1_uzytkownika, liczba2_uzytkownika)
print("Następne zadanie")

liczba1_uzytkownika = float(input("Podaj liczbę 1: "))
liczba2_uzytkownika = float(input("Podaj liczbę 2: "))
dodaj_dwie_liczby_uzytkownika(liczba1_uzytkownika, liczba2_uzytkownika)


print("*"*50)
print("Odejmowanie liczb")
liczbau1_odejm = float(input("Liczba pierwsza: "))
liczbau2_odejm = float(input("Liczba druga: "))
def odejmowanie_2_liczb(liczbau1, liczbau2):
    print("Ta funkcja odejmuje dwie liczby")
    print("Podaj liczby")

    print(f"Wynik odejmowania: {liczbau1} - {liczbau2} = {liczbau1 - liczbau2}")

odejmowanie_2_liczb(liczbau1_odejm, liczbau2_odejm)

