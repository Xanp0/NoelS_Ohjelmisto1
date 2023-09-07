# parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
# nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
voittoTulos = 6
def testi():
    noppaHeitto = random.randint(1, 6)
    return noppaHeitto

testi()
noppaTulos = 1 # fixsaa!

while noppaTulos <= voittoTulos:
    print(f"Nopasta tuli {noppaTulos}.")
    testi()

