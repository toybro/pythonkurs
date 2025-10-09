# Metoda append/ dodawanie do listy
lista_1 = ["a", "b", "c"]
print("Lista lista_1, przed edycją: ", lista_1)
lista_1.append("d")
lista_1.append("e")
lista_1.append("f")
print("Lista lista_1 po dodawaniu d,e,f", lista_1)
lista_1.append(["f", "2"])
print("Lista lista_1 po dodawaniu d,e,f oraz zagnieżdżeniu drugiej listy w środku", lista_1)

print("Indeks 0 lista_1", lista_1[0])
print("Indeks -1 lista_1", lista_1[-1])
print("Indeks -1 lista_1 oraz indeksu 0 wewnątrz listy", lista_1[-1][0])
z, x, y = lista_1[0], lista_1[1], lista_1[2]
print("z:", z, "x: ", x, "y: ", y)
z, x, y = lista_1[:3]
print(f"z: {z}\nx: {x}\ny: {y}\nz")
z, x = x, z
print(z, x)
