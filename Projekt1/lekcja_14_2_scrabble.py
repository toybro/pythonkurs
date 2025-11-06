def punkty_scrabble(slowo):
    wartosci = {
        1: "A E I N O R S W Z",
        2: "C D K L M P T Y",
        3: "B G H J Ł U",
        5: "Ą Ę F Ó Ś Ż",
        6: "ĆŃ",
        7: "Ź",
        9: "Q V X"
    }

    mapa_punktow = {}
    for punkty, litery in wartosci.items():
        for litera in litery.split():
            mapa_punktow[litera] = punkty

    suma = 0
    for znak in slowo.upper():
        suma += mapa_punktow.get(znak, 0)

    return suma

slowo = input("Podaj slowo: ")

punkty_scrabble(slowo)
print(f"Podałeś slowo: {slowo}")
print(f"{punkty_scrabble(slowo)} Tyle pukntow ma słowo")