import random

arpoja = int(input("Arpakuutioiden lukumäärä: "))
kerrat = 1
arpaLuvut = []
arpaMäärä = 0

while kerrat <= arpoja:
    arpakuutio = random.randint(1, 6)
    arpaLuvut.append(arpakuutio)
    kerrat += 1

for luku in arpaLuvut:
    arpaMäärä += luku

print(f"Arpakuutioiden silmälukujen summa: {arpaMäärä}")
