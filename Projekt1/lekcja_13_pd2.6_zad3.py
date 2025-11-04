print("Policz liczbę liczb całkowitych z zakresu od 100 do 999, które mają dwie identyczne cyfry.")
licznik = 0
for i in range(100, 1000):
    s = str(i)
    if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
        licznik += 1
print("Liczba takich liczb:", licznik)