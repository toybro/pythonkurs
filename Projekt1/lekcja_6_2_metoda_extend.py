#Metoda extend rozszerzania listy
lista_1 = [4, 5, 6]
lista_2 = [7, 8, 9]

lista_3 = lista_1 + lista_2
print("ID lista_1:", id(lista_1))
print("Wyświetlanie dodanych list 1 i 2", lista_3)

lista_1 += lista_2  # lista_1  = lista_1 + lista 2


print("Wyświetlanie dodanych list 1 i 2 jako lista_1", lista_1)

lista_4 = ["a", "b", "c"]
lista_1.extend(lista_4)
print("Wyświetlenie lista_1, rozszerzonej extend o lista_4", lista_1)
print("ID lista_1 po zmianie: ", id(lista_1))
