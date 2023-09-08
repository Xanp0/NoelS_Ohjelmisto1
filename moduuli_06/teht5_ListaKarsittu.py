def listakarsiminen(luvut):

    for luku in luvut:
        if luku % 2 == 0:
            karsittuLista.append(luku)

    return

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
karsittuLista = []

listakarsiminen(lista)
print(lista)
print(karsittuLista)
