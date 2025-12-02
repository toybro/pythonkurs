def oblicz_bmi(waga, wzrost):
    wynik = waga / wzrost ** 2
    print("Z funkcji oblicz_bmi wynik:", wynik)

def oblicz_bmi(waga, wzrost):
    wynik = waga / wzrost ** 2
    print("Z funkcji oblicz_bmi wynik:", wynik)
    return


oblicz_bmi(90, 2)


def bmi(waga, wzrost):
    wynik = waga / wzrost ** 2
    if wynik > 25:
        return "Masz otyłość"
    elif wynik < 18.5:
        return "Masz niedowagę"
    else:
        return "Twoja waga jest OK."


moja_waga = 80
moj_wzrost = 1.75

moje_bmi = bmi(moja_waga, moj_wzrost)

print(f"Wartość zwrocona z zmiennej moje_bmi: {moje_bmi}")


def bmi_2(waga, wzrost):
    wynik = waga / wzrost ** 2
    if wynik > 25:
        return "Masz otyłość"
    elif wynik < 18.5:
        return "Masz niedowagę"
    return "Twoja waga jest OK."


waga_usera = float(input(f"Podaj swoją wagę w kg: "))
wzrost_usera = float(input(f"Podaj swoj wzrost w m: "))

print("Wartość z funkcji bmi_2:", bmi_2(waga_usera, wzrost_usera))


def bmi_3(waga, wzrost):
    wynik = waga / wzrost ** 2
    print("wynik:", wynik)
    if wynik > 25:
        print("Masz otyłość")
    if wynik < 18.5:
        print("Masz niedowagę")
    if wynik > 30:
        print("Jesteś po prostu gruby")
    print("Twoja waga jest OK.")


bmi_3(waga_usera, wzrost_usera)


def bmi_4(waga, wzrost):
    wynik = waga / wzrost ** 2
    if wynik > 25:
        return "Masz otyłość"
    if wynik < 18.5:
        return "Masz niedowagę"
    if wynik > 30:
        return "Jesteś po prostu gruby"
    return "Twoja waga jest OK."


print("Wartość z funkcji bmi_4:", bmi_4(waga_usera, wzrost_usera))


def bmi_5(waga, wzrost):
    wynik = waga / wzrost ** 2
    if wynik > 30:
        print("Jesteś po prostu gruby")
    elif wynik < 18.5:
        print("Masz niedowagę")
    elif wynik > 25:
        print("Masz otyłość")
    else:
        print("Twoja waga jest OK.")

    wartosc = f"Wynik funkcji wynik_bmi_5: {wynik}"
    return wartosc

print("*"*50,"\n")
wynik_bmi_5 = bmi_5(waga_usera, wzrost_usera)
print(wynik_bmi_5)

print(oblicz_bmi(90, 2))