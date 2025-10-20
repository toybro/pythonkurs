print("Zadanie 1")

print("Podaj liczbę od 1 do 7, aby wybrać dzień tygodnia:")
dzien = int(input("Dzień tygodnia (1–7): "))

if dzien == 1:
    print("Poniedziałek")
elif dzien == 2:
    print("Wtorek")
elif dzien == 3:
    print("Środa")
elif dzien == 4:
    print("Czwartek")
elif dzien == 5:
    print("Piątek")
elif dzien == 6:
    print("Sobota")
elif dzien == 7:
    print("Niedziela")
else:
    print("Niepoprawna liczba. Podaj wartość od 1 do 7.")

print("Zadanie 2")
print("*"*50)

print("Podaj liczbę od 1 do 12, aby wybrać miesiąc:")
miesiac = int(input("Numer miesiąca: "))

if miesiac == 1:
    print("Styczeń")
elif miesiac == 2:
    print("Luty")
elif miesiac == 3:
    print("Marzec")
elif miesiac == 4:
    print("Kwiecień")
elif miesiac == 5:
    print("Maj")
elif miesiac == 6:
    print("Czerwiec")
elif miesiac == 7:
    print("Lipiec")
elif miesiac == 8:
    print("Sierpień")
elif miesiac == 9:
    print("Wrzesień")
elif miesiac == 10:
    print("Październik")
elif miesiac == 11:
    print("Listopad")
elif miesiac == 12:
    print("Grudzień")
else:
    print("Niepoprawna liczba. Podaj wartość od 1 do 12.")

print("Zadanie 3")
print("*"*50)

print("Podaj dowolną liczbę:")
liczba = float(input("Liczba: "))

if liczba > 0:
    print("Your number is positive")
elif liczba < 0:
    print("Your number is negative")
else:
    print("Your number is equal to zero")

print("Zadanie 4")
print("*"*50)

print("Porównanie dwóch liczb")

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

if liczba1 == liczba2:
    print("Liczby są równe.")
else:
    if liczba1 < liczba2:
        print("Liczby w kolejności rosnącej:", liczba1, liczba2)
    else:
        print("Liczby w kolejności rosnącej:", liczba2, liczba1)