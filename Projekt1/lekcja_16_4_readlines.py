with open("plik.txt") as f:
    wszystkie_linie = f.readlines()
    print(wszystkie_linie)
    for linia in wszystkie_linie:
        print(linia, end="")


def funkcja():
    return [1, 2, 3, 4, 5]  # "asdasdasd dasdasd asdas"


for linia in funkcja():
    print(linia)

with open("plik.txt") as f:
    print(f)
    for linia in f:
        print(linia, end="")