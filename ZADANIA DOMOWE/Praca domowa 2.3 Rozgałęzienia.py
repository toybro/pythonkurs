print("Zadanie 1")
print("Podaj liczbę od 1 do 100:")
liczba = int(input("Liczba: "))

if 1 <= liczba <= 100:
    if liczba % 3 == 0 and liczba % 5 == 0:
        print("Fizz Buzz")
    elif liczba % 3 == 0:
        print("Fizz")
    elif liczba % 5 == 0:
        print("Buzz")
    else:
        print(liczba)
else:
    print("Błąd: liczba musi być z zakresu od 1 do 100.")

print("Zadanie 2")
print("*"*50)

print("Podnoszenie liczby do potęgi od 0 do 7")
liczba = float(input("Podaj liczbę: "))
potega = int(input("Podaj wykładnik potęgi (0–7): "))
if 0 <= potega <= 7:
    wynik = liczba ** potega
    print(f"{liczba} do potęgi {potega} to: {wynik}")
else:
    print("Błąd: wykładnik musi być z zakresu od 0 do 7.")

print("Zadanie 3")
print("*"*50)

print("Obliczanie kosztu połączenia między operatorami")
koszt_bazowy = float(input("Podaj koszt jednej minuty połączenia (zł): "))
print("Dostępni operatorzy: Orange, Play, Plus, T-Mobile")
wychodzacy = input("Podaj operatora połączenia wychodzącego: ").lower()
przychodzacy = input("Podaj operatora połączenia przychodzącego: ").lower()
doplata_miedzy_sieciami = 0.20
if wychodzacy == przychodzacy:
    koszt_koncowy = koszt_bazowy
else:
    koszt_koncowy = koszt_bazowy + doplata_miedzy_sieciami

print(f"Całkowity koszt połączenia: {koszt_koncowy} zł")

print("Zadanie 4")
print("*"*50)

print("Obliczanie wynagrodzenia dla trzech sprzedawców")


def oblicz_wynagrodzenie(sprzedaz):
    podstawa = 200
    if sprzedaz <= 500:
        prowizja = sprzedaz * 0.03
    elif sprzedaz <= 1000:
        prowizja = sprzedaz * 0.05
    else:
        prowizja = sprzedaz * 0.08
    return podstawa + prowizja


sprzedaz1 = float(input("Podaj wartość sprzedaży dla sprzedawcy nr 1: "))
sprzedaz2 = float(input("Podaj wartość sprzedaży dla sprzedawcy nr 2: "))
sprzedaz3 = float(input("Podaj wartość sprzedaży dla sprzedawcy nr 3: "))


wynagrodzenia = [
    oblicz_wynagrodzenie(sprzedaz1),
    oblicz_wynagrodzenie(sprzedaz2),
    oblicz_wynagrodzenie(sprzedaz3)
]


najlepszy_index = wynagrodzenia.index(max(wynagrodzenia))
wynagrodzenia[najlepszy_index] += 200
for i in range(3):
    print(f"Sprzedawca nr {i+1}: {wynagrodzenia[i]:.2f} USD")

print(f"Najlepszy sprzedawca to nr {najlepszy_index+1} – otrzymuje dodatkową premię 200 USD.")