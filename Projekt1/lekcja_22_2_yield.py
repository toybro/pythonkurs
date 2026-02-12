import sys

lista_milion = [i for i in range(1_000_000)]
print(f"Rozmiar listy (1M Elementów) : {sys.getsizeof(lista_milion)} bajtów")

generator_milion = (i for i in range(1_000_000))
print(f"Rozmiar generatora (1m Elementow) : {sys.getsizeof(generator_milion)} bajtów")