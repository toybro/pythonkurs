print("Zadanie 1")
print("*"*50)
def uruchom_program():
    print("Wpisz ciąg znaków: ")
    ciag = input()
    odwrocony = ciag[::-1]
    print("\nOdwrócony ciąg: ")
    print(odwrocony)

uruchom_program()




print("Zadanie 2")
print("*"*50)
def policz_litery_i_cyfry(ciag):
    litery = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cyfry = "0123456789"
    liczba_liter = 0
    liczba_cyfr = 0

    for znak in ciag:
        if znak in litery:
            liczba_liter += 1
        elif znak in cyfry:
            liczba_cyfr += 1

    return liczba_liter, liczba_cyfr

def uruchom_program():
    print("Wpisz ciąg znaków: ")
    tekst = input()
    litery, cyfry = policz_litery_i_cyfry(tekst)
    print(f"\nLiczba liter: {litery}")
    print(f"Liczba cyfr: {cyfry}")

uruchom_program()



print("Zadanie 3")
print("*"*50)
def policz_symbol(ciag, symbol):
    licznik = 0
    for znak in ciag:
        if znak == symbol:
            licznik += 1
    return licznik

def uruchom_program():
    print("Wpisz ciąg znaków: ")
    tekst = input()
    print("Wpisz symbol do wyszukania: ")
    szukany = input()

    if len(szukany) != 1:
        print("Podaj dokładnie jeden znak jako symbol.")
        return

    wynik = policz_symbol(tekst, szukany)
    print(f"\nSymbol '{szukany}' występuje {wynik} razy w ciągu.")

uruchom_program()


print("Zadanie 4")
print("*"*50)
def policz_wystapienia(ciag, slowo):
    return ciag.count(slowo)

def uruchom_program():
    print("Wpisz ciąg znaków: ")
    tekst = input()
    print("Wpisz wyszukiwane słowo: ")
    szukane = input()

    liczba = policz_wystapienia(tekst, szukane)
    print(f"\nSłowo '{szukane}' występuje {liczba} razy w ciągu.")

uruchom_program()


print("Zadanie 5")
print("*"*50)

def uruchom_program():
    print("Wpisz ciąg znaków: ")
    tekst = input()
    print("Wpisz słowo do zastąpienia: ")
    stare = input()
    print("Wpisz nowe słowo: ")
    nowe = input()

    wynik = tekst.replace(stare, nowe)
    print("\nZmodyfikowany ciąg znaków:")
    print(wynik)

uruchom_program()