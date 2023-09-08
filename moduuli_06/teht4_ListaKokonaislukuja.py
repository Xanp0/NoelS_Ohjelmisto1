def lukuLaskeminen(luvut):
    laskuTulos = 0

    for luku in luvut:
        laskuTulos += luku

    return laskuTulos

lista = []
laskemaan = False

while laskemaan != True:
    uusiLuku = int(input("Anna kokonaisluku: "))
    print("Listaan lisätty uusi luku, jos annoit 0 luvun lista lasketaan läpi.")
    lista.append(uusiLuku)

    if uusiLuku == 0:
        laskemaan = True

tulos = lukuLaskeminen(lista)
print(f"Listan lukujen summa on {tulos}")
