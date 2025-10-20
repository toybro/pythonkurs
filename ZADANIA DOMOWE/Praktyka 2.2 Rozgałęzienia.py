print("Zadanie 1")

print("Obliczanie czasu do północy")
sekundy_od_poczatku = int(input("Podaj liczbę sekund od początku dnia: "))
sekundy_w_dobie = 24 * 60 * 60
pozostalo_sekund = sekundy_w_dobie - sekundy_od_poczatku
godziny = pozostalo_sekund // 3600
minuty = (pozostalo_sekund % 3600) // 60
sekundy = pozostalo_sekund % 60

print(f"Do północy pozostało: {godziny} godzin, {minuty} minut, {sekundy} sekund.")

print("*"*50)
print("Zadanie 2")

srednica = float(input("Podaj średnicę okręgu: "))
print("Wybierz opcję:")
print("1 - Oblicz pole")
print("2 - Oblicz obwód")
wybor = int(input("Twój wybór: "))
pi = 3.14159
promien = srednica / 2
if wybor == 1:
    pole = pi * promien * promien
    print(f"Pole okręgu wynosi: {pole}")
elif wybor == 2:
    obwod = pi * srednica
    print(f"Obwód okręgu wynosi: {obwod}")
else:
    print("Niepoprawny wybór.")

print("*"*50)
print("Zadanie 3")

print("Obliczanie kosztu konsoli z rabatem")
cena_konsoli = float(input("Podaj cenę jednej konsoli: "))
ilosc = int(input("Podaj ilość konsol: "))
rabat = float(input("Podaj rabat w procentach: "))
print("Wybierz opcję:")
print("1 - Całkowita kwota zamówienia z rabatem")
print("2 - Cena jednej konsoli po rabacie")
wybor = int(input("Twój wybór: "))
if wybor == 1:
    cena_po_rabacie = cena_konsoli * (1 - rabat / 100)
    laczna_kwota = cena_po_rabacie * ilosc
    print(f"Całkowita kwota zamówienia wynosi: {laczna_kwota} zł")
elif wybor == 2:
    cena_po_rabacie = cena_konsoli * (1 - rabat / 100)
    print(f"Cena jednej konsoli po rabacie wynosi: {cena_po_rabacie} zł")
else:
    print("Niepoprawny wybór.")

print("*"*50)
print("Zadanie 4")

print("Obliczanie czasu pobierania pliku")

rozmiar_gb = float(input("Podaj rozmiar pliku w GB: "))
przepustowosc_bps = float(input("Podaj przepustowość łącza w bitach na sekundę: "))
print("Wybierz jednostkę czasu:")
print("1 - Godziny")
print("2 - Minuty")
print("3 - Sekundy")
wybor = int(input("Twój wybór: "))
rozmiar_bit = rozmiar_gb * 1024 * 1024 * 1024 * 8
czas_sekundy = rozmiar_bit / przepustowosc_bps
if wybor == 1:
    czas_godziny = czas_sekundy / 3600
    print(f"Pobranie pliku zajmie około {czas_godziny} godzin.")
elif wybor == 2:
    czas_minuty = czas_sekundy / 60
    print(f"Pobranie pliku zajmie około {czas_minuty} minut.")
elif wybor == 3:
    print(f"Pobranie pliku zajmie około {czas_sekundy} sekund.")
else:
    print("Niepoprawny wybór.")

print("*" * 50)
print("Zadanie 5")

print("Podaj godzinę (od 0 do 23):")
godzina = int(input("Godzina: "))
if 0 <= godzina < 6:
    print("Good Night")
elif 6 <= godzina < 13:
    print("Good Morning")
elif 13 <= godzina < 17:
    print("Good Day")
elif 17 <= godzina < 24:
    print("Good Evening")
else:
    print("Niepoprawna godzina. Podaj wartość od 0 do 23.")