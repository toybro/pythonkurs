print("Zadanie 1")

print("Podaj 3 liczby")
liczba1 = int(input("Podaj liczbe 1: "))
liczba2 = int(input("Podaj liczbe 2: "))
liczba3 = int(input("Podaj liczbe 3: "))

wynnik = 0

print("Menu")
print("1 - Suma")
print("2 - Iloczyn")
wybor = int(input("Co wybierasz ? "))
if wybor == 1:
    wynik = liczba1 + liczba2 + liczba3
    print("Suma liczb wynosi: ", wynik)

elif wybor == 2:
    wynik = liczba1 * liczba2 * liczba3
    print("Iloczyn liczb wynosi: ", wynik)
else:
    print("Nie wybrales poprawnej opcji w menu")

print("*"*50)

print("Zadanie 2")

print("Podaj 3 liczby")
liczba1 = int(input("Podaj liczbe 1: "))
liczba2 = int(input("Podaj liczbe 2: "))
liczba3 = int(input("Podaj liczbe 3: "))

wynnik = 0

print("Menu")
print("1 - Max")
print("2 - Min")
print("3 - Średnia artymetnyczna")

wybor = int(input("Co wybierasz ? "))
if wybor == 1:
    wynik = max(liczba1, liczba2, liczba3)
    print("Max wynosi: ", wynik)

elif wybor == 2:
    wynik = min(liczba1, liczba2, liczba3)
    print("Min: ", wynik)

elif wybor == 3:
    wynik = (liczba1 + liczba2 + liczba3)/3
    print("Średnia: ", wynik)

else:
    print("Nie wybrales poprawnej opcji w menu")

print("*"*50)

print("Zadanie 3")

print("Podaj ilośc metrów")
metry = float(input("Oczekiwana wartość: "))
print("Na co chcesz przeliczyć ?")
print("Mila - 1")
print("Cale - 2")
print("Jardy - 3")

wybor = int(input("Co wybierasz ? "))
if wybor == 1:
    wynik = metry * 0.000621371
    print(f"{metry} metrów to {wynik} mili")
elif wybor == 2:
    wynik = metry * 39.3701
    print(f"{metry} metrów to {wynik} cali")
elif wybor == 3:
    wynik = metry * 1.09361
    print(f"{metry} metrów to {wynik} jardów")
else:
    print("Niepoprawny wybór jednostki.")
