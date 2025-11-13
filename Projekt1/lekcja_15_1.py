
cyfra0 = "zero"
cyfra1 = "jeden"
cyfra2 = "dwa"
cyfra3 = "trzy"
cyfra4 = "cztery"
cyfra5 = "pięć"
cyfra6 = "sześć"
cyfra7 = "siedem"
cyfra8 = "osiem"
cyfra9 = "dziewięć"
minus = "minus"


liczba = input("Podaj liczbę: ")



print("Słownie:", end=" ")
for znak in liczba:
    if znak == "0":
        print(cyfra0, end=", ")
    elif znak == "1":
        print(cyfra1, end=", ")
    elif znak == "2":
        print(cyfra2, end=", ")
    elif znak == "3":
        print(cyfra3, end=", ")
    elif znak == "4":
        print(cyfra4, end=", ")
    elif znak == "5":
        print(cyfra5, end=", ")
    elif znak == "6":
        print(cyfra6, end=", ")
    elif znak == "7":
        print(cyfra7, end=", ")
    elif znak == "8":
        print(cyfra8, end=", ")
    elif znak == "9":
        print(cyfra9, end=", ")
    elif znak == "-":
        print(minus, end=", ")
    else:
        print("[nieznany znak]", end=", ")
