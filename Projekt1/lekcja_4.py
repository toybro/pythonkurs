licznik = 0
while licznik <= 5:
    print("Wartość zmiennej :", licznik)
    licznik = licznik + 1
    print("Zwiększamy licznik o jeden i powtarzamy pętle aż licznik będzie równy 5")

print("Koniec pętli.")

while True:
    print("Pętla nieskończona")
    stop = input("Wpisz 'stop', aby przerwać: ")
    if stop.lower() == "stop":
        print("Zatrzymano pętlę.")
        break
