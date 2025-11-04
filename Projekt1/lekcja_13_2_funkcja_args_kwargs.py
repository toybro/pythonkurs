def funkcja(args1, args2, kwarg1=0, kwarg2=0):
    print(f"arg1: {args1}. arg2: {args2}.\nkwarg1: {kwarg1}. kwarg2: {kwarg2}")
print("Funkcja(args1=1, args2=2, kwarg1=0, kwarg2=0)")
funkcja(1, 2)

print("Funkcja(args1=2, args2=4, kwarg1=0, kwarg2=0)")
funkcja(2, 4)

print("Funkcja(args1=2, args2=4, kwarg1=55, kwarg2=0)")
funkcja(33, 44, 55)

print("Funkcja(args1=33, args2=55, kwarg1=44, kwarg2=0)")
funkcja(33, kwarg1=44, args2=55)

#ARGUMENTY WYPISUJEMY PODCZAS URUCHOMIENIA FUNKCJI
#KWARGSY CZYLI KEYWORD ARGUMENT MOŻEMY NAZWAĆ JUZ W KODZIE FUNCKJI

def nowa_funkcja(*args, **kwargs):
    pass:
