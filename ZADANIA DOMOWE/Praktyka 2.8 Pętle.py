print("ZADANIE 1")
print("*"*50)

def pokaz_menu():
    print("\n=== MENU ===")
    print("1. Wprowadź liczbę")
    print("2. Pokaż liczbę cyfr")
    print("3. Oblicz sumę cyfr")
    print("4. Oblicz średnią cyfr")
    print("5. Policz liczbę zer")
    print("6. Zakończ program")

def liczba_cyfr(liczba):
    return len(liczba)

def suma_cyfr(liczba):
    return sum(int(cyfra) for cyfra in liczba)

def srednia_cyfr(liczba):
    return suma_cyfr(liczba) / liczba_cyfr(liczba)

def liczba_zer(liczba):
    return liczba.count("0")

def uruchom_program():
    liczba = ""
    while True:
        pokaz_menu()
        wybor = input("Wybierz opcję (1–6): ")

        if wybor == "1":
            liczba = input("Podaj liczbę całkowitą: ").strip()
            if not liczba.isdigit():
                print("To nie jest poprawna liczba całkowita.")
                liczba = ""
            else:
                print("Liczba została zapisana.")
        elif wybor == "2":
            if liczba:
                print(f"Liczba cyfr: {liczba_cyfr(liczba)}")
            else:
                print("Najpierw wprowadź liczbę.")
        elif wybor == "3":
            if liczba:
                print(f"Suma cyfr: {suma_cyfr(liczba)}")
            else:
                print("Najpierw wprowadź liczbę.")
        elif wybor == "4":
            if liczba:
                print(f"Średnia cyfr: {srednia_cyfr(liczba):.2f}")
            else:
                print("Najpierw wprowadź liczbę.")
        elif wybor == "5":
            if liczba:
                print(f"Liczba zer: {liczba_zer(liczba)}")
            else:
                print("Najpierw wprowadź liczbę.")
        elif wybor == "6":
            print("Zakończono program.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

uruchom_program()

print("ZADANIE 2")
print("*"*50)

def szachownica(rozmiar, wiersze, kolumny):
    for w in range(wiersze):
        for _ in range(rozmiar):
            linia = ""
            for k in range(kolumny):
                if (w + k) % 2 == 0:
                    linia += "*" * rozmiar
                else:
                    linia += "-" * rozmiar
            print(linia)

print("MOZESZ TU ZMIENIC W KODZIE WARTOSCI")
rozmiar_komorki = 3
liczba_wierszy = 6
liczba_kolumn = 5

szachownica(rozmiar_komorki, liczba_wierszy, liczba_kolumn)

print("ZADANIE 3")
print("*"*50)

import random

def menu():
    print("\n=== TEST Z TABLICZKI MNOŻENIA ===")
    print("1. Poziom łatwy (1–5, 5 pytań)")
    print("2. Poziom średni (1–10, 7 pytań)")
    print("3. Poziom trudny (5–15, 10 pytań)")
    print("4. Zakończ")

def generuj_pytania(zakres_min, zakres_max, liczba_pytan):
    punkty = 0
    for i in range(1, liczba_pytan + 1):
        a = random.randint(zakres_min, zakres_max)
        b = random.randint(zakres_min, zakres_max)
        poprawna_odpowiedz = a * b
        print(f"\nPytanie {i}: Ile to {a} × {b}?")
        try:
            odpowiedz = int(input("Twoja odpowiedź: "))
            if odpowiedz == poprawna_odpowiedz:
                print("Dobrze!")
                punkty += 1
            else:
                print(f"Źle. Poprawna odpowiedź to {poprawna_odpowiedz}.")
        except ValueError:
            print("To nie jest liczba. Brak punktu.")
    return punkty, liczba_pytan

def uruchom_program():
    while True:
        menu()
        wybor = input("Wybierz poziom trudności (1–4): ")

        if wybor == "1":
            punkty, maks = generuj_pytania(1, 5, 5)
        elif wybor == "2":
            punkty, maks = generuj_pytania(1, 10, 7)
        elif wybor == "3":
            punkty, maks = generuj_pytania(5, 15, 10)
        elif wybor == "4":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór.")
            continue

        print(f"\nTwój wynik: {punkty} / {maks} punktów")
        print("Umiejętności:", "★" * punkty + "☆" * (maks - punkty)) #NA MACBOOKU TA LINIJKA WYRZUCA BŁĄD

uruchom_program()

print("ZADANIE 4")
print("*"*50)

def drukuj_romb(wysokosc):
    # TO JEST GORA I MOZNA EDYTOWAC
    for i in range(wysokosc):
        spacje = " " * (wysokosc - i - 1)
        gwiazdki = "*" * (2 * i + 1)
        print(spacje + gwiazdki)
    # A TO JE DOŁ I TEZ MOZNA EDYTOWAC
    for i in range(wysokosc - 2, -1, -1):
        spacje = " " * (wysokosc - i - 1)
        gwiazdki = "*" * (2 * i + 1)
        print(spacje + gwiazdki)


drukuj_romb(5)