print("*" * 50)
print("Zadanie 1")
print("Wypisz wszystkie liczby pierwsze w podanym przez użytkownika zakresie.")
start = int(input("Podaj początek zakresu: "))
end = int(input("Podaj koniec zakresu: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()

print("*" * 50)
print("Zadanie 2")
print("Wydrukuj tabliczkę mnożenia dla wszystkich liczb od 1 do 10.")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}*{j} = {i*j}", end="\t")
    print()

print("*" * 50)
print("Zadanie 3")
print("Wydrukuj tabliczkę mnożenia w podanym przez użytkownika zakresie.")
start = int(input("Podaj początek zakresu: "))
end = int(input("Podaj koniec zakresu: "))

for i in range(start, end + 1):
    for j in range(1, 11):
        print(f"{i}*{j} = {i*j}", end="\t")
    print()

