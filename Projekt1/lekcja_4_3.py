#Sprawdzanie, która liczba w liście jest nieparzysta
lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for liczba in lista_liczb:
    if liczba % 2 == 0: # liczba modulo 2
        continue
    print("Liczba jest nieparzysta", liczba)

print("Koniec pętli 1.")
