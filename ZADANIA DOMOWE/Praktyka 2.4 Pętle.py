print("Zadanie 1")
print("Użytkownik wpisuje dwie liczby. Wypisz wszystkie liczby z podanego zakresu.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
for i in range(a, b + 1):
    print(i)

print("Zadanie 2")
print("Użytkownik wpisuje dwie liczby. Wydrukuj wszystkie liczby nieparzyste z podanego zakresu.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)

print("Zadanie 3")
print("Użytkownik wpisuje dwie liczby. Wydrukuj wszystkie liczby parzyste z podanego zakresu.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)

print("Zadanie 4")
print("Użytkownik wpisuje dwie liczby. Wypisz wszystkie liczby z podanego zakresu w kolejności malejącej.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
for i in range(max(a, b), min(a, b) - 1, -1):
    print(i)

print("Zadanie 5")
print("Użytkownik wpisuje dwie liczby. Wypisz wszystkie liczby nieparzyste z podanego zakresu. Jeśli punkty końcowe i początkowe zakresu są nieprawidłowe, znormalizuj je.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
start = min(a, b)
end = max(a, b)
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i)