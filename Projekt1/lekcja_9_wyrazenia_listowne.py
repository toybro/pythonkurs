nowa_lista=[]
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in lista:
    if i % 2 == 0:
        print(i)
        nowa_lista.append(i*i)

print(nowa_lista)