#Robienie kopii listy

liczba = 11

print("Zmienna liczba: ", liczba)
kopia_liczby = liczba
print("Zmienna kopia_liczby: ", kopia_liczby)
liczba = 12
print("Zmienna liczba po zmianie: ", liczba)
print("Zmienna kopia_liczby", kopia_liczby)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Zmienna lista: ", lista)
kopia_listy = lista
print("Zmienna kopia_listy", kopia_listy)

lista[4] = None
print("Zmienna lista: ", lista)
print("Zmienna kopia_listy", kopia_listy)
print("*"*30)

print("ID liczba: ", id(liczba))
print("ID kopia_liczby: ", id(kopia_liczby))
print("ID lista: ", id(lista))
print("ID kopia_listy: ", id(kopia_listy))

lista_copy = lista.copy()
print("Zmienna lista_copy: ", lista_copy)
lista[-1] = "Koniec"
print("Zmienna lista: ", lista)
print("Zmienna kopia_listy", lista_copy)

print("*"*30)#Wyświetlenie 30 gwiazdek

lista_wycinek = lista[:]
print("Zmienna lista_wycinek", lista_wycinek)
lista[0] = "Początek" #Zmiana pierwszej pozycji oryginalnej listy na "Początek"
print("Zmienna lista: ", lista, end="\n")
print("Zmienna lista_wycinek", lista_wycinek)
