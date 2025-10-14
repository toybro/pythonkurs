lista = [1, 2, 3, 4, 5]
print(f"To nasza lista: {lista}")

element_pop = lista.pop() #usuwa ostatni element z listy i zastępuje element_pop piątką
#   .pop usuwa domyślnie element z listy

print(f"To nasza lista po metodzie pop: {lista}")
print(f"Zmienna element_pop: {element_pop}")

lista.pop()
print(f"Zmienna lista po drugim popie: {lista}")
lista.pop(1)
print(f"Zmienna lista po trzecim popie z indeksem 1: {lista}")

lista_2 = [1]
lista_2.pop()
print(f"lista2 ma jeden element a po użyciu pop jest pusto {lista_2}")

lista_3 = [2]
lista_3.pop()
print(f"lista_2.pop co zawiera{lista_3.pop}") #wywołanie adresu hex metody
print(hex(id(lista_3))) #Adres hex lista_3


del lista  #Skasowanie listy lista

#print(lista)

lista = [1, 2, 3, 4, 5]
print(f"lista {lista}")


