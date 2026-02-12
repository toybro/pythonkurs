import time
def miernik_czasu(funkcja):
    #funkcja wew (wrapper)
    #Ona przyjmuje argsy i kwargsy (argumenty nazwane i nienazwane)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        wynik = funkcja(*args, **kwargs)
        end_time = time.time()
        czas_wykonania = end_time - start_time

        print(f"Funkcja '{funkcja.__name__}' wykonana w {czas_wykonania:.4f}s")

        return wynik #zwraca wynik oryginalnej funkcji
    return wrapper
@miernik_czasu
def licz_do_n(n):
    """Prosta funkcja która zlicz."""
    suma = 0
    for i in range(n):
        suma += i
    return suma

wynik_liczenia = licz_do_n(1000000)
print(f"Zwroconow ynik: {wynik_liczenia}")