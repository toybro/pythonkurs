def ciąg_liczb(limit):
    i = 0
    while i < limit:
        yield i
        i += 1


def nasz_range(do,od=0,skok=1):
    while od < do:
        yield od
        od += skok



#Użycie generatora w pętli for
for liczba in ciąg_liczb(10):
    print(liczba)

print(list(nasz_range(15, 5)))

def fibonacci(limit):
    a, b = 0, 1
    for i in range(limit):
        yield a
        a, b = b, a + b
licebka = int(input("Podaj liczba: "))
for liczba in fibonacci(licebka):
    print(liczba)
