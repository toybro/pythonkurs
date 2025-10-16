lista_liczb = list(range(0, 11, 2))
odwrocona_lista_liczb = list(range(11, 0, -2))  # Liczenie do tylu ZAWSZE musi mieć określony krok
print("Lista liczb: ", lista_liczb)
print("Odwrocona lista liczb: ", odwrocona_lista_liczb)

szukana_liczba = 3

print("Sprawdzanie czy w liscie jest szukana liczba:", "\n", szukana_liczba in lista_liczb, "\n",
      szukana_liczba in odwrocona_lista_liczb)  # Sprawdzanie IN czy w liscie jest liczba

print("*" * 50)

print(f"Indeks szukanej liczby {szukana_liczba} w odwrocona_lista_liczb: {odwrocona_lista_liczb.index(szukana_liczba)}")

if szukana_liczba in lista_liczb:
      print(f"Indeks szukanej liczby {szukana_liczba} w lista_liczb: {lista_liczb.index(szukana_liczba)}")
else:
      print(f"szukana_liczba({szukana_liczba}) Nie znajduje się w lista_liczb")

