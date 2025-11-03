print("*" * 50)
print("Zadanie 1")
print("Użytkownik wpisuje dwie liczby. Znajdź sumę i średnią liczb z podanego zakresu.")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
suma = 0
licznik = 0
for i in range(a, b + 1):
    suma += i
    licznik += 1
srednia = suma / licznik
print("Suma:", suma)
print("Średnia:", srednia)

print("*" * 50)
print("Zadanie 2")
print("Użytkownik wpisuje liczbę. Oblicz iloraz liczby. Na przykład, jeśli użytkownik wpisze 3, to iloraz wynosi 1*2*3 = 6.")
n = int(input("Podaj liczbę: "))
iloraz = 1
for i in range(1, n + 1):
    iloraz *= i
print("Iloraz (silnia):", iloraz)

print("*" * 50)
print("Zadanie 3")
print("Użytkownik wpisuje długość linii. Wydrukuj poziomą linię składającą się z * o podanej długości.")
dlugosc = int(input("Podaj długość linii: "))
print("*" * dlugosc)

print("*" * 50)
print("Zadanie 4")
print("Użytkownik wpisuje długość linii i symbol, który ma ją wypełnić. Wydrukuj poziomą linię utworzoną z wpisanego symbolu o określonej długości.")
dlugosc = int(input("Podaj długość linii: "))
symbol = input("Podaj symbol: ")
print(symbol * dlugosc)