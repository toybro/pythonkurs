def czy_palindrom(napis):
    odwrocony = ""
    for znak in napis:
        odwrocony = znak + odwrocony

    if napis == odwrocony:
        return True
    else:
        return False

tekst = input("Podaj słowo: ")

if czy_palindrom(tekst):
    print("palindrom")
else:
    print("nie palindrom")