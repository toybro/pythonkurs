#input("Komunikat dla uzytkownika")
#imie = input("Podaj swoje imię: ")
#print("Witaj, ", imie)

waga = input("Podaj swoją wagę w kg: ")
wzrost = input("Podaj swój wzrost w m: ")

print("Określenie typu danych: ", type(waga))

waga = float(waga)
wzrost = float(wzrost)

print("Określenie typu danych: ", type(wzrost))

bmi = waga / wzrost ** 2

if bmi < 18.5:
    wynik = "Niedowaga"
    print(wynik)
print(waga," KG")
print(bmi)
if bmi >= 18.5 and bmi < 25:
    wynik = "Norma"
    print(wynik)
if bmi >= 25:
    wynik ="Nadwaga"
    print(wynik)

print("Do zobaczenia.")