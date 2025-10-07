lista = ["to", "jest", "przykładowy", "tekst", 5, 10, 15, 25, 30]


print("To jest zawartość: ", lista)
print("To jest pojedyńczy element z listy o indeksie 1:", lista[1])
print("To jest ostatni element z listy o indeksie 1:", lista[3])
print("To jest ostatni element z listy o indeksie 1:", lista[-1])#Można użyć -1 jako ostatni element z listy

lista[2] = "ala ma kota"

print("Element z listy po zmianie. Indeks 2:", lista[2])

print("To są 2 elementy z listy o indeksach 1 i 2:", lista[1:3])

print("\nCała Lista", lista[::])
print("To jest co drugi element z listy:", lista[1:-2:2])

print("Elementy z listy od tyłu:", lista[::-1])#Wyświetli całą liste z krokiem -1 co spowoduje wyświetlenie listy od tyłu
print("Elementy z listy od tyłu, co drugi:", lista[::-2])#Wyświetli całą liste z krokiem -1 co spowoduje wyświetlenie listy od tyłu co drugi krok

print("Lista bez ostatniego elementu", lista[0:-1])

print("Lista bez pierwszego elementu:", lista[1:])

print("\nIlośc elementów w liście:", len(lista))#Zwraca ilość elementów w liście

print("Ile jest liter w słowie Python:",len("Python"))#Ilość liter w słowie python

print("Python", "Kolejny" + "tekst", sep="++", end="||")#Wymienia spacje na dwa plusy i zaczyna NASTĘPNEGO printa w tej samej linii
print("Kolejny print")
print("Nowy", "tekst", sep="\n"*3)#Separator między słowami dodaje 2 nowe linie gdyż pierwsza linia zaczyna się w słowie NOWY

