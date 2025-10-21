lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


wynik = [(x * 2) for x in lista if x % 2 == 0] #<--- To jest wyrazenie listowne
print(wynik)

print("*"*50)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista2 = [102, 103, 104, 105]
wynik = [(x * y) for x in lista for y in lista2]  # <--- To jest wyrazenie listowne
print(wynik)
