import random
import lekcja_12_2_moduly

from selenium.webdriver.support.expected_conditions import none_of

print("""
=========================
         MENU
=========================
1 - Dodawanie
2 - Odejmowanie
3 - Dzielenie
4 - Mnożenie
5 - Losowanie liczb
0 - Wyjście
=========================
""")

while True:
    wybor = int(input("Podaj wybor: "))

    if wybor == 0:
        print("Koniec programu. Do zobaczenia!")
        break

    elif wybor == 1:
        liczba1 = float(input("Podaj liczba 1: "))
        liczba2 = float(input("Podaj liczba 2: "))
        print(f"Wynik to: {liczba1 + liczba2}")

    elif wybor == 2:
        liczba1 = float(input("Podaj liczba 1: "))
        liczba2 = float(input("Podaj liczba 2: "))
        print(f"Wynik to: {liczba1 - liczba2}")

    elif wybor == 3:
        liczba1 = float(input("Podaj liczba 1: "))
        liczba2 = float(input("Podaj liczba 2: "))
        if liczba2 != 0:
            print(f"Wynik to: {liczba1 / liczba2}")
        else:
            print("Błąd: nie można dzielić przez zero.")

    elif wybor == 4:
        liczba1 = float(input("Podaj liczba 1: "))
        liczba2 = float(input("Podaj liczba 2: "))
        print(f"Wynik to: {liczba1 * liczba2}")

    elif wybor == 5:
        print(f"Wylosowana liczba to: {random.randint(1, 100)}")

    else:
        print("Nie dokonano poprawnego wyboru.")



