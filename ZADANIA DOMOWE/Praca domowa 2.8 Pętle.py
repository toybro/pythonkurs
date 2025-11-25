def pokaz_menu():
    print("\n=== MENU GWIAZDEK ===")
    print("a. Wzór A")
    print("b. Wzór B")
    print("c. Wzór C")
    print("d. Wzór D")
    print("e. Wzór E")
    print("f. Wzór F")
    print("g. Wzór G")
    print("h. Wzór H")
    print("i. Wzór I")
    print("j. Wzór J")
    print("q. Zakończ program")

def pokaz_wzor(litera):
    wzory = {
        "a": ["***", " **", "  *"],
        "b": ["*  ", "** ", "***"],
        "c": ["***", " * ", "   "],
        "d": ["***", " * ", "***"],
        "e": ["***", " * ", "***"],
        "f": ["* *", "***", "* *"],
        "g": ["*  ", "** ", "*  "],
        "h": ["  *", " **", "  *"],
        "i": ["***", "** ", "*  "],
        "j": ["  *", " **", "***"]
    }

    wzor = wzory.get(litera)
    if wzor:
        print(f"\nWybrano wzór {litera.upper()}:\n")
        for linia in wzor:
            print(linia)
    else:
        print("Nieznany wzór.")

def uruchom_program():
    while True:
        pokaz_menu()
        wybor = input("Wybierz wzór (a–j) lub 'q' aby zakończyć: ").lower()

        if wybor == "q":
            print("Do zobaczenia!")
            break
        elif wybor in "abcdefghij":
            pokaz_wzor(wybor)
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

uruchom_program()