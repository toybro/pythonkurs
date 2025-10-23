lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

wynik = tuple((x * 2) for x in lista if x % 2 == 0) #<--- To jest wyrazenie listowne jako tupla
print(wynik)

wynik = {(x * 2) for x in lista if x % 2 == 0} #<--- To jest wyrazenie listowne jako slownik
print(wynik)

ksiazka_tel = {"Policja": 997, "Pizzeria": 123456789, "Numer alarmowy": 112}
nowy_slownik = {wartosc: klucz for klucz, wartosc in ksiazka_tel.items()}
print(nowy_slownik)
################################
print("*"*50)
ksiazka_tel = {"Policja": 997, "Pizzeria": 123456789, "Numer alarmowy": 112}
nowy_slownik = {}

for klucz, wartosc in ksiazka_tel.items():
    nowy_slownik[wartosc] = klucz

print(nowy_slownik)


ksiazka_tel["Andrzej"] = 987654321


lista_slow = ["ala", "ola", "alek", "mirek", "ela"]
dlugosc_slow = {}
slowa = set(lista_slow)
for slowo in slowa:
    dlugosc_slow[slowo] = len(slowo)
print(dlugosc_slow)
