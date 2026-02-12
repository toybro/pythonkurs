def generuj_parzyste():
    print("-> Start Generatora")
    yield 0
    print("-> Po pierwszym Yield")
    yield 2
    print("-> Po drugim yield")
    yield 4
    print("-> Koniec Generatora")

gen = generuj_parzyste()
print("Krok 1: Wywołanie fukcji next()")
print(next(gen))

print("Krok 2: Wywołanie fukcji next()")
print(next(gen))

print("Krok 3: Wywołanie fukcji next()")
print(next(gen))

try:
    print(next(gen))
except StopIteration:
    print("Koniec Sekwencji")