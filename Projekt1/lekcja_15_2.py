def pozycja_najmniejszej(lista):
    if len(lista) == 0:
        return None

    najmniejsza = lista[0]
    pozycja = 0

    for i in range(1, len(lista)):
        if lista[i] < najmniejsza:
            najmniejsza = lista[i]
            pozycja = i

    return pozycja


tekst = input("Liczbyt podzielone przecinkami: ")
elementy = tekst.split(",")
lista_liczb = []

for e in elementy:
    lista_liczb.append(int(e.strip()))


wynik = pozycja_najmniejszej(lista_liczb)
print("Pozycja w lisxie najmniejszej liczby:", wynik)
