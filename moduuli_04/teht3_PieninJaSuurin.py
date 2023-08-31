komento = input("Anna luku: ")
luku = float(str(komento))
pieninLuku = suurinLuku = luku

while komento != "":
    luku = float(str(komento))
    if luku < pieninLuku:
        pieninLuku = luku
    elif luku > suurinLuku:
        suurinLuku = luku

    print("Jätä luku tyhjäksi ja paina enter, jos haluat lopettaa.")
    komento = input("Anna luku: ")

print(f"Pienin luku oli {pieninLuku} ja suurin luku oli {suurinLuku}")
