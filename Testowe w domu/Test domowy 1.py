#imie = input("Podaj imie: ")
#wiek = input("Podaj wiek: ")
waga = input("Podaj wagę: ")
wzrost = input("Podaj wzrost: ")
bmi = 0
waga = float(waga)
wzrost = float(wzrost)
print("Teraz obliczymy Twoje BMI")
bmi = waga / wzrost ** 2
print("Twoje BMI to: ", bmi)

if bmi > 25:
    print("Masz nadwagę")
elif 18.5 <= bmi <=1 25:
    print("Jest idealnie")
else:
    print("Masz niedowagę")

print("Papa")