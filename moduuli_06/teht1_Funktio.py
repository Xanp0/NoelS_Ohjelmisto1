import random

def noppaTesti():
    noppaHeitto = random.randint(1, 6)
    return noppaHeitto

noppaTulos = noppaTesti()

while noppaTulos != 6:
    print(f"Nopasta tuli {noppaTulos}.")
    noppaTulos = noppaTesti()

print("Numero 6 tuli nopasta. Toiminnot lopetettu.")
