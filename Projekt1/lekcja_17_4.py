licznik_globalny = 0  # G


def licznik_otaczajacy():
    licznik_otaczenia = 0  # E

    def licznik_otaczajacy_2():
        licznik_otaczenia_2 = 0  # E
        licznik_otaczenia = 10
        def inkrementuj():
            nonlocal licznik_otaczenia  # Modyfikujemy zmienna E
            nonlocal licznik_otaczenia_2  # Modyfikujemy zmienna E
            global licznik_globalny  # Modyfikujemy zmienna G

            licznik_otaczenia += 1
            licznik_globalny += 1
            licznik_otaczenia_2 += 2

        inkrementuj()
        inkrementuj()
        print(f"E (Otoczający_2) po inkrementacji: {licznik_otaczenia_2,licznik_globalny,licznik_otaczenia}")

    licznik_otaczajacy_2()
    print(f"E (Otoczający) po inkrementacji: {licznik_globalny,licznik_otaczenia}")


licznik_otaczajacy()
print(f"G (Globalny) po inkrementacji: {licznik_globalny}")
