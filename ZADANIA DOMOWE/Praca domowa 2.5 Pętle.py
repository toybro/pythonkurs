print("*" * 50)
print("Zadanie 1")
print("Użytkownik wpisuje dwie liczby. Znajdź sumę wszystkich liczb parzystych, nieparzystych i wielokrotności 9 w podanym zakresie, a także średnią arytmetyczną każdej z grup.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

suma_parzyste = 0
licznik_parzyste = 0
suma_nieparzyste = 0
licznik_nieparzyste = 0
suma_9 = 0
licznik_9 = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        suma_parzyste += i
        licznik_parzyste += 1
    else:
        suma_nieparzyste += i
        licznik_nieparzyste += 1
    if i % 9 == 0:
        suma_9 += i
        licznik_9 += 1

print("Suma liczb parzystych:", suma_parzyste)
print("Średnia liczb parzystych:", suma_parzyste / licznik_parzyste if licznik_parzyste > 0 else 0)
print("Suma liczb nieparzystych:", suma_nieparzyste)
print("Średnia liczb nieparzystych:", suma_nieparzyste / licznik_nieparzyste if licznik_nieparzyste > 0 else 0)
print("Suma wielokrotności 9:", suma_9)
print("Średnia wielokrotności 9:", suma_9 / licznik_9 if licznik_9 > 0 else 0)

print("*" * 50)
print("Zadanie 2")
print("Użytkownik wpisuje długość linii i symbol, który ma ją wypełnić. Wydrukuj pionową linię utworzoną z wpisanego symbolu o określonej długości.")
dlugosc = int(input("Podaj długość linii: "))
symbol = input("Podaj symbol: ")
for _ in range(dlugosc):
    print(symbol)

print("*" * 50)
print("Zadanie 3")
print("Użytkownik wpisuje liczbę. Jeśli liczba jest większa od 0, wypisywane jest \"Twoja liczba jest dodatnia\"; jeśli jest mniejsza od zera, wypisywane jest \"Twoja liczba jest ujemna\"; jeśli jest równa 0, wypisywane jest \"Twoja liczba jest równa zero\". Gdy użytkownik wpisze 7, program zatrzyma się i wypisze \"Good bye!\".")
while True:
    liczba = int(input("Podaj liczbę: "))
    if liczba == 7:
        print("Good bye!")
        break
    elif liczba > 0:
        print("Twoja liczba jest dodatnia")
    elif liczba < 0:
        print("Twoja liczba jest ujemna")
    else:
        print("Twoja liczba jest równa zero")

print("*" * 50)
print("Zadanie 4")
print("Użytkownik wpisuje liczby. Program musi obliczyć ich sumę oraz znaleźć maksimum i minimum. Gdy użytkownik wpisze 7, program zatrzymuje się i wypisuje \"Good bye!\".")
suma = 0
maks = None
minim = None

while True:
    liczba = int(input("Podaj liczbę: "))
    if liczba == 7:
        print("Good bye!")
        break
    suma += liczba
    if maks is None or liczba > maks:
        maks = liczba
    if minim is None or liczba < minim:
        minim = liczba

print("Suma:", suma)
print("Maksimum:", maks)
print("Minimum:", minim)