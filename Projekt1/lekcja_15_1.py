"""
Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr
na formę tekstową

112 -> 'jeden jeden dwa'
9973 -> 'dziewięc dziewięc siedem trzy'

Podpowiedź: Potrzebujecie funkcji input(), słownika oraz pętli.
"""

# liczby = ['zero', 'jeden', 'dwa', 'trzy', 'cztery' , 'pięć', 'sześć' , 'siedem' , 'osiem' , 'dziewięć']
# while True:
#     user_1 = input("Podaj liczbe do przeksztalcenia: ")
#     for liczba in user_1:
#         print(liczby[int(liczba)], end=" ")
#     print()

# cyfra0 = "zero"
# cyfra1 = "jeden"
# cyfra2 = "dwa"
# cyfra3 = "trzy"
# cyfra4 = "cztery"
# cyfra5 = "pięć"
# cyfra6 = "sześć"
# cyfra7 = "siedem"
# cyfra8 = "osiem"
# cyfra9 = "dziewięć"
# minus = "minus"
#
# liczba = input("Podaj liczbę: ")
#
# print("Słownie:", end=" ")
# for znak in liczba:
#     if znak == "0":
#         print(cyfra0, end=", ")
#     elif znak == "1":
#         print(cyfra1, end=", ")
#     elif znak == "2":
#         print(cyfra2, end=", ")
#     elif znak == "3":
#         print(cyfra3, end=", ")
#     elif znak == "4":
#         print(cyfra4, end=", ")
#     elif znak == "5":
#         print(cyfra5, end=", ")
#     elif znak == "6":
#         print(cyfra6, end=", ")
#     elif znak == "7":
#         print(cyfra7, end=", ")
#     elif znak == "8":
#         print(cyfra8, end=", ")
#     elif znak == "9":
#         print(cyfra9, end=", ")
#     elif znak == "-":
#         print(minus, end=", ")
#     else:
#         print("[nieznany znak]", end=", ")
#
#
cyfry_na_slowa = {
    "0": "zero",
    "1": "jeden",
    "2": "dwa",
    "3": "trzy",
    "4": "cztery",
    "5": "piec",
    "6": "szesc",
    "7": "siedem",
    "8": "osiem",
    "9": "dziewiec"
}

def zamien_cyfry_na_slowa(ciag_cyfr):
    wynik = []
    for cyfra in ciag_cyfr:
        if cyfra in cyfry_na_slowa:
            wynik.append(cyfry_na_slowa[cyfra])
        else:
            wynik.append(cyfra)
    return " ".join(wynik)


ciag = input("Podaj ciąg cyfr: ")
print("Zamienione cyfry:", zamien_cyfry_na_slowa(ciag))
