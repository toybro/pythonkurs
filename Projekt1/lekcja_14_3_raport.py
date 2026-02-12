def generuj_raport(tytul_raportu, *args, **kwargs):
    """
    Generuje raprot z podanym tytułem, listą ocen (*args)
    oraz uwagi dodatkowe (**kwargs).
    """

    print("___ RAPORT ___")
    print(f"Tytuł: {tytul_raportu}")

    if args:
        print(f"\nOceny (Krotka *args): {args}")
    else:
        print("\nBrak podanych ocen.")

    print(f"\nUwagi dodatkowe (*kwargs):")
    if kwargs:
        for klucz, wartosc in kwargs.items():
            print(f"\t>{klucz.replace('_', " ").capitalize()} - {wartosc}")
    else:
        print("Brak uwag dodatkowych.")
    print("_"*20)

if __name__ == "__main__":
    generuj_raport("Raport Kwartał 1", 4.5, 5.0, 3.5, 4.0,
                   data="06-11-2025",
                   projket_zaliczony=False,
                   uwagi_specjalne="Wymaga porpawy w sekcji X")

    print("\n" + "=" * 20 + "\n")

    generuj_raport("Raport Wstępny",
                   osoba_odpowiedzilna="Jan Kowalski")
