import random

def noppaMuokkaus(noppaMax):
    noppaHeitto = random.randint(1, noppaMax)
    return noppaHeitto

noppaMaksimi = int(input("Montako puolta on nopassa: "))
noppaTulos = noppaMuokkaus(noppaMaksimi)

while noppaTulos != noppaMaksimi:
    print(f"Nopasta tuli {noppaTulos}.")
    noppaTulos = noppaMuokkaus(noppaMaksimi)

print(f"Numero {noppaMaksimi} tuli nopasta. Toiminnot lopetettu.")
