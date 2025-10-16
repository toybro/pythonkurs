print("Funkcja range: ", range(20))  # Zwróci 0 i 20
print("Funkcja range od 0 do 19: ", list(range(20)))  # Zwróci od 0 do 19 (20 Elementów)
print("Funkcja range od 5 do 24: ", list(range(5, 25)))  # Zwróci od 5 do 24

print("Lista range liczb od -5 do 25 co 3 krok", list(range(-5, 25, 3)))

for liczba in range(5):  # Wyświetlenie range w pętli for dla "liczba"
    print("Liczba: ", liczba)

print("[]" *50)

for liczba in [0, 1, 2, 3, 4]:
    print("Liczba: ", liczba)

