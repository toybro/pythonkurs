def konfiguracja_profilu(imie, *args, **kwargs):

    """
    Przyjmuje imie, opcjonalne argumenty pozycyjne (*args)
    oraz ustawienia profilu jako argumemty nazwane (**kwargs)
    
    """
    print(f"Konfiguracja profilu dla: {imie}")

    for klucz, wartosc in kwargs.items():
        print(f"\t - Ustawienia {klucz}: {wartosc}")



konfiguracja_profilu("Andrzej", wiek=33, waga=75, wzrost=175, miasto="Gdańsk")
