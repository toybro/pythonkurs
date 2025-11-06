def generuj_raport(*args, **kwargs):
    print("RAPORCIK")

    ocena = kwargs.get("ocena", "Brak oceny")
    odpowiedz = kwargs.get("odpowiedz", "Brak odpowiedzi")
    opis = kwargs.get("opis", "Brak opisu")

    print(f"Ocena: {ocena}")
    print(f"Odpowiedź: {odpowiedz}")
    print(f"Opis: {opis}")

    if args:
        print("\nDodatkowe uwagi:")
        i = 1
        for komentarz in args:
            print(f"{i}. {komentarz}")
            i += 1
    else:
        print("\nBrak opclonalnych uwag.")



generuj_raport(
    ocena=int(input("Podaj ocenę: ")),
    odpowiedz=input("Podaj odpowiedź: "),
    opis=input("Podaj opis: ")
)