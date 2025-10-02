lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
szukana_liczba = int(input("Podaj szukaną liczbę"))
#szukana_liczba = int(szukana_liczba)
for element in lista:
    if element == szukana_liczba:
        print("Znaleziona:", element)
        break
    print("Przetwarzanie elementów listy", element)

print("Koniec pętli")