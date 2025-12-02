f = open('plik.txt', encoding='utf-8')

# while True:
#     linia = f.readline()
#     if not linia:
#         break
#     print(linia)


linia = f.readline() # w domyśle index=0
print("Linia 1:",linia, end='')
linia = f.readline() # po kolejnym uruchomieniu index + 1
print("Linia 2:",linia, end='')