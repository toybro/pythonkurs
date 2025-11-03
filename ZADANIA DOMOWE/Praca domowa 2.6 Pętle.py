print("*" * 50)
print("Zadanie 1")
print("Napisz program, który żąda dwóch liczb całkowitych x i y, a następnie oblicza i wypisuje wartość x podniesioną do potęgi y.")
x = int(input("Podaj liczbę x: "))
y = int(input("Podaj liczbę y: "))
print("Wynik:", x ** y)

print("*" * 50)
print("Zadanie 2")
print("Policz liczbę liczb całkowitych z zakresu od 100 do 999, które mają dwie identyczne cyfry.")
licznik = 0
for i in range(100, 1000):
    s = str(i)
    if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
        licznik += 1
print("Liczba takich liczb:", licznik)

print("*" * 50)
print("Zadanie 3")
print("Policz liczbę liczb całkowitych z zakresu od 100 do 9999, które mają różne cyfry.")
licznik = 0
for i in range(100, 10000):
    s = str(i)
    if len(set(s)) == len(s):
        licznik += 1
print("Liczba tychże liczb:", licznik)

print("*" * 50)
print("Zadanie 4")
print("Użytkownik wpisuje wartość całkowitą. Usuń wszystkie 3 i 6 z tej liczby całkowitej i wypisz ją.")
liczba = input("Podaj liczbę całkowitą: ")
wynik = ""
for znak in liczba:
    if znak not in ['3', '6']:
        wynik += znak
print("Wynik:", wynik)