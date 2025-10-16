pusty_slownik = {}

print(f"pusty_slownik: zawartosc - {pusty_slownik}\n\tTyp - {type(pusty_slownik)} ")  # \t to tabulator

ksiazka_tel = {"Policja": 997, "Pizzeria": 123456789, "Numer alarmowy": 112}

print("Wartość klucza pizzeria z ksiazka_tel: ", ksiazka_tel["Pizzeria"])

ksiazka_tel["Pizzeria"] = 987654321  # ZMIANA wartości klucza Pizzeria

print("Wartość klucza pizzeria z ksiazka_tel po zmianie: ", ksiazka_tel["Pizzeria"])

ksiazka_tel["Mama"] = 789456123  # Dodanie klucza do ksiazka_tel

print("Wartość klucza Mama dodana do ksiazka_tel: ", ksiazka_tel["Mama"])
print("*" * 50)
print(f"Cała ksiazka_tel: {ksiazka_tel}")  # Sprawdzanie czy jest tata w ksiazka_tel
if "Tata" in ksiazka_tel:
    print("Tata w ksiazka_tel: ", ksiazka_tel["Tata"])
else:
    print("Nie ma taty ")

print("Tata w ksiazka_tel: ", ksiazka_tel.get("Tata"))  # Sprawdzanie za pomocą metody GET

print(ksiazka_tel.keys())  # Wyświetlanie samych wartości
print(ksiazka_tel.values())  # Wyświetlanie samych wartości
print(ksiazka_tel.items())  # Wyświetlanie kluczy i wartości

for klucze in ksiazka_tel.keys():
    print(f"Wyświetla klucze z ksiazka_tel {klucze}")

print("*" * 50)

for itemy in ksiazka_tel.items():
    print(f"Wyświetla klucze i wartości z ksiazka_tel {itemy}")

print("*" * 50)

for wartosc in ksiazka_tel.values():
    print(f"Wyświetla wartości z ksiazka_tel {wartosc}")

print("*" * 50)
print("Wyświetla książkę telefoniczną")
for klucz, wartosc in ksiazka_tel.items():
    print(f"\n\t-{klucz}: {wartosc}")