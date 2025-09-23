imie = input("Podaj imie: ")
waga = input("Podaj swoją wagę w kg: ")
wzrost = input("Podaj swój wzrost w m: ")


waga = float(waga)
wzrost = float(wzrost)


bmi = waga / wzrost ** 2
print(bmi)
print(waga," KG")
if bmi < 18.5:
    wynik = "Niedowaga"
    print(wynik)
elif bmi >= 18.5 and bmi < 25:
    wynik = "Norma"
    print(wynik)
elif bmi >= 25:
    wynik ="Nadwaga"
    print(wynik)
elif bmi >= 30:
    wynik = "Duża Nadwaga"
    print(wynik)

print("Koniec pierwszego warunku.")

if bmi < 18.5:
    wynik = "Niedowaga"
    print(wynik)
elif bmi >= 18.5 and bmi < 25:
    wynik = "Norma"
    print(wynik)
else:
    wynik ="Nadwaga"
    print(wynik)

print("Koniec drugiego warunku.")

if bmi < 18.5:
    wynik = "Niedowaga"
elif 18.5 <= bmi < 25:
    wynik = "Norma"
else:
    wynik = "Nadwaga"
    if imie == "Adam":
        print("Czas na dietę")
    print("Zwolnij", imie)

print(wynik)

print("Koniec trzeciego warunku.")