print("*" * 50)
print("Zadanie 1")
print("Użytkownik wpisuje rozmiar boków kwadratu. Wydrukuj pełny kwadrat.")
rozmiar = int(input("Podaj rozmiar boku kwadratu: "))
for _ in range(rozmiar):
    print("*" * rozmiar)

print("*" * 50)
print("Zadanie 2")
print("Użytkownik wpisuje szerokość i wysokość prostokąta. Wydrukuj pełny prostokąt o podanej wysokości i szerokości.")
wysokosc = int(input("Podaj wysokość prostokąta: "))
szerokosc = int(input("Podaj szerokość prostokąta: "))
for _ in range(wysokosc):
    print("*" * szerokosc)

print("*" * 50)
print("Zadanie 3")
print("Użytkownik wpisuje rozmiar boków kwadratu. Wydrukuj pusty kwadrat (wyświetlone zostaną tylko jego boki).")
rozmiar = int(input("Podaj rozmiar boku kwadratu: "))
for i in range(rozmiar):
    if i == 0 or i == rozmiar - 1:
        print("*" * rozmiar)
    else:
        print("*" + " " * (rozmiar - 2) + "*")

print("*" * 50)
print("Zadanie 4")
print("Użytkownik wpisuje długość i szerokość prostokąta. Wydrukuj pusty prostokąt (wyświetlane są tylko jego boki).")
dlugosc = int(input("Podaj długość prostokąta: "))
szerokosc = int(input("Podaj szerokość prostokąta: "))
for i in range(dlugosc):
    if i == 0 or i == dlugosc - 1:
        print("*" * szerokosc)
    else:
        print("*" + " " * (szerokosc - 2) + "*")