print("*" * 50)
print("Zadanie 1")
print("Użytkownik wpisuje dwie liczby (początek i koniec zakresu). Przeanalizuj wszystkie liczby w tym zakresie w następujący sposób: jeśli liczba jest wielokrotnością 7, wypisz ją.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)
    else:
        print("Nie ma tu takiej liczby")

print("*" * 50)
print("Zadanie 2")
print("Użytkownik wpisuje dwie liczby (punkt początkowy i końcowy zakresu). Przeanalizuj wszystkie liczby w tym zakresie. Wydrukuj następujące wyniki:\nWszystkie liczby w zakresie;\nWszystkie liczby w zakresie w porządku malejącym;\nWszystkie liczby będące wielokrotnościami liczby 7;\nIle liczb jest wielokrotnością liczby 5.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

print("Wszystkie liczby w zakresie:")
for i in range(a, b + 1):
    print(i)

print("Wszystkie liczby w zakresie w porządku malejącym:")
for i in range(b, a - 1, -1):
    print(i)

print("Wszystkie liczby będące wielokrotnościami liczby 7:")
for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)

count_5 = 0
for i in range(a, b + 1):
    if i % 5 == 0:
        count_5 += 1
print("Ilość liczb będących wielokrotnościami liczby 5:", count_5)

print("*" * 50)
print("Zadanie 3")
print("Użytkownik wpisuje dwie liczby (punkt początkowy i końcowy zakresu). Przeanalizuj wszystkie liczby w tym zakresie. Wynik powinien być zgodny z poniższymi regułami.\nJeśli liczba jest wielokrotnością 3 (podzielna przez 3 bez reszty), wypisz słowo Fizz. Jeśli jest wielokrotnością 5, wypisane zostanie słowo Buzz. Jeśli jest wielokrotnością 3 i 5, zostanie wyświetlone słowo Fizz Buzz. Jeśli liczba nie jest wielokrotnością 3 lub 5, wypisana zostanie sama liczba.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)