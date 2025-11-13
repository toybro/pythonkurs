def print_star_number(n):
    digits = {
        '0': [" *** ",
              "*   *",
              "*   *",
              "*   *",
              " *** "],
        '1': ["  *  ",
              " **  ",
              "  *  ",
              "  *  ",
              " *** "],
        '2': [" *** ",
              "*   *",
              "   * ",
              "  *  ",
              "*****"],
        '3': [" *** ",
              "    *",
              " *** ",
              "    *",
              " *** "],
        '4': ["   * ",
              "  ** ",
              " * * ",
              "*****",
              "   * "],
        '5': ["*****",
              "*    ",
              "**** ",
              "    *",
              "**** "],
        '6': [" *** ",
              "*    ",
              "**** ",
              "*   *",
              " *** "],
        '7': ["*****",
              "    *",
              "   * ",
              "  *  ",
              " *   "],
        '8': [" *** ",
              "*   *",
              " *** ",
              "*   *",
              " *** "],
        '9': [" *** ",
              "*   *",
              " ****",
              "    *",
              " *** "]
    }

    for row in range(5):
        line = ""
        for digit in str(n):
            line += digits.get(digit, "     ")[row] + "  "
        print(line)

def menu():
    tile_map = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9
    }

    while True:
        print("\n🧩 MENU KAFELKÓW:")
        for key in tile_map:
            print(f"{key.upper()} - Wzór odpowiadający cyfrze {tile_map[key]}")
        print("X - Zakończ")

        choice = input("Wybierz literę (A–J) lub X by zakończyć: ").lower()

        if choice == 'x':
            print("👋 Do zobaczenia!")
            break
        elif choice in tile_map:
            number = tile_map[choice]
            print(f"\n🔢 Cyfra {number} w gwiazdkach:")
            print_star_number(number)
        else:
            print("⚠️ Nieprawidłowy wybór. Spróbuj ponownie.")

menu()