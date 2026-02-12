def powitanie_admin(funkszyn):
    def wrapper(*args, **kwargs):

        if args and args[0] == "admin":
            print("Witaj, admin!")
        else:
            print("Witaj, userze!")
        return funkszyn(*args, **kwargs)
    return wrapper

@powitanie_admin
def zaloguj(nazwa_usera):
    print(f"Logowanie użytkownika: {nazwa_usera}")


zaloguj("admin")
zaloguj("krzysztof")