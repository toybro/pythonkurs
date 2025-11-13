print("Zadanie 1")
print("*"*50)

def analyze_number(number_str):
    digits = [int(d) for d in number_str]
    count = len(digits)
    total = sum(digits)
    average = total / count if count > 0 else 0
    zero_count = digits.count(0)

    print(f"\n📊 ANALIZA LICZBY: {number_str}")
    print(f"- Liczba cyfr: {count}")
    print(f"- Suma cyfr: {total}")
    print(f"- Średnia cyfr: {average:.2f}")
    print(f"- Liczba zer: {zero_count}")

def menu():
    while True:
        print("\nMENU:")
        print("1. Wpisz liczbę do analizy")
        print("2. Zakończ program")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            number = input("Podaj liczbę całkowitą (bez spacji): ")
            if number.isdigit():
                analyze_number(number)
            else:
                print("Błąd: wpisz tylko cyfry (np. 2137).")
        elif choice == '2':
            print("Papa")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

menu()