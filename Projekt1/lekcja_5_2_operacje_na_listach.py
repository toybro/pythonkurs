pierwsza_lista = [1, 2, 3]
druga_lista = ["a", "b", "c"]
suma_list = pierwsza_lista + druga_lista

print("Suma list: ", suma_list, sep="\n")

trzecia_lista = [4, 5, 6]
print("Suma pierwszej i trzeciej listy:", pierwsza_lista + trzecia_lista, sep="\n")

rozwiazanie_1 = [pierwsza_lista[0]+trzecia_lista[0],pierwsza_lista[1]+trzecia_lista[1],pierwsza_lista[2]+trzecia_lista[2]]
print("Najprostrza suma 1 i 3 listy:", rozwiazanie_1)#Suma konkretnych elementów

indeks = 0

for _ in pierwsza_lista:
    trzecia_lista[indeks] = pierwsza_lista[indeks]+trzecia_lista[indeks] #Dodawanie pierwszej listy do trzeciej
    indeks += 1 #Indeks zwiększa się o 1

print("Wartość 3 listy po modyfikacji:", trzecia_lista)
