def konfiguracja_profilu(imie, *args, **kwargs):
    """
    Przyjmuje imie, opcjonalne argumenty pozycyjne (*args)
    oraz ustawienia naszego profilu jako argumenty nazwane (**kwargs)
    """
    print(f"Konfiguruje profil dla {imie}")

    for klucz, wartosc in kwargs.items():
        print(f"\t- Ustawienia {klucz.capitalize()}: {wartosc}")


konfiguracja_profilu("Bartek", wiek=33, waga=75, wzrost=175, miasto="Gdańsk")
