litraMuunnos = 3.785

def muuntaja(gallona):
    muunnettu = gallona * litraMuunnos
    return muunnettu

komento = float(input("Anna bensiinin gallonamäärä: "))
bensiini = muuntaja(komento)

while bensiini > 0:
    print(f"litra muunnos antaa {bensiini} määrän.")
    uusiKomento = float(input("Anna bensiinin gallonamäärä: "))
    bensiini = muuntaja(uusiKomento)

print("Negatiivinen määrä syötetty. Toiminnot lopetettu.")
