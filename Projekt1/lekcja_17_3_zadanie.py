a = 100


def zmienna_a():
    global a
    a = 200


print(f"Poziom 1: Przed wywołaniem funkcji, a = {a}")
zmienna_a()
print(f"Poziom 2: Po wywołaniem funkcji, a = {a}")
