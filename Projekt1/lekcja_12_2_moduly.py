def pokaz():
    print(f"To jest nazwa pliku {__name__} z naszego __name__")

pokaz()
if __name__ == "__main__":
    pokaz()
    from lekcja_11_2_bmi import oblicz_bmi
    import lekcja_8_metoda_zip