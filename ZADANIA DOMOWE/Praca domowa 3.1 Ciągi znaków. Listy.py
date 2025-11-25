print("ZADANIE 1")
print("*"*50)
def menu():
    print("\n=== SPRAWDZANIE PALINDROMU ===")
    print("1. Wprowadź ciąg znaków")
    print("2. Sprawdź, czy to palindrom")
    print("3. Zakończ program")

def wyczysc_tekst(tekst):
    tekst = tekst.lower()
    czysty = ""
    dozwolone = "abcdefghijklmnopqrstuvwxyz0123456789"
    for znak in tekst:
        if znak in dozwolone:
            czysty += znak
    return czysty

def czy_palindrom(tekst):
    czysty = wyczysc_tekst(tekst)
    return czysty == czysty[::-1]

def uruchom_program():
    ciag = ""
    while True:
        menu()
        wybor = input("Wybierz opcję (1–3): ")

        if wybor == "1":
            ciag = input("Wpisz tekst: ")
            print("Ciąg został zapisany.")
        elif wybor == "2":
            if ciag:
                if czy_palindrom(ciag):
                    print("To jest palindrom.")
                else:
                    print("To nie jest palindrom.")
            else:
                print("Najpierw wprowadź tesjt.")
        elif wybor == "3":
            print("Zakończono program.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

uruchom_program()

print("ZADANIE 2")
print("*"*50)
def zamien_na_wielkie(tekst, zastrzezone):
    male = "abcdefghijklmnopqrstuvwxyz"
    duze = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    slowa = tekst.split()
    wynik = []

    for slowo in slowa:
        czyste = ""
        for znak in slowo:
            if znak in male or znak in duze:
                if znak in duze:
                    czyste += male[duze.index(znak)]
                else:
                    czyste += znak
        if czyste in zastrzezone:
            nowe = ""
            for znak in slowo:
                if znak in male:
                    nowe += duze[male.index(znak)]
                else:
                    nowe += znak
            wynik.append(nowe)
        else:
            wynik.append(slowo)

    return " ".join(wynik)

def uruchom_program():
    print("Wpisz tekst: ")
    tekst = input()
    print("Wpisz zastrzeżone słowa oddzielone spacją: ")
    lista = input().lower().split()
    zmodyfikowany = zamien_na_wielkie(tekst, lista)
    print("\nZmodyfikowany tekst: ")
    print(zmodyfikowany)

uruchom_program()

print("ZADANIE 3")
print("*"*50)

def policz_zdania(tekst):
    licznik = 0
    for znak in tekst:
        if znak in ".!?":
            licznik += 1
    return licznik

def uruchom_program():
    print("Wpisz tekst: ")
    tekst = input()
    liczba_zdan = policz_zdania(tekst)
    print(f"\nLiczba zdań w tekście: {liczba_zdan}")

uruchom_program()

