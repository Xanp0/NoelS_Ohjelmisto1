lukuja = []
komento = float(input("Anna luku: "))
luku = float(str(komento))
kerrat = 1

while komento != "":
    luku = float(str(komento))
    lukuja.append(luku)

    if kerrat >= 5:
        komento = input("Anna luku tai lopeta painamalla Enter: ")
    else:
        komento = float(input("Anna luku: "))

    kerrat += 1

lukuja.sort()
lukuja.reverse()
print("Viisi suurinta lukua oli:")
print(lukuja[0], lukuja[1], lukuja[2], lukuja[3], lukuja[4])
