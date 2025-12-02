"""
Stwórz funkcję, która sprawdzi, czy podany jako argument napis jest palindromem
(tj. czytany od przodu i wspak jest dokładnie taki sam, np. „kajak”, „Madam”).
"""

def palindrom(slowo):
    if slowo == slowo[::-1]:
        print(f"Slowo {slowo} jest palindromem")


palindrom("kajak")

def palindrom(slowo):
        print(f"Slowo {slowo} jest palindromem: {slowo == slowo[::-1]}")


palindrom("taczka")

def if_palindrom(text):
    text = "Hello!!!   world??   Python!"