def funkcja(arg1, arg2, kwarg1=0, kwarg2=None):
    print(f"arg1={arg1}, arg2={arg2}, kwarg1={kwarg1}, kwarg2={kwarg2}")


print("funkcja(1,2):")
funkcja(1, 2)

print("funkcja(arg1=11, arg2=22):")
funkcja(arg1=11, arg2=22)

print("funkcja(33,44,55):")
funkcja(33, 44, 55)

print("funkcja(33,44,55):")
funkcja(33, kwarg2=44, arg2=55)

print("funkcja(33,44,55):")
funkcja(kwarg1=33, kwarg2=44, arg2=55, arg1=66)

# print("funkcja(33,44,55):")
# funkcja(kwarg1=33, kwarg2=44, 55, 66)

def nowa_funkcja(*args, **kwargs):
    pass

