lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

wynik = tuple((x * 2) for x in lista if x % 2 == 0) #<--- To jest wyrazenie listowne jako tupla
print(wynik)

wynik = {(x * 2) for x in lista if x % 2 == 0} #<--- To jest wyrazenie listowne jako slownik
print(wynik)

ksiazka_tel = {"Policja": 997, "Pizzeria": 123456789, "Numer alarmowy": 112}
nowy_slownik = {wartosc: klucz for klucz, wartosc in ksiazka_tel.items()}
print(nowy_slownik)
