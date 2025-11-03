import random
import time

print("*" * 50)
print("Zadanie 1")
print("Wypisz tabliczkę mnożenia dla liczby zdefiniowanej przez użytkownika.")
n = int(input("Podaj liczbę: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

print("*" * 50)
print("Zadanie 2")

print("!!!--WALUTY NA DZIEN 3.11.25--!!!")


print("Napisz program przeliczający waluty. Zaimplementuj dialog z użytkownikiem poprzez menu.")
while True:
    print("\nMenu:")
    print("1. PLN na EUR")
    print("2. EUR na PLN")
    print("3. PLN na USD")
    print("4. USD na PLN")
    print("5. Wyjście")
    wybor = input("Wybierz opcję: ")

    if wybor == "5":
        print("Zakończono.")
        break

    kwota = float(input("Podaj kwotę: "))
    if wybor == "1":
        print("Wynik:", round(kwota * 0.23, 2), "EUR")
    elif wybor == "2":
        print("Wynik:", round(kwota * 4.26, 2), "PLN")
    elif wybor == "3":
        print("Wynik:", round(kwota * 0.27, 2), "USD")
    elif wybor == "4":
        print("Wynik:", round(kwota * 3.69, 2), "PLN")
    else:
        print("Nieprawidłowa opcja.")

print("*" * 50)
print("Zadanie 3")
print("Użytkownik wpisuje punkt początkowy i końcowy zakresu oraz liczbę. Jeśli liczba nie mieści się w zakresie, program prosi użytkownika o ponowne wprowadzenie liczby i tak dalej, aż użytkownik wprowadzi liczbę poprawnie. Program wyświetla wszystkie liczby w zakresie, podświetlając liczbę wykrzyknikiem.")
start = int(input("Podaj początek zakresu: "))
end = int(input("Podaj koniec zakresu: "))
while True:
    liczba = int(input("Podaj liczbę z zakresu: "))
    if start <= liczba <= end:
        break
    print("Liczba poza zakresem. Spróbuj ponownie.")

for i in range(start, end + 1):
    if i == liczba:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")
print()

print("*" * 50)
print("Zadanie 4")
print("Opracuj grę Zgadnij liczbę.")
sekret = random.randint(1, 500)
proby = 0
start_time = time.time()

while True:
    guess = int(input("Zgadnij liczbę (1–500) lub wpisz 0, aby zakończyć: "))
    if guess == 0:
        print("Zrezygnowałeś. ELO")
        break
    proby += 1
    if guess < sekret:
        print("Za mało.")
    elif guess > sekret:
        print("Za dużo.")
    else:
        czas = time.time() - start_time
        print(f"Brawo! Odgadłeś liczbę {sekret} w {proby} próbach.")
        print(f"Czas gry: {round(czas, 2)} sekund.")
        break