lista = list(range(100, 1000))
print(lista)
policz_2_identyczne = 0

for liczba in lista:
    liczba_na_str = str(liczba)
    str_na_set = set(liczba_na_str)
    ilosc_w_set_unikalnych_liczb = len(str_na_set)
    if ilosc_w_set_unikalnych_liczb == 2:
        policz_2_identyczne = policz_2_identyczne + 1 # policz_2_identyczne+=1

print(policz_2_identyczne)
