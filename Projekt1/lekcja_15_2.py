"""
Stwórzcie funckje Przyjmującą listę liczb całkowitych,a zwracającą informację,
na której pozycji znajduje się najmniejsz liczba.

Przykład:

Dla listy [42, 13, 56, 7, 12, 3, 85] funkcja ma zwrócić 5 ponieważ pod
tym indeksem w tej liście znajduje się element najmniejszy
"""


# def najmniejszy_index(wprowadzona_lista):
#     najmnejszy = min(wprowadzona_lista)
#     return wprowadzona_lista.index(najmnejszy)
#
# lista_usera = []
# ile_liczb_w_liscie = int(input("Wpisz ile liczb ma posiadać liczba: "))
# for i in range(ile_liczb_w_liscie):
#     liczba = int(input(f"Wprowadź {i + 1} liczbę: "))
#     lista_usera.append(int(liczba))
# print(f"Indeks dla najmniejszej liczby w liscie: {najmniejszy_index(lista_usera)}")


# def liczby(lista_liczb):
#     szukana = (min(lista_liczb))
#     wynik = 0
#
#     for i in lista_liczb:
#         if i != szukana:
#             wynik += 1
#     print(wynik - 1)
# lista_liczb = [42, 13, 56, 7, 12, 3, 85]
#
# liczby(lista_liczb)


def list_analys(*args):
    # lista = []
    min_pos = None
    min_val = None
    for ind, arg in enumerate(args):
        arg_int = int(arg)
        # lista.append(arg)
        if min_val == None:
            min_pos = ind
            min_val = arg_int

        elif arg_int < min_val:
            min_pos = ind
            min_val = arg_int
    print("Najmniejsza pozycja jest w: ", min_pos, " ma wartosc: ", min_val)


if __name__ == '__main__':
    list_analys(42, 13, 56, 7, 12, 3, 85)
