def pokaz():
    print(f"To jest nazwa pliku 'lekcja_12_2_moduly' - {__name__} z naszego __name__")
tekst = "Wiadomość"
pokaz()
if __name__ == "__main__":
    pokaz()
    from lekcja_11_2_bmi import bmi
    import lekcja_8_1_zip