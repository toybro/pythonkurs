import random


opcje = ["kamień", "papier", "nożyce"]


print("Gramy w 'Kamień, papier, nożyce'!")
print("Wybierz jedną z opcji:")
print("1 - kamień")
print("2 - papier")
print("3 - nożyce\n")


wybor = input("Wpisz numer (1, 2 lub 3): ")


if wybor in ["1", "2", "3"]:
    uzytkownik = opcje[int(wybor) - 1]
    komputer = random.choice(opcje)


    print(f"\nTy wybrałeś: {uzytkownik}")
    print(f"Komputer wybrał: {komputer}")


    if uzytkownik == komputer:
        print("Remis")
    elif (uzytkownik == "kamień" and komputer == "nożyce") or \
         (uzytkownik == "papier" and komputer == "kamień") or \
         (uzytkownik == "nożyce" and komputer == "papier"):
        print("Wygrałeś")
    else:
        print("Przegrałeś")
else:
    print("Niepoprawny wybór. Wpisz 1, 2 lub 3.")