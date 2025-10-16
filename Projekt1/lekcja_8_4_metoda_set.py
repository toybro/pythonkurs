zbior_1 = set(range(5))
zbior_2 = {0,1,2,3,4}

print(f"Zbior 1: {zbior_1}")
print(f"Zbior 2: {zbior_2}")

lista = [50]*10

print(f"Lista 50*10: {lista}")
print(f"Lista jako zbior 50*10: {set(lista)}")
print(f"lista po usunieciu duplikatow {list(set(lista))}")

zbior_2.add(5) #ADD DODAJE TYLKO JEDEN ELEMENT
zbior_2.add(6)

print(f"zbior_2 po dodaniu elementow 5 i 6: {zbior_2}")
zbior_2.update({9,8,7}) # UPDATE DODAJE CALY ZBIOR  (W LISTACH METODA EXTEND)
print(f"zbior_2 po dodaniu zbioru 9,8,7: {zbior_2}")

