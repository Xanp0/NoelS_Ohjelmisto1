nimiJoukko = set()
luettele = False
komento = (input("Anna nimi: "))
nimiJoukko.add(komento)

while luettele != True:
    komento = (input("Anna nimi: "))

    if komento == "":
        luettele = True
    elif komento in nimiJoukko:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi lisätty, jos haluat lopettaa jätä nimi tyhjäksi.")
        nimiJoukko.add(komento)

for nimi in nimiJoukko:
    print(nimi)
