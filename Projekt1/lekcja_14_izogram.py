def czy_izogram(slowo):
    slowo = slowo.lower()
    return len(slowo) == len(set(slowo))
    pass


if __name__ == '__main__':
    #Jeżeli uruchomimy ten plik to zmienna __name__ ma wartość __main__
    #Gdy zaimportujemy ten plik do innego pliku __name__ zwróci nazwe pliku z tym kodem

    while True:
        nasze_slowo = input('Podaj slowo: ')
        wynik = czy_izogram(nasze_slowo)
        if wynik:
            print(f"Słowo: {nasze_slowo} jest izogramem")
        else:
            print(f"Słowo: {nasze_slowo} nie jest izogramem")

        pytanie = input("Czy chcesz kontynuować? \nT/N :")
        if pytanie.upper() != "T":
            break