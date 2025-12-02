"""
Stwórz funkcję, która sprawdzi, czy liczba podana w argumencie jest pierwsza.
Funkcja powinna przyjmować wartość numeryczną, a zwracać powinna wartość logiczną
True/False.

Np.

Dla 11 funkcja zwróci True, natomiast dla 12 -> False.

1,2.,3.,4,5.,6,7.8,9,10,11.,12,13.,14,15
"""

def czy_pierwsza_liczba(liczba):
    if liczba < 2:
        return False
    for i in range(2, (int(liczba**(0.5) + 1))):
        if liczba % i == 0:
            return False
    return True

liczba_user = (input("Podaj liczbę: "))
while not liczba_user.isdigit():
    print("Niepoprawne dane!")
    liczba_user = (input("Podaj liczbę: "))
print(czy_pierwsza_liczba(int(liczba_user)))