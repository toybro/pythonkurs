"""
Stwórz funkcję, która obliczy liczbę małych i wielkich liter w ciągu.

np. dla : "The quick Brown Fox" oczekiwany wynik : Liczba wielkich liter : 3,
liczba małych liter : 13

Podpowiedź:

wykorzystaj pętlę, instrukcję warunkową i odpowiednie metody dla stringa.
"""

# tekst = input("Podaj tekst: ")
# male = 0
# duze = 0
# for litera in tekst:
#     if litera.isupper():
#         male += 1
#     if litera.islower():
#         duze += 1
# print(f"Dużych liter jest {duze} a małych :{male}")

tekst = input("Podaj tekst: ")

liczba_malych = 0
liczba_duzych = 0

for znak in tekst:
    if znak.islower():
        liczba_malych += 1
    elif znak.isupper():
        liczba_duzych += 1

print(f"Liczba małych liter: {liczba_malych}")
print(f"Liczba dużych liter: {liczba_duzych}")