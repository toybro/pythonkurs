print("Zadanie 1")
cyfry = []
cyfra1 = input("Podaj pierwszą cyfrę: ")
cyfra2 = input("Podaj drugą cyfrę: ")
cyfra3 = input("Podaj trzecią cyfrę: ")
cyfry.append(cyfra1)
cyfry.append(cyfra2)
cyfry.append(cyfra3)

liczba = int(cyfra1 + cyfra2 + cyfra3)
print("Utworzona liczba: ", liczba)

print("*"*50)

print("Zadanie 2")
liczba = input("Podaj czterocyfrową liczbę: ")
cyfra1 = int(liczba[0])
cyfra2 = int(liczba[1])
cyfra3 = int(liczba[2])
cyfra4 = int(liczba[3])
iloczyn = cyfra1 * cyfra2 * cyfra3 * cyfra4
print(f" {cyfra1} * {cyfra2} * {cyfra3} * {cyfra4} = {iloczyn}")

print("*"*50)

print("Zadanie 3")
metry = float(input("Podaj liczbę metrów: ")) #musiałem ustawić typ danych

centymetry = metry * 100
decymetry = metry * 10
milimetry = metry * 1000
mile = metry / 1609.344

print("Centymetry: ", centymetry)
print("Decymetry: ", decymetry)
print("Milimetry: ", milimetry)
print("Mile: ", mile)

print("*"*50)

print("Zadanie 4")
podstawa = float(input("Podaj długość podstawy trójkąta: ")) #ustawienie danycj
wysokosc = float(input("Podaj wysokość trójkąta: ")) # ustawinie danych
pole = (podstawa * wysokosc) / 2
print("Pole trójkąta wynosi: ", pole)

print("*"*50)

print("Zadanie 5")
liczba_czterocyfrowa = input("Podaj czterocyfrowa liczbe: ")
print(liczba_czterocyfrowa[3], liczba_czterocyfrowa[2], liczba_czterocyfrowa[1], liczba_czterocyfrowa[0])