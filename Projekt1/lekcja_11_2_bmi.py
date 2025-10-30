print("Obliczanie BMI")

def oblicz_bmi(waga, wzrost, imie):
    bmi = waga / (wzrost ** 2)
    print(f"Twoje BMI {imie} wynosi: {bmi:.2f}")
    if bmi < 18.5:
        print("Masz niedowagę.")
    elif bmi < 25:
        print("Twoja waga jest prawidłowa.")
    elif bmi < 30:
        print("Masz nadwagę.")
    else:
        print("Masz otyłość.")


waga = float(input("Podaj wagę w kilogramach: "))
wzrost = float(input("Podaj wzrost w metrach: "))
imie = input("Podaj swoje imie: ")
oblicz_bmi(waga, wzrost, imie)
