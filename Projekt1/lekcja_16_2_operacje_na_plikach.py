f = open("plik.txt", 'w',)

# r - tylko do odczytu
# w - do zapisu, jeśli plik nie isnieje to zostanie utworzony,
#     jeżeli istnieje jego stara zawratość zostanie usunięta
# x - do tworzenia, opercja nie powiedzie się, jeżeli plik już istnieje.
# a - dopisywanie, jeśli plik nie isnieje to zostanie utworzony,
#     jeżeli istnieje to nowa wartość zostanie dopisana.
# + -

f.write("Ala ma Kota")
f.write("asdasdasdas")

f.close()
print(f)

with open('plik1.txt', 'a+') as file:
    file.write("1asdasdasdas")

