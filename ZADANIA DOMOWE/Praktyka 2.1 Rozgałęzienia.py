print("Zadanie 1")
liczba = int(input("Podaj liczbe: "))
if liczba % 2 == 0:
    print(f"{liczba} Jest parzysta")
else:
    print(f"{liczba} Jest nieparzysta")

print("*"*50)

print("Zadanie 2")
liczba = int(input("Podaj liczbe: "))
if liczba % 7 == 0:
    print(f"{liczba} To wielokrotnośc 7")
else:
    print(f"{liczba} Nie jest wielokrotnoscia 7")

print("*"*50)

print("Zadanie 3")
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
maksimum = max(liczba1, liczba2)
print(f"Maksimum z podanych liczb to: {maksimum}")

print("*"*50)

print("Zadanie 4")
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
minimum = min(liczba1, liczba2)
print(f"Minimum z podanych liczb to: {minimum}")

print("*"*50)

print("Zadanie 5")
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
print("Wybierz opcje z meni")
print("1 To Suma")
print("2 To Różnica")
print("3 To Iloczyn")
print("4 To Średnia arytmetyczna")

menu = input("Twój wybór (1-4): ")
if menu == "1":
    wynik = liczba1 + liczba2
    print(f"Suma: {wynik}")
elif menu == "2":
    wynik = liczba1 - liczba2
    print(f"Różnica: {wynik}")
elif menu == "3":
    wynik = liczba1 * liczba2
    print(f"Iloczyn: {wynik}")
elif menu == "4":
    wynik = (liczba1 + liczba2) / 2
    print(f"Średnia arytmetyczna: {wynik}")
else:
    print("Nieprawidłowy wybór. Wybierz opcję od 1 do 4.")

