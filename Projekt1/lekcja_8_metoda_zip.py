lista_zakupow = ['jajka', 'szynka', 'ser']
ilosci = [4, 2, 3]
#ZIP TO PAKOWANIE
print("Lista zakupow: ", lista_zakupow)
print("Ilosci", ilosci)
print("Funkcja zip: ", zip(lista_zakupow, ilosci))
print("Listy po spakowaniu:" ,list(zip(lista_zakupow, ilosci)))

dluzsza_lista = ['red', 'hot', 'chilli', 'peppers']
krotsza_lista = ['Czerwone', 'gorace', 'chilli']
print(f"Dluzsza lista: ({len(dluzsza_lista)})' - {dluzsza_lista}")
print(f"Krotsza lista: ({len(krotsza_lista)})' - {krotsza_lista}")

print("Lista po spakowaniu:", list(zip(dluzsza_lista, krotsza_lista)))

print("*" * 50)
print("Lista po spakowaniu:", list(zip(lista_zakupow, dluzsza_lista, krotsza_lista)))

print(list(zip("51", "51"))) #TYLKO STRINGI I KROTKI SA ITEROWALNE