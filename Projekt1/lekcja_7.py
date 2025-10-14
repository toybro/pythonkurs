lista = [1, 6, 3, 4]
lista.append(5) #dodaje element do listy
print(f"Zmienna lista po dodanie wartości  5: \n{lista}")
print("Dodanie liczby 5 w princie za pomocą w metody append: ", lista.append(5))
print(f"Zmienna lista po dodaniu wartości 5: {lista}")
print(f"Użycie metody sort w funkcji print: {lista.sort()}")
print(f"Zmienna lista po użyciu metody sort: {lista}")

tekst = "Nasze zdanie"

print(f"To jest nasza zmiena tekst po użyciu upper w funkcji print: {tekst.upper()}")
print(f"Na tym tekście użyć metody upper".upper())

print("Tekst {} {}".format("elementy", 1)) #Dodawanie informacji w środku tekstu
print("Tekst {} {} {} informacje dalsze".format("elementy", 1, 2))
print("Tekst {b} {c} {a} informacje dalsze".format(a="elementy", b=1, c=2)) #nazywanie elementów
print("Tekst {2} {1} {0} informacje dalsze".format("elementy", 1, 2)) #numerowanie elementów
print(" {} {} {} {} {} {} ".format(*lista)) #Wypisuje w princie elementy z listy

