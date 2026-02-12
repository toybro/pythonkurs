def czy_izogram(slowo):
    slowo = slowo.lower()
    return len(slowo) == len(set(slowo))

print(__name__)
if __name__ == '__main__':
# Jeżeli uruchomimy ten plik to zmienna __name__ ma wartość '__main__'
# Gdy za impotujemy ten plik do innego pliku __name__ zwrócić nazwe pliku z tym kodem.
    while True:
        nasze_slowo = input("Podaj slowo: ")
        if czy_izogram(nasze_slowo):
            print(f"Słowo: {nasze_slowo} jest izogramem")
        else:
            print(f"Słowo: {nasze_slowo} nie jest izogramem")

        pytanie = input("Czychcesz kontynuować [T/N]")
        if pytanie.upper() != 'T':
            break

    while True:
        nasze_slowo = input("Podaj slowo: ")
        odpowiedz = "jest" if czy_izogram(nasze_slowo) else 'nie jest'
        print(f"Słowo: {nasze_slowo} {odpowiedz} izogramem")
        pytanie = input("Czychcesz kontynuować [T/N]")
        if pytanie.upper() != 'T':
            break